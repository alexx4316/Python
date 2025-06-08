numero = int(input("Ingrese un numero: "))
if numero % 3 == 0 and numero % 5 == 0:
    print("FizzBuzz")
elif numero % 3 == 0:
    print("Fizz")
elif numero % 5 == 0:
    print("Buzz")
else: 
    print("El numero ingresado no es divisible ni por 3 ni por 5")