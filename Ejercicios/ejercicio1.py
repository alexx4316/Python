producto = input("Ingrese el nombre del producto: ")
while True:
    try:
        preciouni = float(input("Ingrese el precio unitario del producto: "))
        if preciouni < 0:
            print("El precio no puede ser negativo.")
        else:
            break
        #El valuError es una exepcion propia de python que evaluo numero en vez de letras, caracterres especiales y espacios vacios
    except ValueError:
        print("Entrada invalida, tiene que ser un numero positivo")
while True: 
    try:
        cantidadprod = float(input("Ingrese la cantidad de producto que desea comprar: "))
        if cantidadprod < 0:
            print("La cantidad no puede ser negativa.")
        else:
            break
    except ValueError:
        print("Entrada invalida, tiene que ser un numero positivo")
while True:
    try:
        descuento = float(input("Ingresa el porcentaje de descuento entre 0 a 100%: "))
        if descuento < 0:
            print("El descuento no puede ser negativo.")
        else:
            break
    except ValueError:
        print("Entrada invalida, tiene que ser un numero positivo")

if 0 <= descuento <= 100:
    valortotal = cantidadprod * preciouni
    
    if descuento <= 0:
        print("El producto no tiene descuento.")
        print("Valor total:", valortotal)
    else:
        valordescuento = valortotal * (descuento / 100)
        valorfinal = valortotal - valordescuento
        print("El valor total es: ", valortotal)
        print("El valor con descuento es:", valorfinal)
        print("El descuento es de: ", valordescuento)
        print("Producto:", producto)

else:
    print("❌ El descuento ingresado no es válido. Debe estar entre 0 y 100.")


