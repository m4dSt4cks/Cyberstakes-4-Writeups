from pwn import *

enc_part1 = "Drterc7Txsr7~d-7"
enc_part2 = "Vm0:damKhgn`Ihoj"
key = "0123456789012345"

result = ""
for c in enc_part1:
	result += chr(ord(c) ^ 0x17)

for c in enc_part2:
	result += chr(ord(c) ^ 3)
# print(result)

r = remote("challenge.acictf.com", 21045)
r.sendline(result)
r.interactive()
