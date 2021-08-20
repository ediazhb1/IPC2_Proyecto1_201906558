import xml.etree.ElementTree as ET
from ListaSimple import ListaSimple
import graphviz

ListaTerrenos = ListaSimple()

class archivos():
    def __init__(self):
        pass

    def rutaxml(self,rxml):
        tree = ET.parse(rxml)
        root = tree.getroot()
        for elemento in root:
            print('El terreno',elemento.attrib['nombre'],'ha sido insertado.') #Nombre del terreno
            for posini in elemento.iter("posicioninicio"):
                for itemsxi in posini.iter("x"):
                    print("Posición xi del r2e2:",itemsxi.text)
                for itemsyi in posini.iter("y"):
                    print("Posición yi del r2e2:",itemsyi.text)
            for posini in elemento.iter("posicionfin"):
                for itemsxf in posini.iter("x"):
                    print("Posición xf del r2e2:",itemsxf.text)
                for itemsyf in posini.iter("y"):
                    print("Posición yf del r2e2:",itemsyf.text)

            ListaTerrenos.crearTerreno(elemento.attrib['nombre'],itemsxi.text+","+itemsyi.text,itemsxf.text+","+itemsyf.text) 
            for combu in elemento.iter("posicion"):
                conexion = ListaTerrenos.buscarTerreno(elemento.attrib['nombre'])
                conexion.lista_posiciones.crearPosiciones(combu.attrib['x'],combu.attrib['y'],combu.text)  
                print("x =",combu.attrib['x'],"y =",combu.attrib['y'],"Combustible =",combu.text)
                            
            print("-------------------")
        

    def TerrenosEnLista(self):
        ListaTerrenos.mostrarTerreno()

    def PosicionesEnLista(self):     
        prueba = ListaTerrenos.buscarTerreno("terreno1")
        a = prueba.lista_posiciones.inicio
        b = prueba.lista_posiciones.fin

        while a is not None:
            #print(a.combustible)
            print(a.posy,b.posy)
            a = a.siguiente

    def GraficarReporte(self,SeleTerreno):
        try:
            x = ListaTerrenos.buscarTerreno(SeleTerreno)
            print("*Graficando el Terreno:",x.nombre+"...")
            print("Escribiendo el archivo .dot...")
            
            archivos = open(SeleTerreno+".dot","w")
            archivos.write("digraph G{\r\n" + 
            "label=<\r\n" + 
            "<TABLE border=\"5\" cellspacing=\"10\" cellpadding=\"10\" style=\"rounded\">\r\n" + 
            "<TR><TD border=\"1\">00</TD>\r\n" + 
            "<TD border=\"1\">01</TD>\r\n" + 
            "<TD border=\"1\">02</TD>\r\n" + 
            "<TD border=\"1\">03</TD>\r\n" + 
            "</TR>\r\n" + 
            "<TR><TD border=\"1\">10</TD>\r\n" + 
            "<TD border=\"1\">11</TD>\r\n" + 
            "<TD border=\"1\">12</TD>\r\n" + 
            "<TD border=\"1\">13</TD>\r\n" + 
            "</TR>\r\n" +    
            "</TABLE>>;\r\n" + 
            "}")
            archivos.close()

            print("Renderizando dot a png")
            graphviz.render('dot', 'png',SeleTerreno+'.dot')
            print("Exito! Busque el gráfico con el nombre",SeleTerreno+'.dot')
        except:
            print("Error! ¿Ingreso correctamente el nombre? ¿Cargó el archivo?")
