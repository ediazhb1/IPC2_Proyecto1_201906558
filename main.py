from archivos import archivos
from ListaSimplePos import ListaSimplePos
analisis = archivos()
positions = ListaSimplePos()

def imprimir():
    print("")
    print("\033[1;36m"+"MENÚ PRINCIPAL:")
    print("\033[0;37m"+"1. Cargar archivo")
    print("2. Procesar terreno")
    print("3. Escribir archivo de salida")
    print("4. Mostrar datos del estudiante")
    print("5. Generar gráfica")
    print("6. Salir")

def menu():
    while True:
        imprimir()
        try:
            entrada_usuario = int(input("> Seleccione una opcion (número): "))
            if entrada_usuario in range(7):
                if entrada_usuario == 6:
                    print("Adios! Vuelva pronto")
                    break

                if entrada_usuario == 0:
                    print("Esta opción no tiene asignada una acción")

                if entrada_usuario == 1:
                    print("*Opción Cargar archivo")
                    pathxml = str(input("> Ingrese la ruta del archivo (xml): "))
                    file = './' + pathxml
                    analisis.rutaxml(file)

                if entrada_usuario == 2:
                    print("*Opción Procesar terreno")
                    analisis.TerrenosEnLista()
                    analisis.PosicionesEnLista()
                    
                if entrada_usuario == 3:
                    print("*Opción Archivo de salida")

                if entrada_usuario == 4:
                    print("*Opción Datos del estudiante")
                    print("Eddy Fernando Díaz Galindo")
                    print("201906558")
                    print("Introducción a la programación y computación 2")
                    print("Ingenieria en Ciencias y Sistemas")
                    print("4to Semestre")

                if entrada_usuario == 5:
                    print("*Generar gráfica")
                    analisis.TerrenosEnLista()
                    SeleTerreno = str(input("> Ingrese el nombre del terreno a graficar: "))       
                    analisis.GraficarReporte(SeleTerreno)                       

            else:
                print('Error, solo de aceptan numeros del 1 al 6')

        except ValueError:
            print("Error, ingrese solamente numeros")

if __name__ == '__main__':
    menu()