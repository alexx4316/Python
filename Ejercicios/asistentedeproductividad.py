from datetime import datetime
hora = input("Ingrese la hora actual en formato militar (HH:MM): ")
dia = input("Ingrese el dia de la semana: ").lower()

hora_objeto = datetime.strptime(hora, "%H:%M").time()
hora_trabajo_inicio = datetime.strptime("06:00", "%H:%M").time()
hora_trabajo_fin = datetime.strptime("18:00", "%H:%M").time()
hora_ejercicio_fin = datetime.strptime("22:00", "%H:%M").time()
hora_descanso_fin = datetime.strptime("04:30", "%H:%M").time() 
hora_descanso_inicio = datetime.strptime("22:00", "%H:%M").time()

match dia:
    case "lunes":
        if hora_trabajo_inicio <= hora_objeto < hora_trabajo_fin:
            print("Es hora de trabajar.")
        elif hora_trabajo_fin <= hora_objeto < hora_ejercicio_fin:
            print("Es hora de hacer ejercicio.")
        elif hora_objeto >= hora_descanso_inicio or hora_objeto < hora_trabajo_inicio:
            print("Es hora de descansar.")
    case "martes": 
        if hora_trabajo_inicio <= hora_objeto < hora_trabajo_fin:
            print("Es hora de trabajar.")
        elif hora_trabajo_fin <= hora_objeto < hora_ejercicio_fin:
            print("Es hora de hacer ejercicio.")
        elif hora_objeto >= hora_descanso_inicio or hora_objeto < hora_trabajo_inicio:
            print("Es hora de descansar.")
    case "miercoles":  
        if hora_trabajo_inicio <= hora_objeto < hora_trabajo_fin:
            print("Es hora de trabajar.")
        elif hora_trabajo_fin <= hora_objeto < hora_ejercicio_fin:
            print("Es hora de hacer ejercicio.")
        elif hora_objeto >= hora_descanso_inicio or hora_objeto < hora_trabajo_inicio:
            print("Es hora de descansar.")
    case "jueves":
        if hora_trabajo_inicio <= hora_objeto < hora_trabajo_fin:
            print("Es hora de trabajar.")
        elif hora_trabajo_fin <= hora_objeto < hora_ejercicio_fin:
            print("Es hora de hacer ejercicio.")
        elif hora_objeto >= hora_descanso_inicio or hora_objeto < hora_trabajo_inicio:
            print("Es hora de descansar.")
    case "viernes":
        if hora_trabajo_inicio <= hora_objeto < hora_trabajo_fin:
            print("Es hora de trabajar.")
        elif hora_trabajo_fin <= hora_objeto < hora_ejercicio_fin:
            print("Es hora de hacer ejercicio.")
        elif hora_objeto >= hora_descanso_inicio or hora_objeto < hora_trabajo_inicio:
            print("Es hora de descansar.")
    case "sabado":
            print("Puedes descansar o hacer ejercicio.")
    case "domingo": 
            print("Los domingos no se hace nada")
    case _:
        print("Dia no valido.")
        exit()
