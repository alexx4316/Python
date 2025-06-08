lista = [10, 20, 30, 40,50]
if 30 in lista:
    print("El elemento 30 se encuentra en la lista")
posicion = lista.index(30) # Obtener la posicion del elemento 30
veces = lista.count(20)
print("El index del numero 30 es:", posicion) # Imprimir la posicion del elemento 30
print("El numero 20 aparece", veces, "veces") # Imprimir la cantidad de veces que aparece el elemento 20  