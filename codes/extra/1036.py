import numpy as np

entry = input().split()

A = float(entry[0])
B = float(entry[1])
C = float(entry[2])

right = B**2 - 4*A*C

if A == 0 or right < 0:
    print(f"Impossivel calcular")
else:
    r1 = (-B + np.sqrt(right)) / (2*A)
    r2 = (-B - np.sqrt(right)) / (2*A)
    print(f"R1 = {r1:.5f}")
    print(f"R2 = {r2:.5f}")


