N = int(input())
M = int(input())

mat = [['.' for _ in range(N)] for _ in range (M)]

print(mat)

for linha in mat:
    print(' '.join(linha))