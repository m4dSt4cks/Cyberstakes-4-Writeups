import binascii
from pwn import *

r = remote("challenge.acictf.com", 8818)

r.recvuntil(": ")
enc_flag = r.recvline().rstrip()
ct = int(enc_flag)

r.sendline("KEY:")
r.recvuntil(":")
n = int(r.recvline().rstrip())
r.recvuntil(":")
e = int(r.recvline().rstrip())

mul = pow(2, e, n)
inp = ct * mul % n

r.sendline("RECV:{}".format(inp))
r.recvline()
flag = int(r.recvline().rstrip()) / 2
print(binascii.unhexlify(hex(flag).rstrip("L").lstrip("0x")))

# https://masterpessimistaa.wordpress.com/2018/03/04/pragyan-ctf-rsas-quest/
# https://en.wikipedia.org/wiki/RSA_(cryptosystem)#Padding
