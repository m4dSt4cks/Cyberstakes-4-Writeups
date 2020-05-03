# pcode2code chall/word/vbaProject.bin -o results.txt
import base64


def determine_original(enc):
	results = []
	for i in range(128):
		if enc == ((i * 16) % 256) + (i / 16):
			results.append(i)
	if len(results) != 1:
		print("Got {} results!".format(len(results)))
	return results[0]


enc = "NmgvUlt8glilwTJa1vHPVfuIKUKY/dBIT2DZSlN0004="
# open it in word, go to view->macros->edit, insert message box to see alt 3
enc = "a2nACT4I8F2MtM0NdBX7CWVJ/xg5DeARKhHYEcu3+2I="

temp = base64.b64decode(enc)[::-1]
dec = []
for i, c in enumerate(temp):
	dec.append(ord(c) ^ ((32 + i + 1) % 256))

for i in range(len(dec) - 1, -1, -1):
	modarg = i % 4
	if modarg == 0:
		dec[i] = (dec[i] + 104) % 256
	elif modarg == 1:
		temp = dec[i]
		dec[i] = dec[i - 1]
		dec[i - 1] = temp
	elif modarg == 2:
		dec[i] = determine_original(dec[i])
	else:
		dec[i] = dec[i] ^ dec[i - 1]

print("".join([chr(c) for c in dec]))


"""
Encryption function in python

plain = ""
cipher = []
for i in range(len(plain)):
	cipher.append(ord(plain[i]))
for i in range(len(plain)):
	modarg = i % 4
	if modarg == 0:
		cipher[i] = (cipher[i] - 104 + 256) % 256
	elif modarg == 1:
		temp = cipher[i]
		cipher[i] = cipher[i - 1]
		cipher[i - 1] = temp
	elif modarg == 2:
		cipher[i] = ((cipher[i] * 16) % 256) + (cipher[i] / 16)
	else:
		cipher[i] = cipher[i - 1] ^ cipher[i]
"""
