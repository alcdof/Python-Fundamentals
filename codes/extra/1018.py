A = int(input())

notas_100 = A // 100
notas_50 = (A % 100) // 50
notas_20 = ((A % 100) % 50) // 20
notas_10 = (((A % 100) % 50) % 20) // 10
notas_5 = ((((A % 100) % 50) % 20) % 10) // 5
notas_2 = (((((A % 100) % 50) % 20) % 10) % 5) // 2
notas_1 = ((((((A % 100) % 50) % 20) % 10) % 5) % 2) // 1

print(f"{notas_100} notas de 100")
print(f"{notas_50} notas de 50")
print(f"{notas_20} notas de 20")
print(f"{notas_10} notas de 10")
print(f"{notas_5} notas de 5")
print(f"{notas_2} notas de 2")
print(f"{notas_1} notas de 1")
