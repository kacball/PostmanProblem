import random
import math
import turtle

NumberOfPoints = 10
NumberOfGenerations = 100
Population = 100


class Tour:
    def __init__(self, arg=None):
        if arg is None:
            self.points = [0] * NumberOfPoints
            for i in range(NumberOfPoints):
                valueNotSet = True
                while valueNotSet:
                    goodNumber = True
                    newValue = random.randint(0, NumberOfPoints - 1)
                    for j in range(i):
                        if newValue == self.points[j]:
                            goodNumber = False
                
                    if goodNumber:
                        self.points[i] = newValue
                        valueNotSet = False
            self.length = 0
            for i in range(NumberOfPoints):
                self.length += pointsDistances[self.points[i]][self.points[(i + 1) % NumberOfPoints]]
            self.length = round(self.length, 2)
        else:
            self.points = [0] * NumberOfPoints
            for i in range(NumberOfPoints):
                self.points[i] = arg.points[i]

            numOfChanges = random.randint(0, 3)
            for i in range(numOfChanges):
                pointChanged = random.randint(0, NumberOfPoints - 1)
                self.points[pointChanged], self.points[pointChanged + 1] = self.points[pointChanged + 1], self.points[pointChanged]
            self.length = 0
            for i in range(NumberOfPoints):
                self.length += pointsDistances[self.points[i]][self.points[(i + 1) % NumberOfPoints]]
            self.length = round(self.length, 2)
        
    
    def __str__(self):
        return str(self.points) + " " + str(self.length)



pointsList = []

for i in range(NumberOfPoints):
    pointsList.append((round(random.random() * 600 - 300, 2), round(random.random() * 600 - 300, 2)))


pointsDistances = [[0 for _ in range(NumberOfPoints)] for _ in range(NumberOfPoints)]

for i in range(NumberOfPoints):
    for j in range(NumberOfPoints):
        pointsDistances[i][j] = round(math.sqrt(math.pow(pointsList[i][0] - pointsList[j][0], 2) + math.pow(pointsList[i][1] - pointsList[j][1], 2)), 2)


pen = turtle.Turtle()
pen.up()

for i in range(NumberOfPoints):
    pen.goto(pointsList[i][0], pointsList[i][1])
    pen.dot()

populationArray = []
for i in range(Population):
    populationArray.append(Tour())
for i in populationArray:
    print(i)
populationArray = sorted(populationArray, key=lambda x: x.length)
for i in populationArray:
    print(i)
#for i in range(NumberOfGenerations - 1):




pen.hideturtle()

turtle.done()