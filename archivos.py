import xml.etree.ElementTree as ET
from ListaSimple import ListaSimple
from xml.dom import minidom
ListaTerrenos = ListaSimple()

class archivos():
    def __init__(self):
        self.ruta = ""
        self.posiniciales = ""
        self.posfinales = ""

    def rutaxml(self,rxml):
        
        mydoc = minidom.parse(rxml)
        
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
        
        print("-------------------")
    
    def TerrenosEnLista(self):
        ListaTerrenos.mostrarTerreno()
