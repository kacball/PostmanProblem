import random
import math
import turtle

class Tour:
    def __init__(self):
        self.points = [0] * numberOfPoints
        for i in range(numberOfPoints):
            valueNotSet = True
            while valueNotSet:
                goodNumber = True
                newValue = random.randint(0, numberOfPoints - 1)
                for j in range(i):
                    if newValue == self.points[j]:
                        goodNumber = False
                
                if goodNumber:
                    self.points[i] = newValue
                    valueNotSet = False
        self.length = 0
        for i in range(numberOfPoints):
            self.length += pointsDistances[self.points[i]][self.points[(i + 1) % numberOfPoints]]
        
        
    
    def __str__(self):
        return str(self.points) + " " + str(self.length)


numberOfPoints = input()
numberOfPoints = int(numberOfPoints)

pointsList = []

for i in range(numberOfPoints):
    pointsList.append((round(random.random() * 600 - 300, 2), round(random.random() * 600 - 300, 2)))


pointsDistances = [[0 for _ in range(numberOfPoints)] for _ in range(numberOfPoints)]

for i in range(numberOfPoints):
    for j in range(numberOfPoints):
        pointsDistances[i][j] = round(math.sqrt(math.pow(pointsList[i][0] - pointsList[j][0], 2) + math.pow(pointsList[i][1] - pointsList[j][1], 2)), 2)

print(pointsDistances)

road1 = Tour()
print(road1)

pen = turtle.Turtle()
pen.up()

for i in range(numberOfPoints):
    pen.goto(pointsList[i][0], pointsList[i][1])
    pen.dot()


pen.hideturtle()

turtle.done()