def separar(x):
    digitos = list(str(x))
    print(','.join(digitos))
# Join solo funciona con cadenas, no con enteros
# Programa para separar un número de 4 cifras en sus dígitos
        
n = int(input("Ingrese un número de 4 cifras: ")) 
separar(n)