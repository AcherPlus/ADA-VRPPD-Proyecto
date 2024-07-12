from . import util

class Solution:

    def __init__(self):
        self.drivers = []
        self.loadByID = {}
        self.depot = util.Point(-12.056, -77.084)
        self.max_distance = 30

    def loadProblem(self, file_path):
        loads = util.loadProblemFromFile(file_path)
        for load in loads:
            self.loadByID[int(load.id)] = load

    def computeSavings(self):
        savings = []
        for i in self.loadByID:
            for j in self.loadByID:
                if i != j:
                    load1 = self.loadByID[i]
                    load2 = self.loadByID[j]
                    key = (i, j)
                    saving = (key, util.distanceBetweenPoints(load1.dropoff, self.depot)
                                    + util.distanceBetweenPoints(self.depot, load2.pickup)
                                    - util.distanceBetweenPoints(load1.dropoff, load2.pickup))
                    savings.append(saving)
        savings = sorted(savings, key=lambda x: x[1], reverse=True)
        #print(savings)
        return savings

    def computeDistance(self, nodes):
        if not nodes:
            return 0.0
        distance = 0.0
        for i in range(len(nodes)):
            distance += nodes[i].delivery_distance
            if i != (len(nodes) - 1):
                distance += util.distanceBetweenPoints(nodes[i].dropoff, nodes[i + 1].pickup)
        distance += util.distanceBetweenPoints(self.depot, nodes[0].pickup)
        distance += util.distanceBetweenPoints(nodes[-1].dropoff, self.depot)
        return distance

    def print_solution(self):
        for i, driver in enumerate(self.drivers):
            print(f"+ Ruta {i + 1}:")
            for load in driver.route:
                print(f"\t- Pedido {load.id}:")
                print(f"\t\t* Punto de Recojo: ({load.pickup.x}, {load.pickup.y})")
                print(f"\t\t* Punto de Entrega: ({load.dropoff.x}, {load.dropoff.y})")

    def solve(self):
        savings = self.computeSavings()
        for link, _ in savings:
            load1 = self.loadByID[link[0]]
            load2 = self.loadByID[link[1]]
            if not load1.assigned and not load2.assigned:
                cost = self.computeDistance([load1, load2])
                if cost <= self.max_distance:
                    driver = util.Driver()
                    driver.route = [load1, load2]
                    self.drivers.append(driver)
                    load1.assigned = driver
                    load2.assigned = driver
            elif load1.assigned and not load2.assigned:
                driver = load1.assigned
                i = driver.route.index(load1)
                if i == len(driver.route) - 1:
                    cost = self.computeDistance(driver.route + [load2])
                    if cost <= self.max_distance:
                        driver.route.append(load2)
                        load2.assigned = driver
            elif not load1.assigned and load2.assigned:
                driver = load2.assigned
                i = driver.route.index(load2)
                if i == 0:
                    cost = self.computeDistance([load1] + driver.route)
                    if cost <= self.max_distance:
                        driver.route = [load1] + driver.route
                        load1.assigned = driver
            else:
                driver1 = load1.assigned
                i1 = driver1.route.index(load1)
                driver2 = load2.assigned
                i2 = driver2.route.index(load2)
                if (i1 == len(driver1.route) - 1) and (i2 == 0) and (driver1 != driver2):
                    cost = self.computeDistance(driver1.route + driver2.route)
                    if cost <= self.max_distance:
                        driver1.route = driver1.route + driver2.route
                        for load in driver2.route:
                            load.assigned = driver1
                        self.drivers.remove(driver2)
        for load in self.loadByID.values():
            if not load.assigned:
                driver = util.Driver(0, [])
                driver.route.append(load)
                self.drivers.append(driver)
                load.assigned = driver

def solve_problem(file_path):
    solution = Solution()
    solution.loadProblem(file_path)
    solution.solve()
    solution.print_solution()
