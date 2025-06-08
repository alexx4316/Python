puntaje = 0
pregunta1 = input("Eres mayor de edad? (si/no): ")
if pregunta1 == "si":
    print("Messirve")
    puntaje = puntaje + 50  
    pregunta2 = input("Eres soltera? (si/no): ")
    if pregunta2 == "si":
        print("como seria ps")
        puntaje = puntaje + 50
    else:
        print("volvete seria, respeta la relacion")
        puntaje = puntaje - 50
    pregunta3 = input("Tienes mascotas? (si/no): ")
    if pregunta3 == "si":
        print("que lindo, me gustan las mascotas")
        puntaje = puntaje + 50
    else:
        print("jumm")
        puntaje = puntaje + 25
    pregunta4 = input("Haces algun deporte? (si/no): ")
    if pregunta4 == "si":
        print("que bien, me gustan las personas que practican deporte")
        puntaje = puntaje + 50
    else:
        print("no importa, no es necesario")
        puntaje = puntaje - 50
    pregunta5 = input("Eres estudiante? (si/no): ")
    if pregunta5 == "si":
        print("que bien, me gusta la gente estudiosa")
        puntaje = puntaje + 50
    else:
        pregunta6 = print("jumm, entonces que haces, trabajas? (si/no): ")
        if pregunta6 == "no":
            print("entonces no haces nada")
            puntaje = puntaje - 100
        else:
            print("que bien, me gusta la gente trabajadora")
            puntaje = puntaje + 50
    pregunta7 = input("Eres una persona divertida? (si/no): ")
    if pregunta7 == "si":
        print("que chimba, ya somos dos")
        puntaje = puntaje + 50
    else:
        print("doña aburrida ps")
        puntaje = puntaje - 50
    pregunta8 = input("Eres una persona amable? (si/no): ")
    if pregunta8 == "si":
        print("eso es muy importante")
        puntaje = puntaje + 100
    else:
        print("la gente que no es amable son de lo peor")
        puntaje = puntaje - 100
    pregunta9 = input("Te gusta el tinto? (si/no): ")
    if pregunta9 == "si":
        print("verdad que el tinto es vida")
        puntaje = puntaje + 50
    else:
        print("jumm, como no te va a gustar el tintico")
        puntaje = puntaje - 100
    pregunta10 = input("Te gusta la musica? (si/no): ")
    if pregunta10 == "si":
        print("que bien, me gusta la musica")
        puntaje = puntaje + 50
    else:
        print("no importa, no es necesario")
        puntaje = puntaje - 50
    pregunta11 = input("sabes cocinar? (si/no): ")
    if pregunta11 == "si":
        print("es algo importante para mi, no por que quiera que me cocines, pero es algo basico de spervivencia")
        puntaje = puntaje + 100
    else:
        print("hay que aprender a hacer algo ps")
        puntaje = puntaje - 200
                                        
else:
    print("No messirve")
    puntaje = puntaje - 100
print("Tu puntaje es: ", puntaje)
if puntaje >= 0 and puntaje <= 50:
    print("sos una basura")
if puntaje >= 50 and puntaje <=70 :
    print("hay cositas que hablar")
if puntaje >= 100:
    print("me gusta tu perfil, como seria ps para unos mua mua")
