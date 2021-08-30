from Posiciones import Posiciones
from listansalida import listansalida

ListaSalida = listansalida()


class ListaSimplePos():
    def __init__(self):
        self.inicio = None #Nodo inicial de la lista
        self.fin = None #Nodo final de la lista
        self.posactual = None
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
    
    def ordencuatro(self,rightcombu,leftcombu,upcombu,downcombu):
        menor =""
        if rightcombu < leftcombu and rightcombu < downcombu and rightcombu < upcombu:
            menor = "rightcombu"                    
        elif leftcombu < rightcombu and leftcombu < upcombu and leftcombu < downcombu:                          
            menor = "leftcombu"    
        elif downcombu < rightcombu and downcombu < upcombu and downcombu < leftcombu:
            menor = "downcombu" 
        elif upcombu < rightcombu and upcombu < leftcombu and upcombu < downcombu:
            menor = "upcombu"
        elif rightcombu == leftcombu and upcombu < downcombu and upcombu < rightcombu:
            menor = "upcombu"
        elif rightcombu == leftcombu and downcombu < upcombu and downcombu < rightcombu:
            menor = "downcombu" 
        elif rightcombu == leftcombu and leftcombu < upcombu and leftcombu < downcombu:
            menor = "leftcombu"
        elif upcombu == downcombu and leftcombu < rightcombu and leftcombu < upcombu:
            menor = "leftcombu"
        elif upcombu == downcombu and rightcombu < leftcombu and rightcombu < upcombu:
            menor = "rightcombu"
        elif upcombu == downcombu and downcombu < leftcombu and downcombu < rightcombu:
            menor = "downcombu" 
        elif leftcombu == upcombu and rightcombu < downcombu and rightcombu < leftcombu:
            menor = "rightcombu"
        elif leftcombu == upcombu and downcombu < rightcombu and downcombu < leftcombu:
            menor = "downcombu" 
        elif leftcombu == upcombu and upcombu < rightcombu and upcombu < downcombu:
            menor = "upcombu"
        elif downcombu == leftcombu and upcombu < rightcombu and upcombu < downcombu:
            menor = "upcombu"
        elif downcombu == leftcombu and rightcombu < upcombu and rightcombu < downcombu:
            menor = "rightcombu"
        elif downcombu == leftcombu and  leftcombu < upcombu and leftcombu < rightcombu:
            menor = "leftcombu"
        elif downcombu == rightcombu and rightcombu < upcombu and rightcombu < leftcombu :
            menor = "downcombu"
        #-----------------------------------------------------------------------------
        elif upcombu == leftcombu == downcombu and downcombu < leftcombu:
            menor = "downcombu" 
        elif upcombu == leftcombu == rightcombu and rightcombu < downcombu:
            menor = "rightcombu"
        elif upcombu == rightcombu == downcombu and downcombu < rightcombu:
            menor = "downcombu" 
        elif leftcombu == rightcombu == downcombu and downcombu < upcombu:
            menor = "downcombu"  
        else:
            pass

        return menor
        
    def PosicionComienzo(self,xo,yo,xf,yf):
        ListaSalida.inicio = None
        tmp = self.inicio
        tmp2 = self.fin

        downcombu =0
        upcombu = 0
        leftcombu = 0
        rightcombu = 0
        menor =0
        movsx = 0
        movsy = 0

        downcombusig =0
        upcombusig = 0
        leftcombusig = 0
        rightcombusig = 0

        restax = int(xf) - int(xo)
        restay = int(yf) - int(yo)

        tamañoTerreno = int(tmp2.posx)*int(tmp2.posy)
        
        while tmp is not None:
            
            if int(tmp.posx) == int(xo) and int(tmp.posy) == int(yo):
                self.posactual = tmp
                act = self.posactual
                ListaSalida.crearSalida(act.combustible,act.posx,act.posy,tamañoTerreno)
                a = 0
                while True and a != 90:
                    a +=1                       
                    if int(act.posx) < int(tmp2.posx) and int(act.posy) < int(tmp2.posy) and int(act.posx) > 1 and int(act.posy) > 1:   
                        tmp3 = self.inicio
                        #Buscando combu de los cuatro lados
                        while tmp3 is not None:

                            if int(tmp3.posx) == int(act.posx)-1 and int(tmp3.posy) == int(act.posy):
                                upcombu = int(tmp3.combustible)

                            if int(tmp3.posy) == int(act.posy)-1 and int(tmp3.posx) == int(act.posx):
                                leftcombu = int(tmp3.combustible)

                            if int(tmp3.posy) == int(act.posy)+1 and int(tmp3.posx) == int(act.posx):
                                rightcombu = int(tmp3.combustible)

                            if int(tmp3.posx) == int(act.posx)+1 and int(tmp3.posy) == int(act.posy):
                                downcombu = int(tmp3.combustible)  
                            
                            tmp3 = tmp3.siguiente

                        menortxt = self.ordencuatro(rightcombu,leftcombu,upcombu,downcombu)
                        if menortxt == "downcombu":
                            menor = int(downcombu)
                            movsx = int(act.posx)+1
                            movsy = int(act.posy)
                        elif menortxt == "rightcombu":
                            menor = int(rightcombu)
                            movsx = int(act.posx)
                            movsy = int(act.posy)+1
                        elif menortxt == "leftcombu":
                            menor = int(leftcombu)
                            movsx = int(act.posx)
                            movsy = int(act.posy)-1
                        elif menortxt == "upcombu":
                            menor = int(upcombu)
                            movsx = int(act.posx)-1
                            movsy = int(act.posy) 
                         
                        tmp4 = self.inicio
                        while tmp4 is not None:
                            if int(tmp4.combustible) == int(menor) and int(tmp4.posx) == int(movsx) and int(tmp4.posy) == int(movsy):
                                ListaSalida.crearSalida(tmp4.combustible,tmp4.posx,tmp4.posy,tamañoTerreno)
                                act.combustible = int(act.combustible)+1000
                                act = tmp4
                            
                            tmp4 = tmp4.siguiente
                        
                        if int(act.posx) == int(xf) and int(act.posy) == int(yf):
                            break

                    #Esquina inferior derecha 
                    elif (int(tmp2.posx) == int(act.posx)) and (int(tmp2.posy) == int(act.posy)):
                        tmp5 = self.inicio
                        while tmp5 is not None:

                            if int(tmp5.posx) == int(act.posx)-1 and int(tmp5.posy) == int(act.posy):
                                upcombu = int(tmp5.combustible)

                            if int(tmp5.posy) == int(act.posy)-1 and int(tmp5.posx) == int(act.posx):
                                leftcombu = int(tmp5.combustible)
                            
                            if int(tmp5.posx) == int(act.posx)-2 and int(tmp5.posy) == int(act.posy):
                                upcombusig = int(tmp5.combustible)

                            if int(tmp5.posy) == int(act.posy)-2 and int(tmp5.posx) == int(act.posx):
                                leftcombusig = int(tmp5.combustible)

                            tmp5 = tmp5.siguiente

                        sumarupid = 0
                        sumarleftid = 0
                        sumarupid = upcombusig + upcombu
                        sumarleftid = leftcombusig + leftcombu

                        if sumarupid < sumarleftid:
                            menor = int(upcombu)
                            movsx = int(act.posx)-1
                            movsy = act.posy
                        elif sumarleftid < sumarupid:
                            menor = int(leftcombu)
                            movsx = act.posx
                            movsy = int(act.posy)-1
                        else:
                            pass

                        tmp26 = self.inicio
                        while tmp26 is not None:
                            if int(tmp26.combustible) == int(menor) and int(tmp26.posx) == int(movsx) and int(tmp26.posy) == int(movsy):
                                ListaSalida.crearSalida(tmp26.combustible,tmp26.posx,tmp26.posy,tamañoTerreno)
                                act.combustible = int(act.combustible)+1000
                                self.posactual = tmp26
                                act = self.posactual
                            
                            tmp26 = tmp26.siguiente

                        if int(act.posx) == int(xf) and int(act.posy) == int(yf):
                            break
                    # Esquina Superior Izquierda       
                    elif (int(act.posx) == 1 and int(act.posy) == 1):
                        
                        tmp6 = self.inicio
                        while tmp6 is not None:
                            if int(tmp6.posy) == int(act.posy)+1 and int(tmp6.posx) == int(act.posx):
                                rightcombu = int(tmp6.combustible)

                            if int(tmp6.posx) == int(act.posx)+1 and int(tmp6.posy) == int(act.posy):
                                downcombu = int(tmp6.combustible)
                            
                            if int(tmp6.posy) == int(act.posy)+2 and int(tmp6.posx) == int(act.posx):
                                rightcombusig = int(tmp6.combustible)

                            if int(tmp6.posx) == int(act.posx)+2 and int(tmp6.posy) == int(act.posy):
                                downcombusig = int(tmp6.combustible)
                                
                            tmp6 = tmp6.siguiente

                        sumaright = 0
                        sumardown = 0
                        sumaright = rightcombusig + rightcombu
                        sumardown = downcombusig + downcombu
                        
                        if sumaright < sumardown:
                            menor = int(rightcombu)
                            movsx = int(act.posx)
                            movsy = int(act.posy)+1                            

                        elif sumardown < sumaright:
                            menor = int(downcombu)
                            movsx = int(act.posx)+1
                            movsy = int(act.posy)
                                
                        else:
                            print("SON IGUALES, SUPERIOR IZQUIERDA")

                        tmp7 = self.inicio
                        while tmp7 is not None:
                            if int(tmp7.combustible) == int(menor) and int(tmp7.posx) == int(movsx) and int(tmp7.posy) == int(movsy):
                                ListaSalida.crearSalida(tmp7.combustible,tmp7.posx,tmp7.posy,tamañoTerreno)
                                act.combustible = int(act.combustible)+1000
                                act = tmp7
                            
                            tmp7 = tmp7.siguiente

                        if int(act.posx) == int(xf) and int(act.posy) == int(yf):
                            break
                    #Esquina superior Derecha 
                    elif (int(act.posx) ==1) and (int(act.posy) == int(tmp2.posy)):
                        tmp9 = self.inicio
                        while tmp9 is not None:
                            if int(tmp9.posy) == int(act.posy)-1 and int(tmp9.posx) == int(act.posx):
                                leftcombu = int(tmp9.combustible)

                            if int(tmp9.posx) == int(act.posx)+1 and int(tmp9.posy) == int(act.posy):
                                downcombu = int(tmp9.combustible) 

                            if int(tmp9.posy) == int(act.posy)-2 and int(tmp9.posx) == int(act.posx):
                                leftcombusig = int(tmp9.combustible)

                            if int(tmp9.posx) == int(act.posx)+2 and int(tmp9.posy) == int(act.posy):
                                downcombusig = int(tmp9.combustible)  

                            tmp9 = tmp9.siguiente
                        
                        sumarleftsd = 0
                        sumardownsd = 0
                        sumarleftsd = leftcombusig + leftcombu
                        sumardownsd = downcombusig + downcombu


                        if sumarleftsd < sumardownsd:
                            menor = int(leftcombu)
                            movsx = act.posx
                            movsy = int(act.posy)-1
                        elif sumardownsd < sumarleftsd:
                            menor = int(downcombu)
                            movsx = int(act.posx)+1
                            movsy = act.posy   
                        else:
                            print("SON IGUALES")

                        tmp8 = self.inicio
                        while tmp8 is not None:
                            if int(tmp8.combustible) == int(menor) and int(tmp8.posx) == int(movsx) and int(tmp8.posy) == int(movsy):
                                ListaSalida.crearSalida(tmp8.combustible,tmp8.posx,tmp8.posy,tamañoTerreno)
                                act.combustible = int(act.combustible)+1000
                                act = tmp8
                            
                            tmp8 = tmp8.siguiente
                        
                        if int(act.posx) == int(xf) and int(act.posy) == int(yf):
                            break
                        
                    #Esquina Inferior Izquierda 
                    elif (int(act.posx) == int(tmp2.posx) and int(act.posy) == 1):
                        
                        tmp10 = self.inicio
                        while tmp10 is not None:
                            if int(tmp10.posy) == int(act.posy)+1 and int(tmp10.posx) == int(act.posx):
                                rightcombu = int(tmp10.combustible)

                            if int(tmp10.posx) == int(act.posx)-1 and int(tmp10.posy) == int(act.posy):
                                upcombu = int(tmp10.combustible)

                            if int(tmp10.posy) == int(act.posy)+2 and int(tmp10.posx) == int(act.posx):
                                rightcombusig = int(tmp10.combustible)

                            if int(tmp10.posx) == int(act.posx)-2 and int(tmp10.posy) == int(act.posy):
                                upcombusig = int(tmp10.combustible)

                            tmp10 = tmp10.siguiente


                        sumarrightii = 0
                        sumarupii = 0
                        sumarrightii = rightcombusig + rightcombu
                        sumarupii = upcombusig + upcombu

                        
                        if sumarrightii < sumarupii:
                            menor = int(rightcombu)
                            movsx = act.posx
                            movsy = int(act.posy)+1 
                        elif sumarupii < sumarrightii:
                            menor = int(upcombu)
                            movsx = int(act.posx)-1
                            movsy = act.posy  
                        else:
                            print("SON IGUALES")

                        tmp11 = self.inicio
                        while tmp11 is not None:
                            if int(tmp11.combustible) == int(menor) and int(tmp11.posx) == int(movsx) and int(tmp11.posy) == int(movsy):
                                ListaSalida.crearSalida(tmp11.combustible,tmp11.posx,tmp11.posy,tamañoTerreno)
                                act.combustible = int(act.combustible)+1000
                                act = tmp11
                            
                            tmp11 = tmp11.siguiente
                        
                        if int(act.posx) == int(xf) and int(act.posy) == int(yf):
                            break

                    #Bordes izquierdos
                    elif (int(act.posy)==1) and (int(act.posx) > 1) and (int(act.posx) < int(tmp2.posx)):
                        menor = 0
                        tmp12 = self.inicio
                        
                        while tmp12 is not None:

                            if int(tmp12.posx) == int(act.posx)-1 and int(tmp12.posy) == int(act.posy):
                                upcombu = int(tmp12.combustible)

                            if int(tmp12.posy) == int(act.posy)+1 and int(tmp12.posx) == int(act.posx):
                                rightcombu = int(tmp12.combustible)

                            if int(tmp12.posx) == int(act.posx)+1 and int(tmp12.posy) == int(act.posy):
                                downcombu = int(tmp12.combustible)  
                            
                            tmp12 = tmp12.siguiente

                        if upcombu < rightcombu and upcombu < downcombu:
                            menor = int(upcombu)
                            movsx = int(act.posx)-1
                            movsy = int(act.posy)  
                        elif rightcombu < upcombu and rightcombu < downcombu:
                            menor = int(rightcombu)
                            movsx = int(act.posx)
                            movsy = int(act.posy)+1
                        elif downcombu < upcombu and downcombu < rightcombu:
                            menor = int(downcombu)
                            movsx = int(act.posx)+1
                            movsy = int(act.posy)
                        elif rightcombu == downcombu and upcombu < downcombu:
                            menor = int(upcombu)
                            movsx = int(act.posx)-1
                            movsy = int(act.posy) 
                        elif upcombu == rightcombu and downcombu < rightcombu:
                            menor = int(downcombu)
                            movsx = int(act.posx)+1
                            movsy = int(act.posy)
                        elif upcombu == downcombu and rightcombu < upcombu:
                            menor = int(rightcombu)
                            movsx = int(act.posx)
                            movsy = int(act.posy)+1
                        elif upcombu == downcombu and downcombu < rightcombu:
                            if restay > 0:
                                menor = int(downcombu)
                                movsx = int(act.posx)+1
                                movsy = int(act.posy)
                            elif restay < 0:
                                menor = int(upcombu)
                                movsx = int(act.posx)-1
                                movsy = int(act.posy) 
                        else:
                            pass

                        tmp13 = self.inicio
                        while tmp13 is not None:
                            if int(tmp13.combustible) == int(menor) and int(tmp13.posx) == int(movsx) and int(tmp13.posy) == int(movsy):
                                ListaSalida.crearSalida(tmp13.combustible,tmp13.posx,tmp13.posy,tamañoTerreno)
                                act.combustible = int(act.combustible)+1000
                                act = tmp13
                            
                            tmp13 = tmp13.siguiente
                        
                        if int(act.posx) == int(xf) and int(act.posy) == int(yf):
                            break
                        
                    #Borde superior
                    elif (int(act.posx) == 1) and (int(act.posy) > 1) and (int(act.posy) < int(tmp2.posy)):
                        tmp14 = self.inicio
                        
                        while tmp14 is not None:

                            if int(tmp14.posy) == int(act.posy)-1 and int(tmp14.posx) == int(act.posx):
                                leftcombu = int(tmp14.combustible)

                            if int(tmp14.posy) == int(act.posy)+1 and int(tmp14.posx) == int(act.posx):
                                rightcombu = int(tmp14.combustible)

                            if int(tmp14.posx) == int(act.posx)+1 and int(tmp14.posy) == int(act.posy):
                                downcombu = int(tmp14.combustible)  
                            
                            tmp14 = tmp14.siguiente
                        
                        if leftcombu < rightcombu and leftcombu < downcombu:
                            menor = int(leftcombu)
                            movsx = act.posx
                            movsy = int(act.posy)-1
                        elif rightcombu < leftcombu and rightcombu < downcombu:
                            menor = int(rightcombu)
                            movsx = act.posx
                            movsy = int(act.posy)+1
                        elif downcombu < leftcombu and downcombu < rightcombu:
                            menor = int(downcombu)
                            movsx = int(act.posx)+1
                            movsy = act.posy
                        elif leftcombu == rightcombu and leftcombu < downcombu:
                            if restax > 0:
                                menor = int(rightcombu)
                                movsx = act.posx
                                movsy = int(act.posy)+1
                            elif restax < 0:
                                menor = int(leftcombu)
                                movsx = act.posx
                                movsy = int(act.posy)-1                            
                        else:
                            print("SON IGUALES")

                        tmp15 = self.inicio
                        while tmp15 is not None:
                            if int(tmp15.combustible) == int(menor) and int(tmp15.posx) == int(movsx) and int(tmp15.posy) == int(movsy):
                                ListaSalida.crearSalida(tmp15.combustible,tmp15.posx,tmp15.posy,tamañoTerreno)
                                act.combustible = int(act.combustible)+1000
                                act = tmp15
                            
                            tmp15 = tmp15.siguiente
                        
                        if int(act.posx) == int(xf) and int(act.posy) == int(yf):
                            break
                    #Borde inferior
                    elif (int(act.posx) == 5) and (int(act.posy) > 1) and (int(act.posy) < int(tmp2.posy)):
                        tmp16 = self.inicio
                        
                        while tmp16 is not None:

                            if int(tmp16.posy) == int(act.posy)-1 and int(tmp16.posx) == int(act.posx):
                                leftcombu = int(tmp16.combustible)

                            if int(tmp16.posy) == int(act.posy)+1 and int(tmp16.posx) == int(act.posx):
                                rightcombu = int(tmp16.combustible)

                            if int(tmp16.posx) == int(act.posx)-1 and int(tmp16.posy) == int(act.posy):
                                upcombu = int(tmp16.combustible) 
                            
                            tmp16 = tmp16.siguiente
                        
                        if leftcombu < rightcombu and leftcombu < upcombu:
                            menor = int(leftcombu)
                            movsx = int(act.posx)
                            movsy = int(act.posy)-1
                        elif rightcombu < leftcombu and rightcombu < upcombu:
                            menor = int(rightcombu)
                            movsx = int(act.posx)
                            movsy = int(act.posy)+1
                        elif upcombu < leftcombu and upcombu < rightcombu:
                            menor = int(upcombu)
                            movsx = int(act.posx)-1
                            movsy = int(act.posy)  
                        elif leftcombu == rightcombu and leftcombu < upcombu:
                            if restax > 0:
                                menor = int(rightcombu)
                                movsx = act.posx
                                movsy = int(act.posy)+1
                            elif restax < 0:
                                menor = int(leftcombu)
                                movsx = act.posx
                                movsy = int(act.posy)-1

                        elif int(act.posy)+1 == int(yf) and int(act.posx) == 5:
                            menor = int(rightcombu)
                            movsx = int(act.posx)
                            movsy = int(act.posy)+1
                        else:
                            print("SON IGUALES BORDES INFERIORES")

                        

                        tmp17 = self.inicio
                        while tmp17 is not None:
                            if int(tmp17.combustible) == int(menor) and int(tmp17.posx) == int(movsx) and int(tmp17.posy) == int(movsy):
                                ListaSalida.crearSalida(tmp17.combustible,tmp17.posx,tmp17.posy,tamañoTerreno)
                                act.combustible = int(act.combustible)+1000
                                act = tmp17
                            
                            tmp17 = tmp17.siguiente
                        
                        if int(act.posx) == int(xf) and int(act.posy) == int(yf):
                            break
                    # Bordes Derechos
                    elif (int(act.posy)==5) and (int(act.posx) > 1) and (int(act.posx) < int(tmp2.posx)):
                        tmp18 = self.inicio
                        
                        while tmp18 is not None:

                            if int(tmp18.posx) == int(act.posx)-1 and int(tmp18.posy) == int(act.posy):
                                upcombu = int(tmp18.combustible)

                            if int(tmp18.posy) == int(act.posy)-1 and int(tmp18.posx) == int(act.posx):
                                leftcombu = int(tmp18.combustible)

                            if int(tmp18.posx) == int(act.posx)+1 and int(tmp18.posy) == int(act.posy):
                                downcombu = int(tmp18.combustible)  
                            
                            tmp18 = tmp18.siguiente

                        if upcombu < leftcombu and upcombu < downcombu:
                            menor = int(upcombu)
                            movsx = int(act.posx)-1
                            movsy = act.posy  
                        elif leftcombu < upcombu and leftcombu < downcombu:
                            menor = int(leftcombu)
                            movsx = act.posx
                            movsy = int(act.posy)-1
                        elif downcombu < upcombu and downcombu < leftcombu:
                            menor = int(downcombu)
                            movsx = int(act.posx)+1
                            movsy = act.posy
                        elif upcombu == downcombu and downcombu < leftcombu:
                            if restay > 0:
                                menor = int(downcombu)
                                movsx = int(act.posx)+1
                                movsy = int(act.posy)
                            elif restay < 0:
                                menor = int(upcombu)
                                movsx = int(act.posx)-1
                                movsy = int(act.posy) 
                        else:
                            pass

                        tmp19 = self.inicio
                        while tmp19 is not None:
                            if int(tmp19.combustible) == int(menor) and int(tmp19.posx) == int(movsx) and int(tmp19.posy) == int(movsy):
                                ListaSalida.crearSalida(tmp19.combustible,tmp19.posx,tmp19.posy,tamañoTerreno)
                                act.combustible = int(act.combustible)+1000
                                act = tmp19
                            
                            tmp19 = tmp19.siguiente
                        if int(act.posx) == int(xf) and int(act.posy) == int(yf):
                            break


            tmp = tmp.siguiente
        ListaSalida.mostrarCamino()

    def salida1(self,SeleTerreno1):
        if len(SeleTerreno1) > 0:
            ListaSalida.escritura(SeleTerreno1)
        else:
            print("Debe procesar un archivo")