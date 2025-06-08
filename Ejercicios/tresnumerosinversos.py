num = int(input("Ingrese un valor de 3 digitos: "))
decenas = (num % 100) //10
centenas = (num // 100)
unidades = (num % 10)
print("El valor inverso es ",unidades,decenas,centenas) 