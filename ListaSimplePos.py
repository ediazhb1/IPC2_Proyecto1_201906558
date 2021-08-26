from Posiciones import Posiciones

class ListaSimplePos():
    def __init__(self):
        self.inicio = None #Nodo inicial de la lista
        self.fin = None #Nodo final de la lista
        self.posactual = None
        self.prueba = []
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
    
        
    def PosicionComienzo(self,xo,yo,xf,yf):
        tmp = self.inicio
        tmp2 = self.fin

        downcombu =0
        upcombu = 0
        leftcombu = 0
        rightcombu = 0
        menor =0
        movsx = 0
        movsy = 0
        DosCaminos = False
        while tmp is not None:
            if tmp.posx == xo and tmp.posy == yo:
                self.prueba.append("Combustible: "+tmp.combustible+" posx: " +tmp.posx +" posy: "+tmp.posy)
                self.posactual = tmp
                act = self.posactual
                a = 0
                while act.posx != xf and act.posy != yf and a !=70:
                    a +=1
                    if int(act.posx) < int(tmp2.posx) and int(act.posy) < int(tmp2.posy) and int(act.posx) > 1 and int(act.posy) > 1:   
                        tmp3 = self.inicio
                        
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

                        
                        if rightcombu < leftcombu and rightcombu < downcombu and rightcombu < upcombu:
                            menor = int(rightcombu)
                            movsx = act.posx
                            movsy = int(act.posy)+1                           
                        elif leftcombu < rightcombu and leftcombu < upcombu and leftcombu < downcombu:                          
                            menor = int(leftcombu)
                            movsx = act.posx
                            movsy = int(act.posy)-1     
                        elif downcombu < rightcombu and downcombu < upcombu and downcombu < leftcombu:
                            menor = int(downcombu)
                            movsx = int(act.posx)+1
                            movsy = act.posy    
                        elif upcombu < rightcombu and upcombu < leftcombu and upcombu < downcombu:
                            menor = int(upcombu)
                            movsx = int(act.posx)-1
                            movsy = act.posy 
                        #-----------------------------------------------------------------------------
                        elif rightcombu == leftcombu and upcombu < downcombu and upcombu < rightcombu:
                            menor = int(upcombu)
                            movsx = int(act.posx)-1
                            movsy = act.posy 
                        elif rightcombu == leftcombu and downcombu < upcombu and downcombu < rightcombu:
                            menor = int(downcombu)
                            movsx = int(act.posx)+1
                            movsy = act.posy   
                        elif rightcombu == leftcombu and leftcombu < upcombu and leftcombu < downcombu:
                            menor = int(leftcombu) #DOS MENORES, DOS CAMINOS
                            movsx = act.posx
                            movsy = int(act.posy)-1
                            DosCaminos = True
                        elif upcombu == downcombu and leftcombu < rightcombu and leftcombu < upcombu:
                            menor = int(leftcombu)
                            movsx = act.posx
                            movsy = int(act.posy)-1
                        elif upcombu == downcombu and rightcombu < leftcombu and rightcombu < upcombu:
                            menor = int(rightcombu)
                            movsx = act.posx
                            movsy = int(act.posy)+1 
                        elif upcombu == downcombu and downcombu < leftcombu and downcombu < rightcombu:
                            menor = int(downcombu) #DOS MENORES, DOS CAMINOS
                            movsx = int(act.posx)+1
                            movsy = act.posy   
                            DosCaminos = True
                        elif leftcombu == upcombu and rightcombu < downcombu and rightcombu < leftcombu:
                            menor = int(rightcombu)
                            movsx = act.posx
                            movsy = int(act.posy)+1 
                        elif leftcombu == upcombu and downcombu < rightcombu and downcombu < leftcombu:
                            menor = int(downcombu)
                            movsx = int(act.posx)+1
                            movsy = act.posy   
                        elif leftcombu == upcombu and upcombu < rightcombu and upcombu < downcombu:
                            menor = int(upcombu) #DOS MENORES, DOS CAMINOS
                            movsx = int(act.posx)-1
                            movsy = act.posy 
                            DosCaminos = True
                        elif downcombu == leftcombu and upcombu < rightcombu and upcombu < downcombu:
                            menor = int(upcombu)
                            movsx = int(act.posx)-1
                            movsy = act.posy 
                        elif downcombu == leftcombu and rightcombu < upcombu and rightcombu < downcombu:
                            menor = int(rightcombu)
                            movsx = act.posx
                            movsy = int(act.posy)+1 
                        elif downcombu == leftcombu and  leftcombu < upcombu and leftcombu < rightcombu:
                            menor = int(leftcombu) #DOS MENORES, DOS CAMINOS
                            movsx = act.posx
                            movsy = int(act.posy)-1
                            DosCaminos = True
                        #-----------------------------------------------------------------------------

                        elif upcombu == leftcombu == downcombu and downcombu < leftcombu:
                            menor = int(downcombu)
                            movsx = int(act.posx)+1
                            movsy = act.posy   
                        elif upcombu == leftcombu == rightcombu and rightcombu < downcombu:
                            menor = int(rightcombu)
                            movsx = act.posx
                            movsy = int(act.posy)+1 
                        elif upcombu == rightcombu == downcombu and downcombu < rightcombu:
                            menor = int(downcombu)
                            movsx = int(act.posx)+1
                            movsy = act.posy   
                        elif leftcombu == rightcombu == downcombu and downcombu < upcombu:
                            menor = int(downcombu)
                            movsx = int(act.posx)+1
                            movsy = act.posy   
                        else:
                            print("SON IGUALES")

                        tmp4 = self.inicio
                        while tmp4 is not None:
                            if int(tmp4.combustible) == int(menor) and int(tmp4.posx) == int(movsx) and int(tmp4.posy) == int(movsy):
                                self.prueba.append("Combustible: "+tmp4.combustible+" posx: " +tmp4.posx +" posy: "+tmp4.posy)
                                act.combustible = int(act.combustible)+1000
                                self.posactual = tmp4
                                act = self.posactual
                            
                            tmp4 = tmp4.siguiente

                    #Esquina inferior derecha 
                    elif (int(tmp2.posx) == int(act.posx) and int(tmp2.posy) == int(act.posy)):
                        tmp5 = self.inicio
                        while tmp5 is not None:

                            if int(tmp5.posx) == int(act.posx)-1 and int(tmp5.posy) == int(act.posy):
                                upcombu = int(tmp5.combustible)

                            if int(tmp5.posy) == int(act.posy)-1 and int(tmp5.posx) == int(act.posx):
                                leftcombu = int(tmp5.combustible)

                            tmp5 = tmp5.siguiente

                        if upcombu < leftcombu:
                            menor = int(upcombu)
                            movsx = int(act.posx)-1
                            movsy = act.posy
                        elif leftcombu < upcombu:
                            menor = int(leftcombu)
                            movsx = act.posx
                            movsy = int(act.posy)-1
                        else:
                            print("SON IGUALES")

                        tmp6 = self.inicio
                        while tmp6 is not None:
                            if int(tmp6.combustible) == int(menor) and int(tmp6.posx) == int(movsx) and int(tmp6.posy) == int(movsy):
                                self.prueba.append("Combustible: "+tmp6.combustible+" posx: " +tmp6.posx +" posy: "+tmp6.posy)
                                act.combustible = int(act.combustible)+1000
                                self.posactual = tmp6
                                act = self.posactual
                            
                            tmp6 = tmp6.siguiente
                    # Esquina Superior Izquierda       
                    elif (int(act.posx) == 1 and int(act.posy) == 1):
                        
                        tmp6 = self.inicio
                        while tmp6 is not None:
                            if int(tmp6.posy) == int(act.posy)+1 and int(tmp6.posx) == int(act.posx):
                                rightcombu = int(tmp6.combustible)

                            if int(tmp6.posx) == int(act.posx)+1 and int(tmp6.posy) == int(act.posy):
                                downcombu = int(tmp6.combustible)  

                            tmp6 = tmp6.siguiente

                        
                        if rightcombu < downcombu:
                            menor = int(rightcombu)
                            movsx = act.posx
                            movsy = int(act.posy)+1 
                        elif downcombu < rightcombu:
                            menor = int(downcombu)
                            movsx = int(act.posx)+1
                            movsy = act.posy   
                        else:
                            print("SON IGUALES")

                        tmp7 = self.inicio
                        while tmp7 is not None:
                            if int(tmp7.combustible) == int(menor) and int(tmp7.posx) == int(movsx) and int(tmp7.posy) == int(movsy):
                                self.prueba.append("Combustible: "+tmp7.combustible+" posx: " +tmp7.posx +" posy: "+tmp7.posy)
                                act.combustible = int(act.combustible)+1000
                                self.posactual = tmp7
                                act = self.posactual
                            
                            tmp7 = tmp7.siguiente
                    #Esquina superior Derecha 
                    elif (int(act.posx) ==1) and (int(act.posy) == int(tmp2.posy)):
                        tmp9 = self.inicio
                        while tmp9 is not None:
                            if int(tmp9.posy) == int(act.posy)-1 and int(tmp9.posx) == int(act.posx):
                                leftcombu = int(tmp9.combustible)

                            if int(tmp9.posx) == int(act.posx)+1 and int(tmp9.posy) == int(act.posy):
                                downcombu = int(tmp9.combustible)  

                            tmp9 = tmp9.siguiente
                        
                        if leftcombu < upcombu:
                            menor = int(leftcombu)
                            movsx = act.posx
                            movsy = int(act.posy)-1
                        elif downcombu < rightcombu:
                            menor = int(downcombu)
                            movsx = int(act.posx)+1
                            movsy = act.posy   
                        else:
                            print("SON IGUALES")

                        tmp8 = self.inicio
                        while tmp8 is not None:
                            if int(tmp8.combustible) == int(menor) and int(tmp8.posx) == int(movsx) and int(tmp8.posy) == int(movsy):
                                self.prueba.append("Combustible: "+tmp8.combustible+" posx: " +tmp8.posx +" posy: "+tmp8.posy)
                                act.combustible = int(act.combustible)+1000
                                self.posactual = tmp8
                                act = self.posactual
                            
                            tmp8 = tmp8.siguiente
                        
                    #Esquina Inferior Izquierda 
                    elif (int(act.posx) == int(tmp2.posx) and int(act.posy) == 1):
                        
                        tmp10 = self.inicio
                        while tmp10 is not None:
                            if int(tmp10.posy) == int(act.posy)+1 and int(tmp10.posx) == int(act.posx):
                                rightcombu = int(tmp10.combustible)

                            if int(tmp10.posx) == int(act.posx)-1 and int(tmp10.posy) == int(act.posy):
                                upcombu = int(tmp10.combustible)

                            tmp10 = tmp10.siguiente

                        
                        if rightcombu < upcombu:
                            menor = int(rightcombu)
                            movsx = act.posx
                            movsy = int(act.posy)+1 
                        elif upcombu < rightcombu:
                            menor = int(upcombu)
                            movsx = int(act.posx)-1
                            movsy = act.posy  
                        else:
                            print("SON IGUALES")

                        tmp11 = self.inicio
                        while tmp11 is not None:
                            if int(tmp11.combustible) == int(menor) and int(tmp11.posx) == int(movsx) and int(tmp11.posy) == int(movsy):
                                self.prueba.append("Combustible: "+tmp11.combustible+" posx: " +tmp11.posx +" posy: "+tmp11.posy)
                                act.combustible = int(act.combustible)+1000
                                self.posactual = tmp11
                                act = self.posactual
                            
                            tmp11 = tmp11.siguiente

                    #Bordes izquierdos
                    elif (int(act.posy)==1) and (int(act.posx) > 1) and (int(act.posx) < int(tmp2.posx)):
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
                            movsy = act.posy  
                        elif rightcombu < upcombu and rightcombu < downcombu:
                            menor = int(rightcombu)
                            movsx = act.posx
                            movsy = int(act.posy)+1
                        elif downcombu < upcombu and downcombu < rightcombu:
                            menor = int(downcombu)
                            movsx = int(act.posx)+1
                            movsy = act.posy
                        else:
                            print("SON IGUALES")

                        tmp13 = self.inicio
                        while tmp13 is not None:
                            if int(tmp13.combustible) == int(menor) and int(tmp13.posx) == int(movsx) and int(tmp13.posy) == int(movsy):
                                self.prueba.append("Combustible: "+tmp13.combustible+" posx: " +tmp13.posx +" posy: "+tmp13.posy)
                                act.combustible = int(act.combustible)+1000
                                self.posactual = tmp13
                                act = self.posactual
                            
                            tmp13 = tmp13.siguiente

                    #Borde superior
                    elif (int(act.posx) == 1) and (int(act.posy) > 1) and (int(act.posy) < int(tmp2.posy)):
                        tmp14 = self.inicio
                        
                        while tmp14 is not None:

                            if int(tmp14.posy) == int(act.posy)-1 and int(tmp14.posx) == int(act.posx):
                                leftcombu = int(tmp9.combustible)

                            if int(tmp14.posy) == int(act.posy)+1 and int(tmp14.posx) == int(act.posx):
                                rightcombu = int(tmp12.combustible)

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
                        else:
                            print("SON IGUALES")

                        tmp15 = self.inicio
                        while tmp15 is not None:
                            if int(tmp15.combustible) == int(menor) and int(tmp15.posx) == int(movsx) and int(tmp15.posy) == int(movsy):
                                self.prueba.append("Combustible: "+tmp15.combustible+" posx: " +tmp15.posx +" posy: "+tmp15.posy)
                                act.combustible = int(act.combustible)+1000
                                self.posactual = tmp15
                                act = self.posactual
                            
                            tmp15 = tmp15.siguiente
                            
                    #Borde inferior
                    elif (int(act.posx) == 1) and (int(act.posy) > 1) and (int(act.posy) < int(tmp2.posy)):
                        tmp14 = self.inicio
                        
                        while tmp14 is not None:

                            if int(tmp14.posy) == int(act.posy)-1 and int(tmp14.posx) == int(act.posx):
                                leftcombu = int(tmp9.combustible)

                            if int(tmp14.posy) == int(act.posy)+1 and int(tmp14.posx) == int(act.posx):
                                rightcombu = int(tmp12.combustible)

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
                        else:
                            print("SON IGUALES")

                        tmp15 = self.inicio
                        while tmp15 is not None:
                            if int(tmp15.combustible) == int(menor) and int(tmp15.posx) == int(movsx) and int(tmp15.posy) == int(movsy):
                                self.prueba.append("Combustible: "+tmp15.combustible+" posx: " +tmp15.posx +" posy: "+tmp15.posy)
                                act.combustible = int(act.combustible)+1000
                                self.posactual = tmp15
                                act = self.posactual
                            
                            tmp15 = tmp15.siguiente


            tmp = tmp.siguiente

        print(self.prueba)
           