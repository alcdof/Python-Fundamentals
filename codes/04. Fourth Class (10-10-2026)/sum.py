N = int(input())
A = []

for i in range(N):
    A.append(int(input((f"Value A[{i}]: "))))

x = int(input(f"X index (0-{N-1}): "))
y = int(input(f"Y index (0-{N-1}): "))

print(f"Sum of A[{x}] and A[{y}]: {A[x] + A[y]}")