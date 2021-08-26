from ListaSimplePos import ListaSimplePos

class Terreno:#Clase Nodo
    def __init__(self,nombre,xo,yo,xf,yf):
        self.nombre = nombre #Nombre del terreno
        self.xo = xo #Pos. Inicial del r2e2
        self.yo = yo #Pos. Inicial del r2e2
        self.xf = xf #Pos. Final del r2e2
        self.yf = yf #Pos. Final del r2e2
        self.lista_posiciones = ListaSimplePos()
        self.siguiente = None #Apuntador
        