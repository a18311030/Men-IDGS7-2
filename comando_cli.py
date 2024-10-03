import sys
import argparse
import subprocess

# Definir y obtener los argumentos
parse = argparse.ArgumentParser()
parse.add_argument('-t', '--target', help='Introduce la dirección IP o dominio de la víctima')
parse = parse.parse_args()

# Función para obtener la ip con nslookup
def get_ip(target):
    try:
        # Usar subprocess para capturar la salida de nslookup
        res = subprocess.run(['nslookup', target], capture_output=True, text=True)
        print(res.stdout)
    except subprocess.CalledProcessError as e:
        print('[-] No se pudo obtener la IP')
        print(f"Detalles: {e}")
        sys.exit(1)

# Función principal
def main():
    if parse.target:
        get_ip(parse.target)
    else:
        print('[-] Debes indicar una dirección IP o dominio')
        sys.exit(1)

# Punto de entrada del programa
if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n[!] Programa interrumpido por el usuario.")
        sys.exit(0)
