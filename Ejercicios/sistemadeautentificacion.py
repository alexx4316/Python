contraseña = "Andres2502*"
codigo = 2502

intentos_contraseña = 3
intentos_codigo = 3
nombre = input("Ingrese su nombre: ")
while intentos_contraseña > 0:
    contraseñaingresada = input("Ingrese su contraseña: ") 
    if contraseñaingresada == contraseña:
        while intentos_codigo > 0:
            codigoingresado = int(input("Ingrese su codigo: "))
            if codigoingresado == codigo:
                print(f"Bienvenido {nombre}, acceso concedido.")
                break
            else:
                intentos_codigo -= 1
                if intentos_codigo == 0:
                    print("Codigo y contraseña incorrectas, acceso denegado.")
                    break 
    else:
        intentos_contraseña -= 1
        if intentos_contraseña == 0:
            print("Contraseña y codigo incorrectos, acceso denegado.")
        

