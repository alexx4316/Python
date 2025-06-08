palabra = str(input("Introduce una palabra: "))
letra = str(input("Introduce una letra: "))
contador = 0
for i in range(len(palabra)):
    if palabra[i] == letra:
        contador += 1
print(f"la letra {letra} aparece {contador} veces en la palabra {palabra}.") 