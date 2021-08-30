class nsalida:#Clase Nodo
    def __init__(self,combustible,actux,actuy,tamañoTerreno):
        self.actux = actux #Pos. Inicial del r2e2
        self.actuy = actuy
        self.tamañoTerreno = tamañoTerreno
        self.combustible = combustible 
        self.siguiente = None #Apuntador