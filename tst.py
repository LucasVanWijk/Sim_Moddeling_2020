# import pandas as pd

# Ajax      =  [None, [65,17,18], [54,21,25], [74,14,12], [78,13,9]]
# Feyenoord =  [[30,21,49], None, [37,24,39], [51,22,27], [60,21,19]]
# PSV       =  [[39,22,39], [54,22,24], None, [62,20,18], [62,22,16]]
# FCUtrecht =  [[25,14,61], [37,23,40], [29,24,47], None, [52,23,25]]
# WillemII  =  [[17,18,65], [20,26,54], [23,24,53], [37,25,38], None]

# teams = ["Ajax", "Feyenoord", "PSV", "FCUtrecht", "WillemII"]
# table = pd.DataFrame([Ajax, Feyenoord, PSV, FCUtrecht, WillemII])
# table = table.set_index(pd.Index(teams))
# table.columns = teams

# import MerseneTwister
# import random as r
# RandomClass = MerseneTwister.Mersenne()
# random = RandomClass.randomNumber

# #Makes a list with 100 items. If the win chanse is 30 than 30 items in this list are 3 (you get 3 points for a win)
# #Then randomly picks a item in this list
# determinHomePoints = lambda chan: ([3]*chan[0] + [1]*chan[1] + [0]*chan[2])[random([0,99])] if chan != None else None
# determinResult = lambda homePoints: (homePoints,{3:0, 1:1, 0:3}[homePoints]) if homePoints != None else None

# def determinMotivation(past):
#     if past == [3,3,3]:
#         return [10,5,-15]
#     elif past == [0,0,0]:
#         return [-10,-5,15]
#     elif past[0] == 3:
#         return [5,0,-5]
#     elif past[0] == 0:
#         return [-5,0,5]
#     else:
#         return [0,0,0]


# def runSim():
#     leaqueTable = table.copy()
#     dictOfTeams = {team:0 for team in teams}
#     for index, row in leaqueTable.iterrows():
#         pastScore = [None,None,None]
#         for colum in list(leaqueTable):
#             chanses = leaqueTable[colum][index]
#             if chanses == None:
#                 continue
            
#             chanses = [a + b for a, b in zip(determinMotivation(pastScore), leaqueTable[colum][index])]
#             pointsForHomeTeam = determinHomePoints(chanses)
#             result = determinResult(pointsForHomeTeam)
#             # colum == awayteam index == hometeam
#             dictOfTeams[index] += result[0]
#             dictOfTeams[colum] += result[1]
#             pastScore[1:2] = pastScore[0:1].copy()
#             pastScore[0] = result[0]

#     ranking = pd.Series(dictOfTeams).sort_values(ascending=False)
#     return ranking

# def runSimulations(numberOfSimulations):
#     rankingNumbersDict = {i+1:0 for i in range(len(teams))}
#     rankingTeams = {team: rankingNumbersDict.copy() for team in teams}
#     for simNummer in range(numberOfSimulations):
#         seasonRanking = runSim()
#         ii = 0
#         for i, v in seasonRanking.iteritems():
#             rankingTeams[i][ii + 1] += 1
#             #Checks if the team is not tied with the one above
#             if (ii+1 != len(seasonRanking)-1) and (v != seasonRanking[ii+1]):
#                 ii += 1
                
#     return rankingTeams 


# def displaySimulationsResult(numberOfSimulations=100):
#     print((pd.DataFrame.from_dict(runSimulations(numberOfSimulations), orient='index') /numberOfSimulations) * 100)

# displaySimulationsResult(100)