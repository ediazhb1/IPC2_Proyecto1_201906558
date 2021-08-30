from nsalida import nsalida

class listansalida():
    def __init__(self):
        self.inicio = None #Nodo inicial de la lista
        self.fin = None #Nodo final de la lista
        self.size = 0 #Cantidad de nodos

    def crearSalida(self,combustible,actux,actuy,tamañoTerreno):
        nuevo = nsalida(combustible,actux,actuy,tamañoTerreno) #Agregando data al nodo
        self.size += 1 #El nodo se llena y aumenta el tamaño
        if self.inicio is None: #Verifica si el nodo tiene asignado un nodo inicial
            self.inicio = nuevo
        else: #Sino ya tiene asignado un nodo inicial llena otro nodo que no este en uso
            tmp = self.inicio
            while tmp.siguiente is not None:
                tmp = tmp.siguiente
            tmp.siguiente = nuevo
            self.fin = tmp.siguiente


    def mostrarCamino(self):
        sumacombus= 0
        tmp = self.inicio
        while tmp is not None:
            #print("Posición x: "+tmp.actux+"  Posición y: "+tmp.actuy+' Combustible: '+tmp.combustible)
            sumacombus += int(tmp.combustible)
            tmp = tmp.siguiente
        print("EL COMBUSTIBLE ES: "+ str(sumacombus))

    def escritura(self,Seleterreno1):
        sumacombu = 0
        tmp = self.inicio
        tmp2 = self.fin
        tmp3 = self.inicio
        print(str(Seleterreno1))

        while tmp3 is not None:
            sumacombu += int(tmp3.combustible)
            tmp3 = tmp3.siguiente

        archivos1 = open(str(Seleterreno1)+".xml","w")
        archivos1.write("<terreno nombre=\""+str(Seleterreno1)+"\">\r\n" + 
            "<posicioninicio>\r\n" + 
            "<x>"+ str(tmp.actux)+ "</x>\r\n"+
            "<y>"+ str(tmp.actuy)+ "</y>\r\n" + 
            "</posicioninicio>\r\n"+
            "<posicionfin>\r\n" + 
            "<x>"+ str(tmp2.actux)+ "</x>\r\n"+
            "<y>"+ str(tmp2.actuy)+ "</y>\r\n" + 
            "</posicionfin>\r\n"+
            "<combustible>"+ str(sumacombu)+ "</combustible>\r\n")

        while tmp is not None:
            archivos1.write("<posicion x=\""+str(tmp.actux)+"\" y=\""+str(tmp.actuy)+'\">'+str(tmp.combustible)+"</posicion>\r\n")
            tmp = tmp.siguiente
        
        archivos1.write("</terreno>")

        archivos1.close()