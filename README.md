# CWCPredictions
Attempting to predict the matches of the 2025 FIFA Club World Cup

## Sources
Used this source to obtain team rankings and league rankings, tables are manually typed: https://globalfootballrankings.com

Source for the league training data: https://www.kaggle.com/datasets/adamgbor/club-football-match-data-2000-2025?resource=download

Source for UEFA Champions League training Data: https://www.kaggle.com/datasets/cbxkgl/uefa-champions-league-2016-2022-data

Source for CONMEBOL Libertadores training data: https://www.kaggle.com/datasets/ernestonlm/conmebol-libertadores-results-from-2011-to-2022

Manually entered data from previous Club World Cup games dating back to the 2022 tournament. If needed, I also added the previous three games for teams in the tournament. Data from SofaScore.

# Predictions

## **Round 1**
#### Group A
| Date | Home Team | Away Team | Result | Total Goals | Pred Result | Pred Goals |
|------|-----------|-----------|--------|-------------|---------------------|--------------------|
|Jun 14, 2025| Al Ahly <img src="https://flagcdn.com/w40/eg.png" width="20"/> | Inter Miami <img src="https://flagcdn.com/w40/us.png" width="20"/>| Draw | 0 | ✅ | ✅ |
|Jun 15, 2025| Palmeiras <img src="https://flagcdn.com/w40/br.png" width="20"/> | Porto <img src="https://flagcdn.com/w40/pt.png" width="20"/> | Draw | 0 | ✅ | ✅ |

#### Group B
| Date | Home Team | Away Team | Result | Total Goals | Pred Result | Pred Goals |
|------|-----------|-----------|--------|-------------|---------------------|--------------------|
|Jun 15, 2025| Paris SG <img src="https://flagcdn.com/w40/fr.png" width="20"/> | Atletico Madrid <img src="https://flagcdn.com/w40/es.png" width="20"/>| Paris SG | 4 | ✅ | ❌ |
|Jun 15, 2025| Botafogo <img src="https://flagcdn.com/w40/br.png" width="20"/> | Seattle Sounders <img src="https://flagcdn.com/w40/us.png" width="20"/> | Botafogo | 3 | ✅ | ✅ |

#### Group C
| Date | Home Team | Away Team | Result | Total Goals | Pred Result | Pred Goals |
|------|-----------|-----------|--------|-------------|---------------------|--------------------|
|Jun 15, 2025| Bayern Munich <img src="https://flagcdn.com/w40/de.png" width="20"/> | Auckland City <img src="https://flagcdn.com/w40/nz.png" width="20"/>| Bayern Munich | 10 | ✅ | ✅ |
|Jun 16, 2025| Boca Juniors <img src="https://flagcdn.com/w40/ar.png" width="20"/> | Benfica <img src="https://flagcdn.com/w40/pt.png" width="20"/> | Draw | 4 | ✅ | ❌ |

#### Group D
| Date | Home Team | Away Team | Result | Total Goals | Pred Result | Pred Goals |
|------|-----------|-----------|--------|-------------|---------------------|--------------------|
|Jun 16, 2025| Chelsea <img src="https://flagcdn.com/w40/gb.png" width="20"/> | Los Angeles FC <img src="https://flagcdn.com/w40/us.png" width="20"/>| Chelsea | 2 | ✅ | ✅ |
|Jun 16, 2025| Flamengo <img src="https://flagcdn.com/w40/br.png" width="20"/> | Esperance <img src="https://flagcdn.com/w40/tn.png" width="20"/> | Flamengo | 2 | ✅ | ✅ |

#### Group E
| Date | Home Team | Away Team | Result | Total Goals | Pred Result | Pred Goals |
|------|-----------|-----------|--------|-------------|---------------------|--------------------|
|Jun 17, 2025| River Plate <img src="https://flagcdn.com/w40/ar.png" width="20"/> | Urawa Reds <img src="https://flagcdn.com/w40/jp.png" width="20"/>| River Plate | 4 | ✅ | ❌ |
|Jun 17, 2025| Monterrey <img src="https://flagcdn.com/w40/mx.png" width="20"/> | Inter <img src="https://flagcdn.com/w40/it.png" width="20"/> | Draw | 2 | ❌ | ✅ |

