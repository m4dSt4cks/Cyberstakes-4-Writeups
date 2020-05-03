import string
import requests
import binascii

BLOCKSIZE = 16
BLOCKSIZE_MINUS = BLOCKSIZE - 1

def encrypt_stuff(PT):
	# put the method for encrypting the input here
	cookies = {"session":"eyJjc3JmX3Rva2VuIjoiYzJlMDg5YzliN2Y1ZWM0NWU3YTU5YzY4YjIzZWNhMzIxN2U3ZmU4OCJ9.XqL9Kw.mlH35bPBJs_J6dlJSammPIw9Lb4"}
	params = {"username":PT,"password":"zamp"}	
	r = requests.post("http://challenge.acictf.com:57680/register", cookies=cookies, data=params)
	if r.status_code != 200:
		print("Status error: {}".format(r.status_code))
		exit()
	return binascii.unhexlify(r.cookies["auth_token"])
	
def get_blocks(CT):
	result = []
	for i in range(0, len(CT), BLOCKSIZE):
		result.append(CT[i:i+BLOCKSIZE])
	return result

blocks = []
offset = -1

last_block = 10
input_len = (BLOCKSIZE * last_block) + BLOCKSIZE_MINUS
blocks = get_blocks(encrypt_stuff("A" * input_len))
alphabet = string.ascii_uppercase + string.ascii_lowercase + string.digits + string.punctuation

secret = ""
for i in range(16):
	for guess in alphabet:
		offset = BLOCKSIZE - 1 - (len(secret) % 16)
		payload = (BLOCKSIZE * (last_block)) * "A" + "B" * offset + secret + guess + "B" * offset
		blocks = get_blocks(encrypt_stuff(payload))
		if blocks[last_block] == blocks[last_block + ((len(secret) / 16) + 1)]:
			print(i, guess)
			secret += guess
			print(secret)
			break

for i in range(1):
	for guess in alphabet:
		offset = BLOCKSIZE - 1 - (len(secret) % 16)
		payload = (BLOCKSIZE * (last_block)) * "A" + secret[(i + 1):] + guess + "B" * offset
		blocks = get_blocks(encrypt_stuff(payload))
		if blocks[last_block] == blocks[last_block + ((len(secret) / 16) + 1)]:
			print(i, guess)
			secret += guess
			print(secret)
			break



