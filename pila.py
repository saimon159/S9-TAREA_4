clase  pila :
    def  __init__ ( self , tamanio = 1 ):
        uno mismo lista = []
        uno mismo tamaño = tamanio
        uno mismo topo = 0

    def  empujar ( self , dato ):
        si  uno mismo . arriba  <  uno mismo . tamaño :
            uno mismo lista  =  uno mismo . lista  + [ dato ]
            uno mismo arriba  +=  1
        más :
            print ( "La lista esta llena" )

    def  pop ( uno mismo ):
        si  uno mismo . vacío ():
            volver  Ninguno
        más :
            arriba  =  uno mismo . lista [ - 1 ]
            uno mismo lista  =  uno mismo . lista [: - 1 ]
            uno mismo arriba  -=  1
            volver  arriba

    def  mostrar ( auto ):
        para la  parte superior  del  rango ( self . top - 1 , - 1 , - 1 ):
                imprimir ( "[{}]" . format ( self . lista [ top ]))

        def  longuitud ( auto ):
            devolverse  a uno mismo . cima

        def  mostrar ( auto ):
            para la  parte superior  del  rango ( self . top - 1 , - 1 , - 1 ):
                imprimir ( "[{}]" . format ( self . lista [ top ]))

    def  vacío ( auto ):
        si  uno mismo . arriba == 0 :
            volver  verdadero
        más :
            volver  falso

pila1  =  pila ( 3 )
pila1 _ empujar ( 8 )
pila1 _ empujar ( 10 )
pila1 _ empujar ( 12 )
pila1 _ empujar ( 4 )
dato  =  pila1 . estallar ()

pila1 _ mostrar ()
imprimir ( pila1 . longitud ())

#if dato: print("El dato eliminado es; {}",format(dato))
#else: print("La lista esta vacia")
#if dato: print("El dato eliminado es; {}",format(dato))
#else: print("La lista esta vacia")
#if dato: print("El dato eliminado es; {}",format(dato))
#else: print("La lista esta vacia")
#if dato: print("El dato eliminado es; {}",format(dato))
#else: print("La lista esta vacia")

número  =  Ninguno
si  num : imprimir ( "Tiene valor" )
