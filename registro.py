usuarios=[{
    "usr":"admin",
    "pwd":"admin123"},
    {"usr":"alucyk",
    "pwd":"lucyk"},
    {"usr":"pablo",
    "pwd":"lucyk2"}]     # Aca creo una lista con un diccionario para guardar los usuarios

def muestra_usuario(nuevo_usuario,nueva_contra):
    return f'¡¡ Nuevo Usuario: {nuevo_usuario}, Contraseña: {nueva_contra} !!'  # Funcion para mostrar el nuevo usuario agregado

def todos_usuarios():
    return usuarios

menu=0
while menu==0:
    print(" -- Menu -- ")
    print(" 1 - Registro ")
    print(" 2 - Consulta todos los usuarios ")
    print(" 3 - Login ")
    print(" 9 - Salir ")
    seleccion=int(input("Seleccione una opcion: "))
    if seleccion==1: 
        print(" 1 - Registro ")
        nombre=input("Ingrese nombre de usuario: ")
        contra=input("Ingrese una contraseña: ")
        for i in usuarios:      # Aca controlo que no se registren usuarios repetidos
            if i["usr"]!=nombre:        # Comprobando si el usuario no existe, agrega uno nuevo
                usuarios.append({"usr":nombre , "pwd":contra})  # Agregando nuevo usuaro a la lista
                print(muestra_usuario(nombre,contra))
                break
            else:
                print("El usuario ya existe, ingrese otro..!!")

    elif seleccion==2:
        print(" 2 - Consulta todos los usuarios ")
        print(todos_usuarios())

    elif seleccion==3:
        print(" 3 - Login ")
        log_nombre=input("Ingrese nombre de usuario: ") # Recibo los datos para el login
        log_contra=input("Ingrese una contraseña: ")
        for login in usuarios:
            if login["usr"]==log_nombre and login["pwd"]==log_contra:   #Si los datos coinciden con el diccionario, accede.
                print("Acceso concedido!!")
                break
            else:
                print("El usuario o la contraseña es incorrecto!!")
                break

    elif seleccion==9:
        print(" 9 - Salir ")
        exit()
    else:
        print(" ## Opcion Invalida ##")