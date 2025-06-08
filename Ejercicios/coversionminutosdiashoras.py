cantidadminutos = int(input("Ingrese la cantidad de minutos : "))
# 1 dia = 24 horas * 60 minutos = 1440 minutos
dias = cantidadminutos // 1440
print(f"Debug: cantidadminutos = {cantidadminutos}, dias = {dias}")
resto_minutos = cantidadminutos % 1440
print(f"Debug: resto_minutos = {resto_minutos}")  
horas = resto_minutos // 60
print(f"Debug: horas = {horas}")
minutos = resto_minutos % 60
print(f"Debug: minutos = {minutos}") 
print(f"las dias son: {dias} las horas son: {horas} los minutos son: {minutos}")