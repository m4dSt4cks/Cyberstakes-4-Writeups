from pwn import *
import string

def create_firmware(r, vin, name="", flash="y"):
	r.sendline("1")
	res = r.recvline()
	r.sendline(vin)
	res = r.recvline()
	r.sendline(name)
	res = r.recvline()
	r.sendline(flash)
	r.recvline()
	res = r.recvline()
	if "Succesfully" in res:
		r.recvuntil("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
		r.recvuntil("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
		r.recvline()
		return 0
	else:
		start = res.index("(")
		stop = res.index("bytes)")
		r.recvuntil("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
		r.recvuntil("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
		r.recvline()
		return int(res[start+1:stop-1])
		


r = remote("challenge.acictf.com", 54852)
r.recvuntil("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
r.recvuntil("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
r.recvline()
alphabet = "_" + string.ascii_lowercase + string.ascii_uppercase + string.digits

vin = "8" * 17
flag = ""
for index in range(64):
	shortest = 5000
	shortest_c = ""
	for c in alphabet:
		length = create_firmware(r, vin, ("{" * 1000 + "::Vin:{}::DeviceKey:{}{}".format(vin, flag, c)))
		# print(c, length)
		if length < shortest:
			shortest = length
			shortest_c = c
			if length == 237:
				break
	if shortest > 237:
		print("No letter found for index {} :(".format(index))
		exit()
	else:
		print("Found {}".format(shortest_c))
		flag += shortest_c
		print(flag)
print(flag)