#### Group F
| Date | Home Team | Away Team | Result | Total Goals | Pred Result | Pred Goals |
|------|-----------|-----------|--------|-------------|---------------------|--------------------|
|Jun 17, 2025| Fluminense <img src="https://flagcdn.com/w40/br.png" width="20"/> | Dortmund <img src="https://flagcdn.com/w40/de.png" width="20"/>| Draw | 0 | ❌ | ✅ |
|Jun 17, 2025| Ulsan <img src="https://flagcdn.com/w40/kr.png" width="20"/> | Mamelodi Sundowns <img src="https://flagcdn.com/w40/za.png" width="20"/> | Mamelodi Sundowns | 1 | ❌ | ❌ |

#### Group G
| Date | Home Team | Away Team | Result | Total Goals | Pred Result | Pred Goals |
|------|-----------|-----------|--------|-------------|---------------------|--------------------|
|Jun 18, 2025| Man City <img src="https://flagcdn.com/w40/gb.png" width="20"/> | Wydad Casablanca <img src="https://flagcdn.com/w40/ma.png" width="20"/>| Man City | 2 | ✅ | ✅ |
|Jun 18, 2025| Al-Ain <img src="https://flagcdn.com/w40/ae.png" width="20"/> | Juventus <img src="https://flagcdn.com/w40/it.png" width="20"/> | Juventus | 5 | ✅ | ❌ |

#### Group H
| Date | Home Team | Away Team | Result | Total Goals | Pred Result | Pred Goals |
|------|-----------|-----------|--------|-------------|---------------------|--------------------|
|Jun 18, 2025| Real Madrid <img src="https://flagcdn.com/w40/es.png" width="20"/> | Al Hilal <img src="https://flagcdn.com/w40/sa.png" width="20"/>| Draw | 2 | ✅ | ❌ |
|Jun 18, 2025| Pachuca <img src="https://flagcdn.com/w40/mx.png" width="20"/> | Salzburg <img src="https://flagcdn.com/w40/at.png" width="20"/> | Salzburg | 3 | ❌ | ✅ |


After round 1, our result model sucessfully predicted 12/16 of the matches correctly, giving us a 75.0% accuracy for the first round. 

We have also successfully predicted 10/16 of the goal totals correctly. This gives us a 62.5% accuracy for the first round. 

## **Round 2**
#### Group A
| Date | Home Team | Away Team | Result | Total Goals | Pred Result | Pred Goals |
|------|-----------|-----------|--------|-------------|---------------------|--------------------|
|Jun 19, 2025| Inter Miami <img src="https://flagcdn.com/w40/us.png" width="20"/> | Porto <img src="https://flagcdn.com/w40/pt.png" width="20"/>| Inter Miami | 3 | ✅ | ✅ |
|Jun 19, 2025| Palmeiras <img src="https://flagcdn.com/w40/br.png" width="20"/> | Al Ahly <img src="https://flagcdn.com/w40/eg.png" width="20"/>  | Palmeiras | 2 | ✅ | ✅ |

#### Group B
| Date | Home Team | Away Team | Result | Total Goals | Pred Result | Pred Goals |
|------|-----------|-----------|--------|-------------|---------------------|--------------------|
|Jun 19, 2025| Paris SG <img src="https://flagcdn.com/w40/fr.png" width="20"/> | Botafogo <img src="https://flagcdn.com/w40/br.png" width="20"/>| Botafogo | 1 | ❌ | ✅ | 
|Jun 19, 2025| Seattle Sounders <img src="https://flagcdn.com/w40/us.png" width="20"/> | Atletico Madrid <img src="https://flagcdn.com/w40/es.png" width="20"/> | Athletico Madrid | 4 | ✅ | ❌ |

