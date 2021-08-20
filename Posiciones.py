class Posiciones:#Clase Nodo
    def __init__(self,posx,posy,combustible):
        self.posx = posx #Nombre del terreno
        self.posy = posy #Pos. Inicial del r2e2
        self.combustible = combustible #Pos. Final del r2e2
        self.siguiente = None #Apuntador