lines = 8
columns = 8

mat = [['.' for _ in range(lines)] for _ in range(columns)]


mat[0] = ['t', 'c', 'b', 'q', 'k', 'b', 'c', 't']
mat[1] = ['p', 'p', 'p', 'p', 'p', 'p', 'p', 'p']
mat[6] = ['p', 'p', 'p', 'p', 'p', 'p', 'p', 'p']
mat[7] = ['T', 'C', 'B', 'Q', 'K', 'B', 'C', 'T'] 

for k in mat:
    print(' '.join(k))

print('\nremovendo o cavalo\n')

mat[0][1] = '.'

for k in mat:
    print(' '.join(k))
