import numpy as np

def MaiorAB(a, b):
    maior = (a+b + np.absolute(a-b))/2

    return int(maior)

entry = input().split()

A = int(entry[0])
B = int(entry[1])
C = int(entry[2])
# print(f"A: {A}\t B: {B}\t C: {C}")

maior_de_todos = MaiorAB(MaiorAB(A,B), C)

print(f"{maior_de_todos} eh o maior")
