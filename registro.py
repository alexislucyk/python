usuarios=[{
    "user":"admin",
    "pass":"admin123"}]     # Aca creo una lista con un diccionario para guardar los usuarios

menu=0

while menu==0:
    print(" -- Menu -- ")
    print(" 1 - Registro ")
    print(" 2 - Consulta ")
    print(" 3 - Salir ")
    seleccion=int(input("Seleccione una opcion: "))
    if seleccion==1: 
        print(" 1 - Registro ")
        nombre=input("Ingrese nombre de usuario: ")
        contra=input("Ingrese una contraseña: ")
        usuarios.append({"usr":nombre , "pass":contra})
        print(usuarios)

    elif seleccion==2:
        print(" 2 - Consulta ")
    elif seleccion==3:
        print(" 3 - Salir ")
        exit()
    else:
        print(" ## Opcion Invalida ##")