#Calificación individual y estado
nota1 = int(input("Ingrese una calificación numérica de 0 a 100: "))
if nota1 >= 70:
    print("Aprueba")
else:
    print("Desaprueba")

#Ingreso de lista de calificaciones
entrada = input("\nIngresa las calificaciones separadas por comas (ej: 3.0,4.0,5.0): ")
partes = entrada.split(',')

suma = 0
cantidad = 0 
calificaciones = []

#Calcular promedio
for parte in partes:
    try:
        numero = float(parte.strip())
        calificaciones.append(numero)
        suma += numero
        cantidad += 1
    except ValueError:
        print(f"'{parte}' no es un número válido. Se omitirá.")

if cantidad > 0:
    promedio = suma / cantidad
    print(f"\nEl promedio de las calificaciones es: {promedio:.2f}")
else:
    print("No se ingresaron calificaciones válidas.")
    exit()

#Buscar una calificación específica y contarla
calificacion_buscar = float(input("\n¿Qué calificación deseas buscar?: "))
contador = 0

for nota in calificaciones:
    if nota == calificacion_buscar:
        contador += 1
    elif nota < 0:
        continue 

if contador > 0:
    print(f"La calificación {calificacion_buscar} aparece {contador} veces.")
else:
    print(f"La calificación {calificacion_buscar} no fue encontrada.")

#Contar cuántas calificaciones son mayores a la buscada, usando while
indice = 0
mayores = 0

while indice < len(calificaciones):
    if calificaciones[indice] > calificacion_buscar:
        mayores += 1
    indice += 1

print(f"\nHay {mayores} calificaciones mayores que {calificacion_buscar}.")
