import string

# in GDB break at check address
# in GDB run source [this script]
# update addresses with actual values

alphabet = string.hexdigits + "}"
flag_length = 34
known = "ACI{"


while len(known) < flag_length:
	for letter in alphabet:
		guess = known + letter + ("_" * (flag_length - 1 - len(known)))
		gdb.execute("r < <(python -c \"print '" + guess + "'\")")
		enc_flag = str(gdb.parse_and_eval(hex(0x5555557576d0+len(known))).cast(gdb.lookup_type('char').pointer()).dereference())
		data_str = str(gdb.parse_and_eval(hex(0x5555557577d0+len(known))).cast(gdb.lookup_type('char').pointer()).dereference())
		if enc_flag == data_str:
			known += letter
			print(known)
print("Flag: {}".format(known))
