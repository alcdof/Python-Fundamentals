age = int(input())

if age == 0:
    print("Recém Nascido")
elif age >= 1 and age <= 12:
    print("Criança")
elif age >= 13 and age <= 18:
    print("Adolescente")
elif age >= 19 and age <= 60:
    print("Adulto")
elif age >= 61 and age <= 80:
    print("Idoso")
elif age > 80:
    print("Longevo")
else:
    print("Idade inválida")
