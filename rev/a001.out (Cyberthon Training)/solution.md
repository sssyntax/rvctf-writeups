# solution for a001.out

[a001.jpg](rev/a001.out (Cyberthon Training)/a001.out.jpeg)

first, i put the file into ghidra. 

i found some string containing curly braces, which i believed was the flag;
```
    "K0A8nglgoHG0n8V3nusG7LXBOZcVMy0C5nriszw7{sEQYmMXykCXuT3bCPBXcGaRURLgxfFxksEEoHhImgAvpa2wXJyiUoVCuaP9wMJQp9EzY4HRHZBvDkEaQOYIRF}"
    "hlqn69a53TaPf1uH4s77Mo5H5h2dmgkXlSvq1ZUQCvb3gwI24Ja1EBR13QZp0X50tx5BNq3gWz5e9NMScEje9o8LJmG3rFVYnKQkiqzXdeCyL3RQZXr24FQFTuZeIWSoE"
```

i also found this strange function; 
```
int32_t main(int32_t argc, char** argv, char** envp)
{
    puts("\n>rb<");
    printf("PROVIDE KEY? ");
    fflush(*stdout);
    scanf(&data_1950, &data_20008);
    printf(&data_1958);
    uint32_t x0_2 = sub_1320();
    
    for (int32_t i = 0; i < x0_2; i += 1)
        sub_1320();
    
    for (int32_t i_1 = 0; i_1 <= 0x17; i_1 += 1)
        putchar(*std::string::operator[](&data_20050, sub_1320()));
    
    puts(" < \n");
    fflush(*stdout);
    return 0;
}
```

i looked into it, and i realised it was definitely xoring something. so i ran it through chatgpt to get me a xorshift32 function in python, and i didn't know the seed so i had to brute force it. this code brute forces seeds until it gets the correct one.

```
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

if name == "main":
    brute_force()
```

and after it ran for a bit, i finally got the flag, which is:
```Cyberthon{C7oRaXxKIMs7T}```