#### Group C
| Date | Home Team | Away Team | Result | Total Goals | Pred Result | Pred Goals |
|------|-----------|-----------|--------|-------------|---------------------|--------------------|
|Jun 20, 2025| Bayern Munich <img src="https://flagcdn.com/w40/de.png" width="20"/> | Boca Juniors <img src="https://flagcdn.com/w40/ar.png" width="20"/>| Bayern Munich | 3 | ✅ | ✅ |
|Jun 20, 2025| Benfica <img src="https://flagcdn.com/w40/pt.png" width="20"/> | Auckland City <img src="https://flagcdn.com/w40/nz.png" width="20"/>| Benfica | 6 | ✅ | ✅ |

#### Group D
| Date | Home Team | Away Team | Result | Total Goals | Pred Result | Pred Goals |
|------|-----------|-----------|--------|-------------|---------------------|--------------------|
|Jun 20, 2025|  Los Angeles FC <img src="https://flagcdn.com/w40/us.png" width="20"/>| Esperance <img src="https://flagcdn.com/w40/tn.png" width="20"/> | Esperance | 1 | ❌ | ✅ |
|Jun 20, 2025| Flamengo <img src="https://flagcdn.com/w40/br.png" width="20"/> | Chelsea <img src="https://flagcdn.com/w40/gb.png" width="20"/> | Flamengo | 4 | ❌ | ❌ |

#### Group E
| Date | Home Team | Away Team | Result | Total Goals | Pred Result | Pred Goals |
|------|-----------|-----------|--------|-------------|---------------------|--------------------|
|Jun 21, 2025| Inter <img src="https://flagcdn.com/w40/it.png" width="20"/> | Urawa Reds <img src="https://flagcdn.com/w40/jp.png" width="20"/>| Inter | 3 | ✅ | ✅ |
|Jun 21, 2025| River Plate <img src="https://flagcdn.com/w40/ar.png" width="20"/> | Monterrey <img src="https://flagcdn.com/w40/mx.png" width="20"/> | Draw | 0 | ✅ | ✅ |

#### Group F
| Date | Home Team | Away Team | Result | Total Goals | Pred Result | Pred Goals |
|------|-----------|-----------|--------|-------------|---------------------|--------------------|
|Jun 21, 2025| Fluminense <img src="https://flagcdn.com/w40/br.png" width="20"/> | Ulsan <img src="https://flagcdn.com/w40/kr.png" width="20"/> | Fluminense | 6 | ✅ | ❌ |
|Jun 21, 2025| Mamelodi Sundowns <img src="https://flagcdn.com/w40/za.png" width="20"/> | Dortmund <img src="https://flagcdn.com/w40/de.png" width="20"/>| Dortmund | 7 | ✅ | ❌ |

#### Group G
| Date | Home Team | Away Team | Result | Total Goals | Pred Result | Pred Goals |
|------|-----------|-----------|--------|-------------|---------------------|--------------------|
|Jun 22, 2025| Man City <img src="https://flagcdn.com/w40/gb.png" width="20"/> | Al-Ain <img src="https://flagcdn.com/w40/ae.png" width="20"/> | Man City | 6 | ✅ | ❌ |
|Jun 22, 2025| Juventus <img src="https://flagcdn.com/w40/it.png" width="20"/> | Wydad Casablanca <img src="https://flagcdn.com/w40/ma.png" width="20"/>| Juventus | 5 | ✅ | ✅ |

#### Group H
| Date | Home Team | Away Team | Result | Total Goals | Pred Result | Pred Goals |
|------|-----------|-----------|--------|-------------|---------------------|--------------------|
|Jun 22, 2025| Real Madrid <img src="https://flagcdn.com/w40/es.png" width="20"/> | Pachuca <img src="https://flagcdn.com/w40/mx.png" width="20"/>| Real Madrid | 4 | ✅ | ✅ |
|Jun 22, 2025| Salzburg <img src="https://flagcdn.com/w40/at.png" width="20"/> | Al Hilal <img src="https://flagcdn.com/w40/sa.png" width="20"/>| Draw | 0 | ✅ | ✅ |

After round 2, the model created to predict the result has predicted 13/16 of the results correctly, giving us a 81.2% accuracy for the just this round. Overall, throughout rounds 1 and 2 the model has predicted 25/32 matches correctly yielding a 78.1% accuracy.

We have also successfully predicted 11/16 of the goal totals correctly in this round. This gives us a 68.8% accuracy for the second round. Througout both rounds we have 21/32 predictions correct or a 65.6% accuracy.

