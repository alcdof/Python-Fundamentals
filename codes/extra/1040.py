scores = input().split()

n1 = float(scores[0])
n2 = float(scores[1])
n3 = float(scores[2])
n4 = float(scores[3])

media = (n1*2 + n2*3 + n3*4 + n4) / 10

print(f"Media: {media:.1f}")

if media >= 7.0:
    print("Aluno aprovado.")
elif media >= 5.0:
    print("Aluno em exame.")

    nRec = float(input())

    mediaNova = (media + nRec) / 2

    print(f"Nota do exame: {nRec:.1f}")

    if mediaNova >= 5.0:
        print("Aluno aprovado.")
        print(f"Media final: {mediaNova:.1f}")
    else:
        print("Aluno reprovado.")
        print(f"Media final: {mediaNova:.1f}")
else:
    print("Aluno reprovado.")