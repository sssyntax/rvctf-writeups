POOL = (
    "K0A8nglgoHG0n8V3nusG7LXBOZcVMy0C5nriszw7{sEQYmMXykCXuT3bCPBXcGaRURLgxfFxksEEoHhImgAvpa2wXJyiUoVCuaP9wMJQp9EzY4HRHZBvDkEaQOYIRF}"
    "hlqn69a53TaPf1uH4s77Mo5H5h2dmgkXlSvq1ZUQCvb3gwI24Ja1EBR13QZp0X50tx5BNq3gWz5e9NMScEje9o8LJmG3rFVYnKQkiqzXdeCyL3RQZXr24FQFTuZeIWSoE"
)

def xorshift32(seed):
    while True:
        seed ^= (seed << 13) & 0xFFFFFFFF
        seed ^= (seed >> 17) & 0xFFFFFFFF
        seed ^= (seed << 5) & 0xFFFFFFFF
        yield seed & 0xFFFFFFFF

def decrypt(seed):
    prng = xorshift32(seed)
    skip = next(prng) & 0xFF
    for _ in range(skip):
        next(prng)

    out = ""
    for _ in range(24):
        index = next(prng) % len(POOL)
        out += POOL[index]
    return out

def brute_force(start=0, end=0xFFFFFFFF):
    for seed in range(start, end):
        result = decrypt(seed)
        print("[*] Trying seed:", seed)
        if "Cyberthon" in result:
            print(f"[+] Found! Seed: {seed}")
            print(f"    Flag: {result}")
            break
        if seed % 1000000 == 0:
            print(f"[*] Checked up to seed {seed}")

brute_force()