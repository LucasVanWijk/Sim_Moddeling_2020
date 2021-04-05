import pandas as pd
import math
import random as random
import matplotlib.pyplot as plt
from matplotlib.ticker import PercentFormatter
import numpy as np


Ajax =	 [3.2, 0.9, 3.1, 0.6]
Feyenoord =	[2.4, 1.1, 2.2, 0.8]
PSV = [2.1, 0.7, 1.8, 1.3]
FCUtrecht = [1.9, 1.2, 3, 2.4]
WillemII = [1.4, 1.7, 1, 1.5]
teams = ["Ajax", "Feyenoord", "PSV", "FCUtrecht", "WillemII"]
averScoreDF = pd.DataFrame([Ajax, Feyenoord, PSV, FCUtrecht, WillemII])
averScoreDF = averScoreDF.set_index(pd.Index(teams))
averScoreDF.columns = ["HS", "HC", "AS", "AC"]


applyPoisson = lambda score, averScore: (averScore**score) * (math.e**-averScore) / math.factorial(score)
getDistribution = lambda averScore: [applyPoisson(i,averScore) for i in range(5)]

def listOfChoises(dis):
    choises = []
    for i in range(len(dis)):
        choises += [i] * round(dis[i]*100)
    return choises 

def getScore(averScore):
    distribution = getDistribution(averScore)
    choises = listOfChoises(distribution)
    score = choises[random.randint(0,len(choises)-1)]
    return score

def makeSchedule(teams):
    ammountTeams = len(teams)
    schedule = pd.DataFrame(np.zeros((ammountTeams, ammountTeams)))
    schedule.columns = teams
    schedule.index = teams
    return schedule

def playSchedule(schedule, averScoreDF):
    for column in schedule:
        for index, row in schedule.iterrows():
            if index == column:
                schedule[column][index] = None
            else:
                scoreChanseHome = (averScoreDF["HS"][index] + averScoreDF["AC"][column]) /2
                scoreChanseAway = (averScoreDF["AS"][column] + averScoreDF["HC"][index]) /2
                gameResult = "{}:{}".format(getScore(scoreChanseHome), getScore(scoreChanseAway))
                schedule[column][index] = gameResult
    return schedule

print(playSchedule(makeSchedule(teams), averScoreDF))

results = [getScore(0.824) for i in range(10000)]
plt.subplot(1, 2, 1)
plt.hist(results, weights=np.ones(len(results)) / len(results))
plt.gca().yaxis.set_major_formatter(PercentFormatter(1))
plt.subplot(1, 2, 2)
dis = getDistribution(0.824)
forPlot = {dis.index(i):i for i in dis}
plt.bar(range(5), getDistribution(0.824))
plt.show()

