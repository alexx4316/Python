num = int(input("Ingrese un número: "))    
for i in range(2, num):
    if num % i == 0:
        print(f"{num} no es primo")
        break
    else:
        print(f"{num} es primo") 
        break