import pandas as pd
import numpy as np

league_strength_df = pd.read_csv("../data/league_strength.csv")
team_strength_df = pd.read_csv("../data/team_strength.csv")

def transform_match_data_for_prediction(team1, team2, match_data):
    # Merge in league and team strength
    match_data = match_data.merge(
        league_strength_df.rename(columns={"league_abbrev": "HOME_LEAGUE_ID", "strength": "HOME_LEAGUE_STRENGTH"}),
        on="HOME_LEAGUE_ID", how="left"
    ).merge(
        league_strength_df.rename(columns={"league_abbrev": "AWAY_LEAGUE_ID", "strength": "AWAY_LEAGUE_STRENGTH"}),
        on="AWAY_LEAGUE_ID", how="left"
    ).merge(
        team_strength_df.rename(columns={"team_name": "HOME_TEAM", "strength": "HOME_STRENGTH"}),
        on="HOME_TEAM", how="left"
    ).merge(
        team_strength_df.rename(columns={"team_name": "AWAY_TEAM", "strength": "AWAY_STRENGTH"}),
        on="AWAY_TEAM", how="left"
    )

    # Standardize columns into long format
    home_df = match_data[[
        "DATE", "HOME_TEAM", "RESULT", "HOME_TEAM_SCORE", "AWAY_TEAM_SCORE",
        "HOME_STRENGTH", "HOME_LEAGUE_STRENGTH",
        "HOME_TARGET", "HOME_FOULS", "HOME_CORNERS", "HOME_YELLOW", "HOME_RED"
    ]].copy()
    home_df.rename(columns=lambda x: x.replace("HOME_", ""), inplace=True)
    home_df["TEAM"] = home_df["TEAM"]
    home_df["VENUE"] = "HOME"

    away_df = match_data[[
        "DATE", "AWAY_TEAM", "RESULT", "AWAY_TEAM_SCORE", "HOME_TEAM_SCORE",
        "AWAY_STRENGTH", "AWAY_LEAGUE_STRENGTH",
        "AWAY_TARGET", "AWAY_FOULS", "AWAY_CORNERS", "AWAY_YELLOW", "AWAY_RED"
    ]].copy()
    away_df.rename(columns=lambda x: x.replace("AWAY_", ""), inplace=True)
    away_df["TEAM"] = away_df["TEAM"]
    away_df["VENUE"] = "AWAY"

    # Normalize column names
    away_df.columns = home_df.columns = [
        "DATE", "TEAM", "RESULT", "GOALS_FOR", "GOALS_AGAINST",
        "STRENGTH", "LEAGUE_STRENGTH",
        "TARGET", "FOULS", "CORNERS", "YELLOW", "RED", "VENUE"
    ]

    matches_long = pd.concat([home_df, away_df])
    matches_long["DATE"] = pd.to_datetime(matches_long["DATE"])
    matches_long = matches_long.sort_values(["TEAM", "DATE"])
    '''
    # Map results to points for form
    matches_long["POINTS"] = matches_long["RESULT"].map({
        "H": lambda row: 3 if row["VENUE"] == "HOME" else 0,
        "A": lambda row: 3 if row["VENUE"] == "AWAY" else 0,
        "D": 1
    }).apply(lambda x: x if not callable(x) else x(row))  # handle lambdas
    '''
    def compute_team_stats(team_name):
        team_matches = matches_long[matches_long["TEAM"] == team_name].sort_values("DATE")
        recent = team_matches.iloc[-3:]

        stats = {
            "STRENGTH": recent["STRENGTH"].iloc[-1] if not recent["STRENGTH"].isna().all() else None,
            "LEAGUE_STRENGTH": recent["LEAGUE_STRENGTH"].iloc[-1] if not recent["LEAGUE_STRENGTH"].isna().all() else None,
            "GOALS_FOR_LAST3": recent["GOALS_FOR"].mean(),
            "GOALS_AGAINST_LAST3": recent["GOALS_AGAINST"].mean(),
            "STRENGTH_LAST3": recent["STRENGTH"].mean(),
            "LEAGUE_STRENGTH_LAST3": recent["LEAGUE_STRENGTH"].mean(),
            "TARGET_LAST3": recent["TARGET"].mean(),
            "CORNERS_LAST3": recent["CORNERS"].mean()#,
            #"FORM_LAST3": recent["POINTS"].sum()
        }

        return stats

    # Compute features
    home_stats = compute_team_stats(team1)
    away_stats = compute_team_stats(team2)

    # Combine into one row
    row = {
        f"HOME_{k}": v for k, v in home_stats.items()
    }
    row.update({
        f"AWAY_{k}": v for k, v in away_stats.items()
    })

    # Add engineered features
    row["STRENGTH_DIFF"] = row["HOME_STRENGTH"] - row["AWAY_STRENGTH"] if row["HOME_STRENGTH"] and row["AWAY_STRENGTH"] else None
    row["LEAGUE_STRENGTH_DIFF"] = row["HOME_LEAGUE_STRENGTH"] - row["AWAY_LEAGUE_STRENGTH"] if row["HOME_LEAGUE_STRENGTH"] and row["AWAY_LEAGUE_STRENGTH"] else None
    row["HOME_GOAL_DIFF_LAST3"] = row["HOME_GOALS_FOR_LAST3"] - row["HOME_GOALS_AGAINST_LAST3"]
    row["AWAY_GOAL_DIFF_LAST3"] = row["AWAY_GOALS_FOR_LAST3"] - row["AWAY_GOALS_AGAINST_LAST3"]

    # Dummy HOME_WIN flag for compatibility (can be left blank or computed later)
    row["HOME_WIN"] = None

    return pd.DataFrame([row])