## **Round 3**

#### Group A
| Date | Home Team | Away Team | Result | Total Goals | Pred Result | Pred Goals |
|------|-----------|-----------|--------|-------------|---------------------|--------------------|
|Jun 23, 2025| Inter Miami <img src="https://flagcdn.com/w40/us.png" width="20"/> | Palmeiras <img src="https://flagcdn.com/w40/br.png" width="20"/> | Draw | 4 | ✅ | ❌ |
|Jun 23, 2025| Porto <img src="https://flagcdn.com/w40/pt.png" width="20"/> | Al Ahly <img src="https://flagcdn.com/w40/eg.png" width="20"/>  | Draw | 8 | ✅ | ❌ | 

#### Group B
| Date | Home Team | Away Team | Result | Total Goals | Pred Result | Pred Goals |
|------|-----------|-----------|--------|-------------|---------------------|--------------------|
|Jun 23, 2025| Atletico Madrid <img src="https://flagcdn.com/w40/es.png" width="20"/> | Botafogo <img src="https://flagcdn.com/w40/br.png" width="20"/>| Atletico Madrid | 1 | ✅ | ✅ |
|Jun 23, 2025| Seattle Sounders <img src="https://flagcdn.com/w40/us.png" width="20"/> | Paris SG <img src="https://flagcdn.com/w40/fr.png" width="20"/> | Paris SG | 2 | ✅ | ❌ |

#### Group C
| Date | Home Team | Away Team | Result | Total Goals | Pred Result | Pred Goals |
|------|-----------|-----------|--------|-------------|---------------------|--------------------|
|Jun 24, 2025| Auckland City <img src="https://flagcdn.com/w40/nz.png" width="20"/> | Boca Juniors <img src="https://flagcdn.com/w40/ar.png" width="20"/>| Draw | 2 | ❌ | ✅ |
|Jun 24, 2025| Benfica <img src="https://flagcdn.com/w40/pt.png" width="20"/> | Bayern Munich <img src="https://flagcdn.com/w40/de.png" width="20"/>| Benfica | 1 | ✅ | ✅ |

#### Group D
| Date | Home Team | Away Team | Result | Total Goals | Pred Result | Pred Goals |
|------|-----------|-----------|--------|-------------|---------------------|--------------------|
|Jun 24, 2025|  Los Angeles FC <img src="https://flagcdn.com/w40/us.png" width="20"/>| Flamengo <img src="https://flagcdn.com/w40/br.png" width="20"/> | Draw | 2 | ✅ | ✅ |
|Jun 24, 2025| Esperance <img src="https://flagcdn.com/w40/tn.png" width="20"/> | Chelsea <img src="https://flagcdn.com/w40/gb.png" width="20"/> | Chelsea | 3 | ✅ | ✅ |

#### Group E
| Date | Home Team | Away Team | Result | Total Goals | Pred Result | Pred Goals |
|------|-----------|-----------|--------|-------------|---------------------|--------------------|
|Jun 25, 2025| Inter <img src="https://flagcdn.com/w40/it.png" width="20"/> | River Plate <img src="https://flagcdn.com/w40/ar.png" width="20"/>| Inter | 2 | ✅ | ❌ |
|Jun 25, 2025| Urawa Reds <img src="https://flagcdn.com/w40/jp.png" width="20"/> | Monterrey <img src="https://flagcdn.com/w40/mx.png" width="20"/> | Monterrey | 4 |❌ |❌ |

#### Group F
| Date | Home Team | Away Team | Result | Total Goals | Pred Result | Pred Goals |
|------|-----------|-----------|--------|-------------|---------------------|--------------------|
|Jun 25, 2025| Dortmund <img src="https://flagcdn.com/w40/de.png" width="20"/> | Ulsan <img src="https://flagcdn.com/w40/kr.png" width="20"/> | Dortmund | 1 | ✅ | ✅ |
|Jun 25, 2025| Mamelodi Sundowns <img src="https://flagcdn.com/w40/za.png" width="20"/> | Fluminense <img src="https://flagcdn.com/w40/br.png" width="20"/> | Draw | 0 |✅ | ✅ |

