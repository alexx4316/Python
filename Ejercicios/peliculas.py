while True:
    print("Escribe salir para salir del programa")
    edad = int(input("Ingrese su edad: "))
    preferencia = input("Cual es tu preferencia de peliculas? (Accion, Comedia, terror): ").lower()
    match preferencia:
        case "accion":
            if edad >= 18:
                print("Las peliculas que te recomiendo son: John Wick, Mad Max: Furia en el camino o The Dark Knight .")
            else:
                print("Las peliculas que te recomiendo son: Spiderman, Avengers o Los Increibles.")
        case "comedia":
            if edad >= 18:
                print("las peliculas que te recomiendo son: ¿Qué pasó ayer?, Deadpool o Superbad .")
            else:
                print("las peliculas que te recomiendo son: Mi villano favorito, Shrek 2 o Hotel Transylvania.")
        case "terror":
            if edad >= 18:
                print("las peliculas que te recomiendo son: El Conjuro, Hereditary o Insidious.")
            else:
                print("Las peliculas que te recomiendo son: Monster House, El extraño mundo de Jack o Coraline.")
        case "salir":
            print("Saliendo del programa.")
            break
        case _:
            print("Preferencia no válida.") 

