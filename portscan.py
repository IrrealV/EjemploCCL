import socket

# Dirección IP que deseas escanear
target_ip = "127.0.0.1"

# Rango de puertos que deseas escanear (ejemplo: del puerto 1 al 1024)
start_port = 1
end_port = 1024

def scan_port(ip, port):
    try:
        # Crear un objeto de socket TCP
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)  # Establecer un tiempo de espera para la conexión

        # Intentar conectar al puerto en la dirección IP
        result = sock.connect_ex((ip, port))

        # Comprobar si la conexión tuvo éxito
        if result == 0:
            print(f"Puerto {port} abierto")
        else:
            print(f"Puerto {port} cerrado")

        # Cerrar el socket
        sock.close()
    
    except KeyboardInterrupt:
        print("Escaneo interrumpido.")
        exit()
    
    except socket.error:
        print("No se pudo conectar al servidor.")
        exit()

# Escanear los puertos en el rango especificado
for port in range(start_port, end_port + 1):
    scan_port(target_ip, port)

