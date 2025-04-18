# quantum scrambler solution
first, i put the output into an output.txt file;
```nc verbal-sleep.picoctf.net 54825 > output.txt```

then i code up these functions to reverse the scrambled data and decode it;

```
import sys

def unscramble(L):
    A = L
    i = len(A) - 1
    while i >= 2:
        A[i - 1].pop()
        n = len(A[i - 1])
        restored = A[i - 2][-n:]
        A[i - 2] = A[i - 2][:-n]
        A.insert(i - 1, restored)
        i -= 1
    return L

def load_and_decode(file_path):
    with open(file_path, 'r') as f:
        scrambled = eval(f.read())
    hex_data = unscramble(scrambled)
    for item in hex_data:
        print(chr(int(item[0], 16)), end='')

if __name__ == "__main__":
    load_and_decode(sys.argv[1]) # take the first command-line argument and use it as the file path to read and decode the scrambled flag
```

then you get the flag: ```picoCTF{python_is_weird63e6d9bb}```!