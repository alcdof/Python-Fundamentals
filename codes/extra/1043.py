def conditionA(A, B, C):
    if (A+B) > C:
        return 1

def conditionB(A, B, C):
    if(A+C) > B:
        return 1

def conditionC(A, B, C):
    if (B+C) > A:
        return 1

entry = input().split()

n1 = float(entry[0])
n2 = float(entry[1])
n3 = float(entry[2])

if conditionA(n1, n2, n3) and conditionB(n1, n2, n3) and conditionC(n1, n2, n3):
    print(f"Perimetro = {n1+n2+n3}")
else:
    print(f"Area = {(n1+n2) * n3 / 2}")
