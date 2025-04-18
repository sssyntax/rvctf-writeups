# Challenge 3 (Bitwise) solution

for each character i in the flag, the code:
1. computes the ASCII value using ord(i)
2. applies bitwise NOT (~), which in Python is equivalent to -ord(i) - 1
3. shifts the result left by 7 bits (multiplying by 128)
4. XOR this shifted value with ~9 (which equals -10)
5. converts the resulting integer to a string and append it to the output list

therefore, in order to recover the original flag from the output list, i have to:
1. convert each string back to an integer y
2. compute A = y ^ -10 (undo the XOR with -10)
3. solve for the original ASCII value using c = (- (A // 128)) - 1
4. convert strings to integers: the original output values were stored as strings
5. undo XOR with -10: the XOR operation is reversed using the same value (~9 = -10)
6. reverse the left shift: undo the << 7 operation with a right shift (>> 7)
7. undo bitwise NOT: the ~ operation is equivalent to -x - 1, so i reverse it with -x - 1

after all this, i get the flag `ictf{guess_1_4m_n0t_a_bit_wise}`!