# NBA-Summer-league-2018-rookie-player-analysis-for-fantasy

This repository is an attempt to analyze the 2018  NBA summer league rooke player's performance for fantasy purposes.

Methodology used: \n
Using the dataset 'rookies_summer_league_2018_stats.csv' I attempt to categorize NBA rookie players based on their performance in the 2018 summer league. Players are separated according to their primary position and based on their position, they receive a score from several statistical categories. The formulas used were made to best match my league's scoring( Yahoo 9 cat leageue), at least in my opinion. Please feel free to comment or suggest modifications. 

Formulas used(number % is the category's contribution to the player's score):
PowerForwards:
GamesPlayed 5%
PointsPerGame 15%
ReboundsPerGame 15%
BlocksPerGame 20%
TurnoversPerGame -5%
3PointsMade 10%
FieldGoalPercentage 15%
FreeThrowsMade 5%
FreeThrowsPercentage 5%
MinutesPerGame 10%
StealsPerGame 5%

ShootingForwards:
GamesPlayed 5%
PointsPerGame 20%
ReboundsPerGame 15%
BlocksPerGame 10%
TurnoversPerGame -5%
3PointsMade 5%
FieldGoalPercentage 10%
FreeThrowsMade 5%
FreeThrowsPercentage 5%
MinutesPerGame 10%
StealsPerGame 15%
AssistsPerGame 5%

PointGuards:
GamesPlayed 5%
PointsPerGame 15%
ReboundsPerGame 5%
TurnoversPerGame -10%
3PointsMade 15%
FieldGoalPercentage 5%
FreeThrowsMade 10%
FreeThrowsPercentage 10%
MinutesPerGame 10%
StealsPerGame 15%
AssistsPerGame 20%

ShootingGuards:
GamesPlayed 5%
PointsPerGame 25%
ReboundsPerGame 5%
TurnoversPerGame -5%
3PointsMade 15%
FieldGoalPercentage 10%
FreeThrowsMade 10%
FreeThrowsPercentage 5%
MinutesPerGame 10%
StealsPerGame 15%
AssistsPerGame 5%

Centers:
GamesPlayed 5%
PointsPerGame 10%
ReboundsPerGame 20%
BlocksPerGame 20%
TurnoversPerGame -5%
3PointsMade 5%
FieldGoalPercentage 20%
FreeThrowsMade 5%
FreeThrowsPercentage 5%
MinutesPerGame 10%
StealsPerGame 2.5%
AssistsPerGame 2.5%

Usage:
1)change the path for the input dataset 
2)install modules imported and run the python script 