#### Group G
| Date | Home Team | Away Team | Result | Total Goals | Pred Result | Pred Goals |
|------|-----------|-----------|--------|-------------|---------------------|--------------------|
|Jun 26, 2025| Wydad Casablanca <img src="https://flagcdn.com/w40/ma.png" width="20"/> | Al-Ain <img src="https://flagcdn.com/w40/ae.png" width="20"/> | Al-Ain | 3 | ❌ | ✅ |
|Jun 26, 2025| Juventus <img src="https://flagcdn.com/w40/it.png" width="20"/> | Man City <img src="https://flagcdn.com/w40/gb.png" width="20"/>| Man City | 7 | ✅ | ❌ |

#### Group H
| Date | Home Team | Away Team | Result | Total Goals | Pred Result | Pred Goals |
|------|-----------|-----------|--------|-------------|---------------------|--------------------|
|Jun 26, 2025| Al Hilal <img src="https://flagcdn.com/w40/sa.png" width="20"/> | Pachuca <img src="https://flagcdn.com/w40/mx.png" width="20"/>| Al Hilal | 2 | ✅ | ✅ |
|Jun 26, 2025| Salzburg <img src="https://flagcdn.com/w40/at.png" width="20"/> | Real Madrid <img src="https://flagcdn.com/w40/es.png" width="20"/>| Real Madrid | 3 | ✅ | ✅ |

In Round 3, the model successfully predicted 13/16 of the matches. This gives us a 81.3% accuracy for round 3. Through the entire tournament we have 38/48 correct predictions, giving us a 79.2% accuracy. 

We have predicted 10/16 of the total goals for the matches correctly. Through the entire tournament we have a 31/48, or a 64.6% accuracy. 

## ** Round of 16 **
| Date | Home Team | Away Team | Result after 90'| Total Goals Through 90'| Pred Result | Pred Goals |
|------|-----------|-----------|--------|-------------|---------------------|--------------------|
|Jun 28, 2025| Palmeiras <img src="https://flagcdn.com/w40/br.png" width="20"/> | Botafogo <img src="https://flagcdn.com/w40/br.png" width="20"/>| Draw | 0 | ✅|✅|
|Jun 28, 2025| Benfica <img src="https://flagcdn.com/w40/pt.png" width="20"/> | Chelsea <img src="https://flagcdn.com/w40/gb.png" width="20"/> | Draw | 2 | ✅|❌|
|Jun 29, 2025| Paris SG <img src="https://flagcdn.com/w40/fr.png" width="20"/> | Inter Miami <img src="https://flagcdn.com/w40/us.png" width="20"/> | Paris SG|4|✅|❌|
|Jun 29, 2025| Flamengo <img src="https://flagcdn.com/w40/br.png" width="20"/> | Bayern Munich <img src="https://flagcdn.com/w40/de.png" width="20"/> | Bayern Munich | 6|✅|❌|
|Jun 30, 2025| Inter <img src="https://flagcdn.com/w40/it.png" width="20"/> | Fluminense <img src="https://flagcdn.com/w40/br.png" width="20"/> | Fluminense | 2|❌ | ✅|
|Jun 30, 2025| Man City <img src="https://flagcdn.com/w40/gb.png" width="20"/> | Al Hilal <img src="https://flagcdn.com/w40/sa.png" width="20"/> |Draw|4|✅|✅|
|Jul 1, 2025| Real Madrid <img src="https://flagcdn.com/w40/es.png" width="20"/> | Juventus <img src="https://flagcdn.com/w40/it.png" width="20"/> |Real Madrid|1|✅|✅|
|Jul 1, 2025| Dortmund <img src="https://flagcdn.com/w40/de.png" width="20"/> | Monterrey <img src="https://flagcdn.com/w40/mx.png" width="20"/> |Dortmund|3|✅|✅|

In this round, we predicted 7/8 of the matches correctly. Through the entire tournament we have a 45/56 or a 80.3% accuracy. 

For predicting the number of goals, this round had an accuracy of 5/8. Through the entire tournament, we have a 36/56 accuracy or a 64.3% accuracy.
