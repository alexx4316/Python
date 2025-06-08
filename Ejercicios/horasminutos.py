cantidadseg = int(input("Ingrese la cantidad de : "))
horas = (cantidadseg / 3600)
minutos = (cantidadseg % 3600) / 60
segundos = (cantidadseg % 60)
print("las horas son: ", horas, "los minutos son: ",minutos, "los segundos son: ",segundos) 