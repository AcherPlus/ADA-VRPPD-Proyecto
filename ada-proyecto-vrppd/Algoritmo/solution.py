import sys
import util

class Solution:

    def __init__(self):
        self.drivers = []
        self.loadByID ={}
        self.depot = util.Point(0,0)
        self.max_distance = 12*60
        # self.max_distance = 8*60

    def loadProblem(self, file_path):
        # Cargar los datos desde el archivo especificado
        loads = util.loadProblemFromFile(file_path)
        for load in loads:
            self.loadByID[int(load.id)] = load

    def computeSavings(self):
        # Calcular ahorros potenciales según el algoritmo de Clark-Wright
        savings = []
        for i in self.loadByID:
            for j in self.loadByID:
                if i != j:      
                    load1 = self.loadByID[i]
                    load2 = self.loadByID[j]      
                    key = (i, j)
                    # Fórmula: 
                    # ahorros = D(i.entrega, 0) + D(0, j.recogida) - D(i.entrega, j.recogida)
                    saving = (key, util.distanceBetweenPoints(load1.dropoff, self.depot) \
                                    + util.distanceBetweenPoints(self.depot, load2.pickup) \
                                    - util.distanceBetweenPoints(load1.dropoff, load2.pickup))
                    savings.append(saving)

        savings = sorted(savings, key = lambda x: x[1], reverse=True)

        return savings
    
    def computeDistance(self, nodes):
        # Calcular la distancia total de la ruta para los nodos dados

        if not nodes:
            return 0.0
        
        distance = 0.0
        for i in range(len(nodes)):
            distance += nodes[i].delivery_distance
            if i != (len(nodes) - 1):
                distance += util.distanceBetweenPoints(nodes[i].dropoff, nodes[i+1].pickup)

        distance += util.distanceBetweenPoints(self.depot, nodes[0].pickup)
        distance += util.distanceBetweenPoints(nodes[-1].dropoff, self.depot)
        
        return distance

    def print_solution(self):
        # Imprimir la solución final
        print()
        for i, driver in enumerate(self.drivers):
            print(f"+ Ruta {i + 1}:")
            for load in driver.route:
                print(f"\t- Pedido {load.id}:")
                print(f"\t\t* Punto de Recojo: ({load.pickup.x}, {load.pickup.y})")
                print(f"\t\t* Punto de Entrega: ({load.dropoff.x}, {load.dropoff.y})")
                print()

    def solve(self):
        '''
        Implementación del algoritmo de ahorro de Clark-Wright
        '''
        
        # Calcular los ahorros para cada enlace
        savings = self.computeSavings()

        for link, _ in savings:

            load1 = self.loadByID[link[0]]
            load2 = self.loadByID[link[1]]

            # Condición a. O bien, ni i ni j han sido asignados a una ruta aún, 
            # en cuyo caso se inicia una nueva ruta que incluye ambos i y j.
            if not load1.assigned and not load2.assigned:

                # Verificar restricciones
                cost = self.computeDistance([load1, load2])
                if cost <= self.max_distance:
                    driver = util.Driver()
                    driver.route = [load1, load2]
                    self.drivers.append(driver)
                    load1.assigned = driver
                    load2.assigned = driver

            # Condición b. O, exactamente uno de los dos nodos (i o j) ya se ha incluido 
            # en una ruta existente y ese punto no es interior a esa ruta.
            elif load1.assigned and not load2.assigned:

                driver = load1.assigned
                i = driver.route.index(load1)
                # si el nodo es el último nodo de la ruta
                if i == len(driver.route) - 1:
                    # Verificar restricciones
                    cost = self.computeDistance(driver.route + [load2])
                    if cost <= self.max_distance:
                        driver.route.append(load2)
                        load2.assigned = driver

            elif not load1.assigned and load2.assigned:

                driver = load2.assigned
                i = driver.route.index(load2)
                # si el nodo es el primer nodo de la ruta
                if i == 0:
                    # Verificar restricciones
                    cost = self.computeDistance([load1] + driver.route)
                    if cost <= self.max_distance:
                        driver.route = [load1] + driver.route
                        load1.assigned = driver

            # Condición c. O, tanto i como j ya se han incluido en dos rutas existentes diferentes 
            # y ninguno de los puntos es interior a su ruta, en cuyo caso se fusionan las dos rutas.
            else:

                driver1 = load1.assigned
                i1 = driver1.route.index(load1)

                driver2 = load2.assigned
                i2 = driver2.route.index(load2)

                # si el nodo1 es el último nodo de su ruta y el nodo 2 es el primer nodo de su ruta y las rutas son diferentes
                if (i1 == len(driver1.route) - 1) and (i2 == 0) and (driver1 != driver2):
                    cost = self.computeDistance(driver1.route + driver2.route)
                    if cost <= self.max_distance:
                        driver1.route = driver1.route + driver2.route
                        for load in driver2.route:
                            load.assigned = driver1
                        
                        self.drivers.remove(driver2)

        # Asignar todos los conductores no asignados a rutas individuales      
        for load in self.loadByID.values():
            if not load.assigned:
                driver = util.Driver(0, [])
                driver.route.append(load)
                self.drivers.append(driver)
                load.assigned = driver

                
if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Uso: python solution.py <ruta_del_archivo>")
        sys.exit(1)
    file_path = sys.argv[1]
    solution = Solution()
    solution.loadProblem(file_path)
    solution.solve()
    solution.print_solution()
