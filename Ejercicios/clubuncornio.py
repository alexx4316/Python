edad = int(input("Digita tu edad en #: "))
if edad > 18 and edad < 25:
    pase = input("Tienes el pase dorado: si/no: ")
    if pase == 'si':
        print("Puedes ingresar al super club de los unicornios ninja")
    elif pase == 'no':
        input("Complicado, ingrese la edad para saber si puede entrar: ")
        if edad >= 18 or edad <= 25: 
            print("Puedes ingresar solo con la edad")
        else:
            print("No puedes ingresar, no cumples con ninguno de los requisitos")
else:
    print("No puedes entrar estas muy peque o muy grande")

