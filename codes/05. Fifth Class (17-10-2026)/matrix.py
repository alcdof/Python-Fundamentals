N = int(input())
M = int(input())

mat = [['.' for _ in range(N)] for _ in range (M)]
mat2 = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
mat3 = []
for i in range(N):
    mat[i].append('a'*3)

print(mat)

for lines in mat:
    print(' '.join(lines))
print()

for lines in mat3:
    print(' '.join(lines))