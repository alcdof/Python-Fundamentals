original_A = []
dobrados_B = []

for i in range(5):
    original_A.append(int(input(f"Valor {i+1}: ")))
    dobrados_B.append(2*original_A[i])

print(f"Original A: {original_A}")
print(f"Dobrados B: {dobrados_B}")
