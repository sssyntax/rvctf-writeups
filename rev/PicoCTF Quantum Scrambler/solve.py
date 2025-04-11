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
    load_and_decode(sys.argv[1])

