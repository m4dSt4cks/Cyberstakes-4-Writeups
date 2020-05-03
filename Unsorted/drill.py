from pwn import *
import time

# Get the core dump
core = Coredump("./core")
# print(core.mappings)

rdi = core.rdi 
rsp = core.rsp 
rsp_next = core.rsp + 8
print(core.exe[rdi:rdi+32])
print(core.stack[rsp:rsp+8])
key_addr = u64(core.stack[rsp_next:rsp_next+8])
print(hex(rdi), hex(key_addr))
print(core.heap[key_addr:key_addr])
# print(core.argc)
# string_at_rax = core.stack[rax:rax+26]
# print("string: {}".format(string_at_rax))



# gdb drill core
# replace our string with theirs, make sure to set rdx somewhere we can write
# ISVCIRIPLQIOXJUMXMWQFMSXAFWMHIQ
# set rdi on function exit
