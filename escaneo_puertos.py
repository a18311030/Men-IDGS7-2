import socket
import sys
import argparse
from os import path

# Configuración del parser de argumentos
parser = argparse.ArgumentParser(description="Script para buscar puertos.")
parser.add_argument('-t', '--target', help='Indica el dominio objetivo', required=True)
args = parser.parse_args()

def main():
    # Verificar si el archivo 'puertos.txt' existe
    if not path.exists('puertos.txt'):
        print("El archivo 'puertos.txt' no existe.")
        return

    with open('puertos.txt', 'r') as wordlist:
        puertos = wordlist.read().splitlines()

    # Comprobar si la lista de puertos está vacía
    if not puertos:
        print("No hay puertos disponibles en 'puertos.txt'.")
        return

    # Iterar sobre cada puerto en la lista
    for puerto in puertos:
        # Validar que el puerto sea un número válido
        if not puerto.isdigit():
            print(f"El puerto '{puerto}' no es válido. Se omitirá.")
            continue

        puerto_numero = int(puerto)

        # Validar que el puerto esté en el rango permitido
        if puerto_numero < 1 or puerto_numero > 65535:
            print(f"El puerto '{puerto}' está fuera del rango permitido (1-65535). Se omitirá.")
            continue

        # Intentar conectarse al puerto
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(5)
        resultado = s.connect_ex((args.target, puerto_numero))

        # Comprobar si el puerto está abierto
        if resultado == 0:
            print(f"El puerto {puerto} está abierto.")
        else:
            print(f"El puerto {puerto} está cerrado.")

        # Cerrar el socket
        s.close()

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nPrograma interrumpido por el usuario.")
        sys.exit()
    except Exception as e:
        print(f"Ocurrió un error inesperado: {e}")
        sys.exit(1)