# Challenge 2 (Too much Resistance) solution

after looking through the files, i notice that the flag was encrypted using RSA with a modulus n reused across 5 different 512-bit public exponents and the encryption applies each exponent sequentially, equivalent to raising the flag to the product of all exponents modulo n

- given the private key (n, d), where d is the inverse of e = 65537 modulo φ(n), i can compute φ(n) indirectly
- i can compute K = 65537 * d - 1, which is a multiple of φ(n)
- the product of the 5 public exponents E is required to find its inverse modulo φ(n)

to decrypt, i need to calculate E as the product of all five public exponents, compute d', the modular inverse of E modulo K (equivalent to modulo φ(n)) and decrypt using d' to reverse the exponentiation.

so i write this code which:
1. computes E: multiplies all five public exponents to get the combined exponent used in encryption
2. calculates K: using the private key's d, compute K = 65537 * d - 1, which is a multiple of φ(n)
3. finds inverse d': computes the modular inverse of E modulo K, which gives the decryption exponent modulo φ(n).
4. decrypts the flag: uses d' to decrypt the ciphertext by raising it to d' modulo n, then convert the resulting integer back to bytes to reveal the flag, which is `LNC24{1_n33d_m0r3_buLL3ts}`!