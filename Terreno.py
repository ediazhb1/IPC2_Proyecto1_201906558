from ListaSimplePos import ListaSimplePos

class Terreno:#Clase Nodo
    def __init__(self,nombre,posinicial,posfinal):
        self.nombre = nombre #Nombre del terreno
        self.posinicial = posinicial #Pos. Inicial del r2e2
        self.posfinal = posfinal #Pos. Final del r2e2
        self.lista_posiciones = ListaSimplePos() #OTRO TDA XD
        self.siguiente = None #Apuntador