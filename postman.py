import random
import math

numberOfPoints = input()
numberOfPoints = int(numberOfPoints)

pointsList = []

for i in range(numberOfPoints):
    pointsList.append((random.random() * 100, random.random() * 100))

for i in range(numberOfPoints):
    print(pointsList[i])

pointsDistances = [[0 for _ in range(numberOfPoints)] for _ in range(numberOfPoints)]

for i in range(numberOfPoints):
    for j in range(numberOfPoints):
        pointsDistances[i][j] = math.sqrt(math.pow(pointsList[i][0] - pointsList[j][0], 2) + math.pow(pointsList[i][1] - pointsList[j][1], 2))

print(pointsDistances[7][7])