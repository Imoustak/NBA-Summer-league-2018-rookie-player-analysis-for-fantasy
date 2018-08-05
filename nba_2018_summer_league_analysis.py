import pandas as pd
import matplotlib.pyplot as pl

# read csv file as pandas dataframe
stats = pd.read_csv( '/Users/ioannismoustakis/Desktop/other/fantasy_data/summer_league_analysis/\
rookies_summer_league_2018_stats.csv', delimiter=';')
print(stats.head())  # print head of the data
print(stats.info())  # print info of the data
#stats['SCORE'] = 0   # create column SCORE

# create a dataframe for each position
PF_players = stats[stats['POS'] == 'PF']
SF_players = stats[stats['POS'] == 'SF']
C_players = stats[stats['POS'] == 'C']
PG_players = stats[stats['POS'] == 'PG']
SG_players = stats[stats['POS'] == 'SG']
print(PF_players.head())
print(PF_players.info())

# create the scoring formula for PFs
PF_players['SCORE'] = 0.05*PF_players['GP']/PF_players['GP'].max() \
                      + 0.15*PF_players['PPG']/PF_players['PPG'].max() + 0.15*PF_players['RPG']/PF_players['RPG'].max()\
                      + 0.20*PF_players['BPG']/PF_players['BPG'].max() - 0.05*PF_players['TOV'] / \
                      PF_players['TOV'].max() \
                      + 0.10*((PF_players['3PA']/PF_players['3PA'].max())*(PF_players['3P%'] /
                                                                           PF_players['3P%'].max())) \
                      + 0.15*PF_players['FG%']/PF_players['FG%'].max() \
                      + 0.05*((PF_players['FTA']/PF_players['FTA'].max())*(PF_players['FT%']/PF_players['FT%'].max())) \
                      + 0.10*PF_players['MPG'] + 0.05*PF_players['FT%']/PF_players['FT%'].max() \
                      + 0.05*PF_players['SPG']/PF_players['SPG'].max()

# sort the PF players based on the SCORE and pick only the best 25
PF_players = PF_players.sort_values('SCORE', ascending=False)
PF_players = PF_players.iloc[0:25, PF_players.columns.get_indexer(['Player', 'SCORE', 'POS', 'TEAM'])]
# print(PF_players)

# create the scoring formula for SFs
SF_players['SCORE'] = 0.05*SF_players['GP']/SF_players['GP'].max() \
                      + 0.20*SF_players['PPG']/SF_players['PPG'].max() + 0.10*SF_players['RPG'] / \
                      SF_players['RPG'].max() \
                      + 0.10*SF_players['BPG']/SF_players['BPG'].max() - 0.05*SF_players['TOV'] / \
                      SF_players['TOV'].max() \
                      + 0.05*((SF_players['3PA']/SF_players['3PA'].max())*(SF_players['3P%']/
                                                                           SF_players['3P%'].max())) \
                      + 0.10*SF_players['FG%']/SF_players['FG%'].max() + 0.05*SF_players['FT%'] / \
                      SF_players['FT%'].max() \
                      + 0.05*((SF_players['FTA']/SF_players['FTA'].max())*(SF_players['FT%']/SF_players['FT%'].max())) \
                      + 0.10*SF_players['MPG'] + 0.15*SF_players['SPG']/SF_players['SPG'].max() \
                      + 0.05*SF_players['APG']/SF_players['APG'].max()

# sort the SF players based on the SCORE and pick only the best 25
SF_players = SF_players.sort_values('SCORE', ascending=False)
SF_players = SF_players.iloc[0:25, SF_players.columns.get_indexer(['Player', 'SCORE', 'POS', 'TEAM'])]
# print(SF_players)

