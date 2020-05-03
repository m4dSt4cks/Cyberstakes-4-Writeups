from pwn import *
import base64
import binascii


r = remote("challenge.acictf.com", 22667)

def convert(s, e, stuff):
	raw = ""
	if s == "raw":
		raw = stuff
	elif s == "b64":
		raw = base64.b64decode(stuff)
	elif s == "hex":
		raw = binascii.unhexlify(stuff)
	elif s == "dec":
		raw = binascii.unhexlify(hex(int(stuff, 10)).rstrip("L").lstrip("0x"))
	elif s == "oct":
		raw = binascii.unhexlify(hex(int(stuff, 8)).rstrip("L").lstrip("0x"))
	elif s == "bin":
		raw = binascii.unhexlify(hex(int(stuff, 2)).rstrip("L").lstrip("0x"))
	else:
		print("start method not found")

	res = ""
	if e == "raw":
		res = raw.encode("utf-8")
	elif e == "b64":
		res = base64.b64encode(raw)
	elif e == "hex":
		res = binascii.hexlify(raw).rstrip("L")
	elif e == "dec":
		res = str(int(binascii.hexlify(raw), 16))
	elif e == "oct":
		res = str(oct(int(binascii.hexlify(raw), 16))).lstrip("0").rstrip("L")
	elif e == "bin":
		res = bin(int(binascii.hexlify(raw), 16)).lstrip("0b")
	else:
		print("end method not found")

	return res

for i in range(500):
	r.recvuntil("--")
	r.recvline()
	conversion = r.recvline().rstrip().split(" -> ")
	start = conversion[0]
	end = conversion[1]
	stuff = r.recvline().rstrip()
	resp = convert(start, end, stuff)

	print("{} Converting {} to {}\nOriginal: {}\nConverted: {}\n".format(i, start, end, stuff, resp))
	r.recvuntil("answer: ")
	r.sendline(resp)

r.interactive()
