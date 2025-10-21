#Una agencia de viajes nos pide informar si hacemos viajes a lugares según la estación del año. 
#En caso de hacerlo mostrar por print  el mensaje “Se viaja”, caso contrario mostrar “No se viaja”. 
#Si es invierno: solo se viaja a Bariloche.
#Si es verano: se viaja a Mar del plata y Cataratas.
#Si es otoño: se viaja a todos los lugares.
#Si es primavera: se viaja a todos los lugares menos Bariloche

viaje =int(input("Elegir un numero que represente la temporada que desea viajar (primavera:1, verano:2, otoño:3 o invierno:4):"))
lugar = int(input("Elija ahora un numero al lugar que desea viajar (Bariloche:1 ,Cataratas:2 ,MAr del Plata:3,Otro:4)"))

match  viaje:
    case 1 :
        if lugar == 1:
            print("No se viaja")
        else:
            print("Se viaja")
    case 2 :
        if lugar == 2:
            print("Se viaja")
        if lugar == 3:
            print("Se viaja")
        else:
            print("No se viaja")
    case 3 : 
        print("Se viaja a todos los lugares")
    case 4 : 
        if lugar == 1:
            print("Se viaja")
        else:
            print("No se viaja")
    case _ :
        print("Incorrecto")