# create the scoring formula for PGs
PG_players['SCORE'] = 0.05*PG_players['GP']/PG_players['GP'].max() \
                      + 0.15*PG_players['PPG']/PG_players['PPG'].max() + 0.05*PG_players['RPG'] / \
                      PG_players['RPG'].max() \
                      - 0.10*PG_players['TOV']/PG_players['TOV'].max() \
                      + 0.15*((PG_players['3PA']/PG_players['3PA'].max())*(PG_players['3P%'] /
                                                                                   PG_players['3P%'].max())) \
                      + 0.05*PG_players['FG%']/PG_players['FG%'].max() + 0.10*PG_players['FT%'] / \
                      PG_players['FT%'].max() \
                      + 0.10*((PG_players['FTA']/PG_players['FTA'].max())*(PG_players['FT%']/PG_players['FT%'].max())) \
                      + 0.10*PG_players['MPG'] + 0.15*PG_players['SPG']/PG_players['SPG'].max() \
                      + 0.20*PG_players['APG']/PG_players['APG'].max()

# sort the PG players based on the SCORE and pick only the best 25
PG_players = PG_players.sort_values('SCORE', ascending=False)
PG_players = PG_players.iloc[0:25, PG_players.columns.get_indexer(['Player', 'SCORE', 'POS', 'TEAM'])]
# print(PG_players)

# create the scoring formula for SGs
SG_players['SCORE'] = 0.05*SG_players['GP']/SG_players['GP'].max() \
                      + 0.25*SG_players['PPG']/SG_players['PPG'].max() + 0.05*SG_players['RPG'] / \
                      SG_players['RPG'].max() \
                      - 0.05*SG_players['TOV']/SG_players['TOV'].max() \
                      + 0.15*((SG_players['3PA']/SG_players['3PA'].max())*(SG_players['3P%']/
                                                                                   SG_players['3P%'].max())) \
                      + 0.10*SG_players['FG%']/SG_players['FG%'].max() + 0.05*SG_players['FT%'] / \
                      SG_players['FT%'].max() \
                      + 0.10*((SG_players['FTA']/SG_players['FTA'].max())*(SG_players['FT%']/SG_players['FT%'].max())) \
                      + 0.10*SG_players['MPG'] + 0.15*SG_players['SPG']/SG_players['SPG'].max() \
                      + 0.05*SG_players['APG']/SG_players['APG'].max()

# sort the SG players based on the SCORE and pick only the best 25
SG_players = SG_players.sort_values('SCORE', ascending=False)
SG_players = SG_players.iloc[0:25, SG_players.columns.get_indexer(['Player', 'SCORE', 'POS', 'TEAM'])]
print(SG_players)

# create the scoring formula for Cs
C_players['SCORE'] = 0.05*C_players['GP']/C_players['GP'].max() \
                     + 0.10*C_players['PPG']/C_players['PPG'].max() + 0.20*C_players['RPG']/C_players['RPG'].max() \
                     + 0.20*C_players['BPG']/C_players['BPG'].max() - 0.05*C_players['TOV']/C_players['TOV'].max() \
                     + 0.05*((C_players['3PA']/C_players['3PA'].max())*(C_players['3P%'] /
                                                                        C_players['3P%'].max())) \
                     + 0.20*C_players['FG%']/C_players['FG%'].max() + 0.05*C_players['FT%']/C_players['FT%'].max() \
                     + 0.05*((C_players['FTA']/C_players['FTA'].max())*(C_players['FT%']/C_players['FT%'].max())) \
                     + 0.10*C_players['MPG']  \
                     + 0.025*C_players['APG']/C_players['APG'].max() + 0.025*C_players['SPG']/C_players['SPG'].max()

# sort the C players based on the SCORE and pick only the best 25
C_players = C_players.sort_values('SCORE', ascending=False)
C_players = C_players.iloc[0:25, C_players.columns.get_indexer(['Player', 'SCORE', 'POS', 'TEAM'])]
#print(C_players)

# create a frrame with all 5 datasets for each position's best 25 players
frames = [SF_players, PF_players, PG_players, C_players, SG_players]
top_players_per_position = pd.concat(frames)
#print(top_players_per_position)
top_players_per_position = top_players_per_position.sort_values('SCORE', ascending=False)
print(top_players_per_position)

# get the best 25 players and plot them in an horizontal bar
top_25_players = top_players_per_position.iloc[0:25, top_players_per_position.columns.get_indexer(['Player', 'SCORE', 'POS', 'TEAM'])]
ax = top_25_players.plot(y='SCORE', x='Player', kind='barh', rot=0)
pl.show()








