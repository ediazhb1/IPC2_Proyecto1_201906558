from Terreno import Terreno

class ListaSimple():
    def __init__(self):
        self.inicio = None #Nodo inicial de la lista
        self.fin = None #Nodo final de la lista
        self.size = 0 #Cantidad de nodos

    def crearTerreno(self, nombre, posinicial, posfinal):
        nuevo = Terreno(nombre, posinicial, posfinal) #Agregando data al nodo
        self.size += 1 #El nodo se llena y aumenta el tamaño
        if self.inicio is None: #Verifica si el nodo tiene asignado un nodo inicial
            self.inicio = nuevo
        else: #Sino ya tiene asignado un nodo inicial llena otro nodo que no este en uso
            tmp = self.inicio
            while tmp.siguiente is not None:
                tmp = tmp.siguiente
            tmp.siguiente = nuevo

    def mostrarTerreno(self):
        tmp = self.inicio
        while tmp is not None:
            print('Terreno:', tmp.nombre, '| Posición Inicial: ('+tmp.posinicial+")",'| Posición Final: ('+tmp.posfinal+")")
            tmp = tmp.siguiente
