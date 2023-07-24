usuarios={}    # Aca creo una lista con un diccionario para guardar los usuarios

def nuevo_usuario(usr,pwd): # Funcion para agregar usuario
    if usr in usuarios:
        print (f'El usuario ya existe, ingrese otro.!!')
    else:
        usuarios[usr]=pwd
        print(f'¡¡El usuario: {usr}, Contraseña: {pwd}, Se registro exitosamente!!')

def todos_usuarios():   # Funcion para mostrar todos los usuarios y contraseña
    for usr,pwd in usuarios.items():
        print(f'Usuario: {usr}, Contraseña: {pwd}')

def login():    # Funcion de Login
    usr=input("Ingrese nombre de usuario: ")
    pwd=input("Ingrese una contraseña: ")
    if usr in usuarios and usuarios[usr]==pwd:
        print('Acceso concedido!!')
    else:
        print('Usuario y/o contraseña erroneos, intente de nuevo')

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
        while True:
            print('Para volver precione 9')
            usr=input("Ingrese nombre de usuario: ")
            if usr=='9':
                break
            pwd=input("Ingrese una contraseña: ")
            nuevo_usuario(usr,pwd)
            break

    elif seleccion==2:
        print(" 2 - Consulta todos los usuarios ")
        print(todos_usuarios())

    elif seleccion==3:
        print(" 3 - Login ")
        login()

    elif seleccion==9:
        exit()
    else:
        print(" ## Opcion Invalida ##")