def sort(vec):
    for i in range(len(vec)):
        for j in range(len(vec)-1) :
            if vec[j+1] > vec[j]:
                aux = vec[j]
                vec[j] = vec[j+1]
                vec[j+1] = aux

    return vec

def triangle_type(A,B,C):
    if(A >= B+C):
        print(f"NAO FORMA TRIANGULO")
        return
    if(A**2 == (B**2 + C**2)):
        print(f"TRIANGULO RETANGULO")
    if(A**2 > (B**2 + C**2)):
        print(f"TRIANGULO OBTUSANGULO")
    if(A**2 < (B**2 + C**2)):
        print(f"TRIANGULO ACUTANGULO")
    if A == B == C: 
        print(f"TRIANGULO EQUILATERO")
    if (A == B and A != C) or (A == C and A != B) or (B == C and B != A):
        print(f"TRIANGULO ISOSCELES")

entry = input().split()

vec = [float(entry[0]), float(entry[1]), float(entry[2])]

sort(vec)

triangle_type(vec[0], vec[1], vec[2])