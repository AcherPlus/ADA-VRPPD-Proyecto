import math
import io
from geopy.distance import distance

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Driver:
    def __init__(self, distance=0.0, route=[]):
        self.distanceTravelled = distance
        self.route = route

class Load:
    def __init__(self, id, pickup, dropoff):
        self.id = id
        self.pickup = pickup
        self.dropoff = dropoff
        self.assigned = None
        self.delivery_distance = distanceBetweenPoints(pickup, dropoff)
        
def distanceBetweenPoints(p1, p2):
    # Define two points (latitude, longitude)
    point1 = (p1.x, p1.y)  # Example: pickup point
    point2 = (p2.x, p2.y)  # Example: dropoff point

    # Calculate the distance between the two points
    dist = distance(point1, point2).km  # The distance in kilometers

    #print(f"The distance between the two points is {dist} kilometers.")
    return dist

    #xDiff = p1.x - p2.x
    #yDiff = p1.y - p2.y
    #return math.sqrt(xDiff*xDiff + yDiff*yDiff)

def loadProblemFromFile(filePath):
    f = open(filePath, "r")
    problemStr = f.read()
    f.close()
    return loadProblemFromProblemStr(problemStr)

def getPointFromPointStr(pointStr):
    pointStr = pointStr.replace("(","").replace(")","")
    splits = pointStr.split(",")
    return Point(float(splits[0]), float(splits[1]))

def loadProblemFromProblemStr(problemStr):
    loads = []
    buf = io.StringIO(problemStr)
    gotHeader = False
    while True:
        line = buf.readline()
        if not gotHeader:
            gotHeader = True
            continue
        if len(line) == 0:
            break
        line = line.replace("\n", "")
        splits = line.split()
        id = splits[0]
        pickup = getPointFromPointStr(splits[1])
        dropoff = getPointFromPointStr(splits[2])
        loads.append(Load(id, pickup, dropoff))
    return loads