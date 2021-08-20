from Posiciones import Posiciones

class ListaSimplePos():
    def __init__(self):
        self.inicio = None #Nodo inicial de la lista
        self.fin = None #Nodo final de la lista
        self.size = 0 #Cantidad de nodos

    def crearPosiciones(self, posx, posy, combustible):
        nuevo = Posiciones(posx, posy, combustible) #Agregando data al nodo
        self.size += 1 #El nodo se llena y aumenta el tamaño
        if self.inicio is None: #Verifica si el nodo tiene asignado un nodo inicial
            self.inicio = nuevo
        else: #Sino ya tiene asignado un nodo inicial llena otro nodo que no este en uso
            tmp = self.inicio
            while tmp.siguiente is not None:
                tmp = tmp.siguiente
            tmp.siguiente = nuevo
            self.fin = tmp.siguiente

    def mostrarPosiciones(self):
        tmp = self.inicio
        while tmp is not None:
            print('x =', tmp.posx, 'y ='+tmp.posy,'Combustible ='+tmp.combustible)
            tmp = tmp.siguiente

    def mostrarCombu(self):
        tmp = self.inicio
        while tmp is not None:
            return tmp