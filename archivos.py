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

            ListaTerrenos.crearTerreno(elemento.attrib['nombre'],itemsxi.text,itemsyi.text,itemsxf.text,itemsyf.text) 
            for combu in elemento.iter("posicion"):
                conexion = ListaTerrenos.buscarTerreno(elemento.attrib['nombre'])
                conexion.lista_posiciones.crearPosiciones(combu.attrib['x'],combu.attrib['y'],combu.text)  
                print("x =",combu.attrib['x'],"y =",combu.attrib['y'],"Combustible =",combu.text)
                            
            print("-------------------")
        

    def TerrenosEnLista(self):
        ListaTerrenos.mostrarTerreno()

    def GraficarReporte(self,SeleTerreno):
        try:
            x = ListaTerrenos.buscarTerreno(SeleTerreno)
            inicios = x.lista_posiciones.inicio
            fines = x.lista_posiciones.fin
            
            print("*Graficando el Terreno:",x.nombre+"...")
            print("Escribiendo el archivo .dot...")
            
            archivos = open(SeleTerreno+".dot","w")
            archivos.write("digraph G{\r\n" + 
            "label=<\r\n" + 
            "<TABLE border=\"5\" cellspacing=\"5\" cellpadding=\"15\" style=\"rounded\">\r\n")

            while inicios is not None:
                if int(inicios.posy) == 1:
                    archivos.write("<TR><TD border=\"1\">"+inicios.combustible+"</TD>\r\n")

                if int(inicios.posy) != 1:
                    archivos.write("<TD border=\"1\">"+inicios.combustible+"</TD>\r\n")

                if inicios.posy == fines.posy:
                    archivos.write("</TR>\r\n")
                inicios = inicios.siguiente

            archivos.write("</TABLE>>;\r\n" + 
            "}")
            archivos.close()

            print("Renderizando dot a png...")
            graphviz.render('dot', 'png',SeleTerreno+'.dot')
            print("Exito! Busque el gráfico con el nombre",SeleTerreno+'.dot')
        except:
            print("Error! ¿Ingreso correctamente el nombre? ¿Cargó el archivo?")

    def algoritmoRuta(self, SeleTerreno1):
        inifin = ListaTerrenos.buscarTerreno(SeleTerreno1)
        inifin.lista_posiciones.PosicionComienzo(inifin.xo,inifin.yo,inifin.xf,inifin.yf)


        