import socket
import sys

def banner_grabbing(dominio, puerto):
    try:
        # Crear el socket
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        
        # Conectar al dominio y puerto
        sock.connect((dominio, int(puerto)))
        sock.settimeout(5)
        
        # Recibir el banner
        banner = sock.recv(1024)
        
        # Mostrar el banner
        print(f"Banner recibido desde {dominio}:{puerto}:\n{banner.decode().strip()}")
    
    except socket.timeout:
        print(f"Timeout: No se pudo recibir el banner desde {dominio}:{puerto}.")
    
    except Exception as e:
        print(f"Error al conectar con {dominio}:{puerto}. Detalles: {e}")
    
    finally:
        sock.close()

if __name__ == "__main__":
    # Validar el número de argumentos
    if len(sys.argv) != 5:
        print("Uso: python banner_grabing.py -t <dominio> -p <puerto>")
        sys.exit(1)
    
    # Inicializar variables para el dominio y puerto
    dominio = ""
    puerto = 0
    
    try:
        # Procesar los argumentos para obtener el dominio y el puerto
        for i in range(len(sys.argv)):
            if sys.argv[i] == "-t":
                dominio = sys.argv[i+1]
            elif sys.argv[i] == "-p":
                puerto = int(sys.argv[i+1])  # Asegurar que el puerto sea un entero válido
        
        # Validar que el dominio y puerto hayan sido proporcionados
        if not dominio or not puerto:
            raise ValueError("Debes especificar un dominio y un puerto válidos.")

        # Llamar a la función de banner grabbing
        banner_grabbing(dominio, puerto)
    
    except ValueError as ve:
        print(f"Error: {ve}")
        sys.exit(1)
    
    except Exception as e:
        print(f"Error inesperado: {e}")
        sys.exit(1)