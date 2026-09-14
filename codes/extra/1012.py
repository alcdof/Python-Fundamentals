pi = 3.14159

entry = input().split()
A = float(entry[0])
B = float(entry[1])
C = float(entry[2])

a_1 = (A*C)/2
a_2 = pi * C**2
a_3 = (A+B) * C / 2
a_4 = B**2
a_5 = A*B

print(f"TRIANGULO: {a_1:.3f}")
print(f"CIRCULO: {a_2:.3f}")
print(f"TRAPEZIO: {a_3:.3f}")
print(f"QUADRADO: {a_4:.3f}")
print(f"RETANGULO: {a_5:.3f}")