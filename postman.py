import random
import math
import turtle

# Constans
NumberOfPoints = 50
NumberOfGenerations = 100
Population = 10000

# Returns 1^2 + 2^2 + 3^2 + ... n^2.
def sumOfSquares(n):
    return (n * (n + 1) * (2 * n + 1)) // 6

# Returns random member of population where
# fitter have better chances of being chose.
def randOfPopulation():
    rand = random.randint(1, sumOfSquares(Population))
    low = 1
    high = Population

    if rand == sumOfSquares(Population):
        return 0
    
    while True:
        mid = math.floor((low + high) / 2)
        if sumOfSquares(mid) == rand:
            return Population - mid
        if sumOfSquares(mid) > rand:
            high = mid
        else:
            if sumOfSquares(mid + 1) > rand:
                return Population - (mid + 1)
            else:
                low = mid

def drawRoute(tour, bool):
    if bool == True:
        for i in range(NumberOfPoints):
            pen.undo()
    pen.up()
    pen.goto(pointsList[tour.points[0]])
    pen.down()
    for i in range(NumberOfPoints):
        pen.goto(pointsList[tour.points[(i + 1) % NumberOfPoints]])

#TODO
def greedyRoute(points):
    numOfPoints = points.length()
    unvisitedPoints = numOfPoints * [0]
    route = numOfPoints * [0]
    unvisitedPoints[0] = 1
    #for i in range(0, numOfPoints - 1):
        # TODO
    return 0


class Tour:
    def __init__(self, arg=None):

        if arg is None: # Totally random tour.
            self.points = [0] * NumberOfPoints
            for i in range(NumberOfPoints):
                valueNotSet = True
                while valueNotSet:
                    potentialNewVertex = True
                    newValue = random.randint(0, NumberOfPoints - 1)
                    for j in range(i):
                        if newValue == self.points[j]:
                            potentialNewVertex = False
                
                    if potentialNewVertex:
                        self.points[i] = newValue
                        valueNotSet = False
            self.length = 0
            for i in range(NumberOfPoints):
                self.length += pointsDistances[self.points[i]][self.points[(i + 1) % NumberOfPoints]]
            self.length = round(self.length, 2)
        
        else: # Tour based on other tour (randomly changed some vertexes).
            self.points = [0] * NumberOfPoints
            for i in range(NumberOfPoints):
                self.points[i] = arg.points[i]

            numOfChanges = random.randint(0, 3)
            for i in range(numOfChanges):
                pointChanged = random.randint(0, NumberOfPoints - 1)
                self.points[pointChanged], self.points[(pointChanged + 1) % NumberOfPoints] = self.points[(pointChanged + 1) % NumberOfPoints], self.points[pointChanged]
            self.length = 0
            for i in range(NumberOfPoints):
                self.length += pointsDistances[self.points[i]][self.points[(i + 1) % NumberOfPoints]]
            self.length = round(self.length, 2)
        
    
    def __str__(self):
        return str(self.points) + " " + str(self.length)


# Initialing set of points.
pointsList = []
for i in range(NumberOfPoints):
    pointsList.append((round(random.random() * 600 - 300, 2), round(random.random() * 600 - 300, 2)))
# N = 4 # Number of points on side of a square. (put N squared for NumberOfPoints)
# for i in range(NumberOfPoints):
#     pointsList.append((math.floor(i / N) * 600 / N - 300, (i % N) * 600 / N - 300))

# Calculating distances.
pointsDistances = [[0 for _ in range(NumberOfPoints)] for _ in range(NumberOfPoints)]
for i in range(NumberOfPoints):
    for j in range(NumberOfPoints):
        pointsDistances[i][j] = round(math.sqrt(math.pow(pointsList[i][0] - pointsList[j][0], 2) + math.pow(pointsList[i][1] - pointsList[j][1], 2)), 2)

# Turtle making points.
pen = turtle.Turtle()
pen.speed(0)
pen.up()
for i in range(NumberOfPoints):
    pen.goto(pointsList[i][0], pointsList[i][1])
    pen.dot()


# Initializing first generation.
print("Generation 1")
populationArray = []
for i in range(Population):
    populationArray.append(Tour())
populationArray = sorted(populationArray, key=lambda x: x.length)

bestTour = populationArray[0]
print(populationArray[0])
drawRoute(populationArray[0], False)

for i in range(NumberOfGenerations - 1):
    print("Generation "+ str(i + 2))
    newPopulationArray = []
    for i in range(Population):
        if i < Population * 4/5: # Tours based of current population.
            newPopulationArray.append(Tour(populationArray[randOfPopulation()]))
        else: # Totally random tours.
            newPopulationArray.append(Tour())
    
    populationArray = sorted(newPopulationArray, key=lambda x : x.length)
    if(populationArray[0].length < bestTour.length):
        print("New best tour " + str(populationArray[0]))
        bestTour = populationArray[0]
        #drawRoute(bestTour, True)
    else:
        print("No new best tour in this generation")

drawRoute(bestTour, True)
print("Best tour:" + str(bestTour))

pen.hideturtle()

turtle.done()
