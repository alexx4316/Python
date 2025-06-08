vlrcomida = int(input("Ingrese el valor de su comida: "))

#Descuentos
descuento1 = vlrcomida*(10/100)
descuento2 = vlrcomida*(15/100)
descuento3 = vlrcomida*(20/100)
#Vlor final con el descuento  
valordesc1 = vlrcomida - descuento1
valordesc2 = vlrcomida - descuento2
valordesc3 = vlrcomida - descuento3

print("el valor a pagar con el descuento del 10 es: ", valordesc1)
print("el valor a pagar con el descuento del 15 es: ", valordesc2)
print("el valor a pagar con el descuento del 20 es: ", valordesc3)