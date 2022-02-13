clase  Cola_1 :
    def  __init__ ( self , tamanio ):
        uno mismo lista = []
        uno mismo tamaño = tamanio
        uno mismo arriba = 0

    def  empujar ( self , dato ):
        si  uno mismo . arriba  < uno mismo . tamaño :
            uno mismo lista  =  uno mismo . lista  + [ dato ]
            uno mismo arriba  +=  1
            volver  verdadero
        más :
            volver  falso

    def  pop ( uno mismo ):
        si  uno mismo . vacío ():
            volver  Ninguno
        más :
            arriba  =  uno mismo . lista [ 0 ]
            uno mismo lista  =  uno mismo . lista [ 1 :]
            uno mismo arriba  -=  1
            volver  arriba
            
    def  mostrar ( auto ):
        para  top  en  rango ( self . top ):
            imprimir ( "[{}]" . format ( self . lista [ top ]))
        
    def  longitud ( auto ):
        devolverse  a uno mismo . cima
                
    def  vacío ( auto ):
        si  uno mismo . arriba  ==  0 :
            volver  verdadero
        más :
            volver  falso
# cola=Cola_1(3)
# imprimir(cola.empujar(20))
# imprimir(cola.empujar(25))
# imprimir(cola.empujar(30))
# imprimir(cola.empujar(35))
# cola.mostrar()
# dato=cola.pop()
# if dato: print("El dato eliminado es: {}".format(dato))
# else: print("La lista esta vacia")
# input("Presione una tecla para continuar...")
# dato=cola.pop()
# if dato: print("El dato eliminado es: {}".format(dato))
# else: print("La lista esta vacia")
# input("Presione una tecla para continuar...")
# cola.mostrar()
