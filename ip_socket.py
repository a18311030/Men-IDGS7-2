import argparse
import socket

# Definir el argumento para la URL
parse = argparse.ArgumentParser()
parse.add_argument("-t", "--target", help="Ingresa la URL sin HTTP")
parse = parse.parse_args()

# Función para obtener la IP de una URL
def getIpLokochon(url):
    try:
        ip = socket.gethostbyname(url)
        print(f"La dirección IP de {url} es: {ip}")
    except socket.gaierror:
        print("No se pudo obtener la IP. Verifique la URL o la conexión.")

# Función principal
def main():
    if parse.target:
        getIpLokochon(parse.target)
    else:
        print("Ingrese una dirección URL válida sin HTTP.")

# Ejecutar la función principal
if __name__ == "__main__":
    main()