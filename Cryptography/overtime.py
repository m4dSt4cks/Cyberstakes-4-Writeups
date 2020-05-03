import binascii

enc_first = "29886da3a932781863cadbd0599da271a5d8ef950be2791588d6ff7647d956d3a406406026866b37e91e96efc76e3da869be1d4c5e1af01dc88289f954d29c51"
enc_first_bytes = binascii.unhexlify(enc_first)
plain_first = "The following encoded individuals are to be given a $27.3k bonus:".ljust(63) + "\n"
enc_last = "5dea02c28c146f106a8bd387588da429f0d5b99659f1204fd98cbd7913c9048ce1155c3263863f78e95cd3ef80276bed27be5c4c5a08e713dbc989bb1b9cc902"
enc_bytes_last = binascii.unhexlify(enc_last)

flag = ""
for i in range(64):
	flag += (chr(ord(enc_first_bytes[i]) ^ ord(plain_first[i]) ^ ord(enc_bytes_last[i])))
print(flag)
