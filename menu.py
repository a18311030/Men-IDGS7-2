import subprocess
import time

def mostrar_menu():
    print("=== Menú ===")
    print("1. Encontrar IP Socket")
    print("2. Encontrar IP Comando CLI")
    print("3. Banner grabbing")
    print("4. Escaneo de puertos")
    print("0. Salir")

def ejecutar_comando(comando):
    try:
        resultado = subprocess.run(comando, shell=True, check=True)
        return resultado
    except subprocess.CalledProcessError as e:
        print(f"Error al ejecutar el comando: {comando}")
        print(f"Detalles: {e}")

def encontrar_ip_socket():
    print("Has elegido la Opción 1: Encontrar IP Socket")
    time.sleep(1)
    while True:
        dominio = input("Ingresa la dirección: ")
        if dominio.lower() == 'volver':
            break
        comando = f"python ip_socket.py -t {dominio}"
        ejecutar_comando(comando)
        print("Comando ejecutado. Puedes ingresar otra dirección o escribir 'volver'.")

def comando_cli():
    print("Has elegido la Opción 2: Encontrar IP Comando CLI")
    time.sleep(1)
    while True:
        dominio = input("Ingresa la dirección: ")
        if dominio.lower() == 'volver':
            break
        comando = f"python comando_cli.py -t {dominio}"
        ejecutar_comando(comando)
        print("Comando ejecutado. Puedes ingresar otra dirección o escribir 'volver'.")

def banner_grabbing():
    print("Has elegido la Opción 3: Banner Grabbing")
    time.sleep(1)
    while True:
        dominio = input("Ingresa la dirección: ")
        if dominio.lower() == 'volver':
            break

        puerto = input("Ingresa el puerto: ")
        if puerto.lower() == 'volver':
            break

        if not puerto.isdigit():
            print("Por favor, ingresa un número válido para el puerto.")
            continue

        comando = f"python banner_grabing.py -t {dominio} -p {puerto}"
        ejecutar_comando(comando)
        print("Comando ejecutado. Puedes ingresar otra dirección o puerto o escribir 'volver'.")

def escaneo_puertos():
    print("Has elegido la Opción 4: Escaneo de puertos")
    time.sleep(1)
    while True:
        dominio = input("Ingresa la dirección: ")
        if dominio.lower() == 'volver':
            break

        comando = f"python escaneo_puertos.py -t {dominio}"
        ejecutar_comando(comando)
        print("Comando ejecutado. Puedes ingresar otra dirección o escribir 'volver'.")

def ejecutar_opcion(opcion):
    if opcion == '1':
        encontrar_ip_socket()
    elif opcion == '2':
        comando_cli()
    elif opcion == '3':
        banner_grabbing()
    elif opcion == '4':
        escaneo_puertos()
    elif opcion == '0':
        print("Saliendo del menú...")
        time.sleep(1)
    else:
        print("Opción no válida. Por favor, elige de nuevo.")

def menu():
    opcion = ''
    while opcion != '0':
        mostrar_menu()
        opcion = input("Elige una opción: ")
        ejecutar_opcion(opcion)

if __name__ == "__main__":
    menu()