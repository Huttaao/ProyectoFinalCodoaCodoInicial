#Comandos
import os

#Funciones.

def creacion_de_cuenta():
    while True:
        crearcuenta = ". ݁₊ ⊹ . ݁˖ . ݁ Crear cuenta . ݁₊ ⊹ . ݁˖ . ݁"
        crearcuenta_centrado = crearcuenta.center(70)
        print(crearcuenta_centrado)
        NombreUsuario = input ("Ingrese un nombre de usuario: ").strip() # Elimina espacios en blanco.
        ContraseñaUsuario = input ("Ingrese una contraseña: ").strip()
        ContraseñaUsuario1 = input ("Ingrese nuevamente la contraseña: ").strip()
        
        if not NombreUsuario or not ContraseñaUsuario: #Por si el usuario ingresa un espacio en blanco
            print("Error. Debe ingresar un nombre de usuario y una contraseña válida.")
        elif ContraseñaUsuario1 == ContraseñaUsuario:
            os.system('cls')
            print ("¡¡¡Cuenta creada exitosamente!!! <(˶ᵔᵕᵔ˶)>")
            print ("Ya puede iniciar sesión.")
            print (" ")
            return NombreUsuario, ContraseñaUsuario #Devuelve valores para verificarlos en el inicio de sesion.
            break  # Sale del bucle ya que las contraseñas coinciden
        else:
            os.system('cls') 
            print ("Error.Las Contraseñas ingresadas no son iguales. Intentelo nuevamente.") #Se repite bucle hasta que coincidan.
            print (" ")
            encabezado_bienvenidainicial ()



def encabezado_bienvenidainicial():
    print (" ")
    decoracion = " ˖⁺‧₊˚♡˚₊‧⁺˖ "
    decoracion_centrado = decoracion.center(70)
    print(decoracion_centrado)
    bienvenida = "¡Bienvenido a tu Agenda Personal"
    bienvenida_centrado = bienvenida.center(70)
    print(bienvenida_centrado)
    print("──★ ˙ ̟Para comenzar, le solicitamos que cree una cuenta como nuevo usuario.")

def encabezado_bienvenidapredeterminada():
    print (" ")
    decoracion = " ˖⁺‧₊˚♡˚₊‧⁺˖ "
    decoracion_centrado = decoracion.center(70)
    print(decoracion_centrado)
    bienvenida = "¡Bienvenido a tu Agenda Personal"
    bienvenida_centrado = bienvenida.center(70)
    print(bienvenida_centrado)

def inicio_sesion(NombreUsuario, ContraseñaUsuario):
    while True:
        iniciarsesion = ". ݁₊ ⊹ . ݁˖ . ݁ Iniciar sesión . ݁₊ ⊹ . ݁˖ . ݁"
        iniciarsesion_centrado = iniciarsesion.center(70)
        print(iniciarsesion_centrado)
        nombre_ingresado = input("Ingrese su nombre de usuario: ")
        contraseña_ingresada = input("Ingrese su contraseña: ")

        if nombre_ingresado == NombreUsuario and contraseña_ingresada == ContraseñaUsuario:
            os.system('cls')
            print("¡¡¡Inicio de sesión exitoso!!! ٩(^ᗜ ^ )و")
            print (" ")
            break
        else:
            os.system('cls') 
            print("Nombre de usuario o contraseña incorrectos. Inténtalo nuevamente.")
            print (" ")
            encabezado_bienvenidapredeterminada()


def mostrar_menu():
    encabezado_bienvenidapredeterminada()
    print (" ")
    decoracion = "⋅˚₊‧ ୨୧ ‧₊˚"
    decoracion_centrada = decoracion.center(70)
    print(decoracion_centrada)
    print("""
    ˗ˏˋ Menu Principal ˎˊ˗
    1. Agregar tarea๋࣭ ⭑
    2. Ver tareas๋࣭ ⭑
    3. Marcar tarea como completada๋࣭ ⭑
    4. Salir๋࣭ ⭑""")
    print(decoracion_centrada)

def opcion_menu(opcion,lista_de_tareas):
    
    match opcion:
        case "1":
            agregar_tarea(lista_de_tareas)
        case "2":
            ver_tareas()
        case "3":
            marcar_completada()
        case "4":
            print("¡Nos vemos! ₍ᐢ. .ᐢ₎")
        case _:
            print("Opción inválida. Inténtalo nuevamente.")


def agregar_tarea(tarea):
    titulo = input("ʚɞ Ingrese el titulo de la tarea: ")
    descripcion = input("ʚɞ Ingrese la descripción de la tarea: ")
    fecha_vencimiento = input("ʚɞ Ingrese la fecha de vencimiento (dia/mes/año): ")
    tarea.append({"titulo": titulo, "descripcion": descripcion, "fecha_vencimiento": fecha_vencimiento})


#Main
encabezado_bienvenidainicial() #Bienvenida al usuario

NombreUsuario, ContraseñaUsuario = creacion_de_cuenta() #creacion de la cuenta
inicio_sesion(NombreUsuario,ContraseñaUsuario) #inicio de sesion de la cuenta

#Borra todo lo anterior, para pasar a mostrar el menu.


while True: #Muestra menu principal
    lista_de_tareas = [] 
    mostrar_menu() 
    print (" ")
    opcion = input("──★ ˙ ̟Seleccione una opción: ")
    print (" ")
    opcion_menu (opcion,lista_de_tareas)
    if opcion == "4":
        break









