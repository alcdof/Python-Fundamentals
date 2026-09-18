total = float(input())

#   TODO: refatorar esse código, ficou muito grande. preciso achar
#         um jeito de automatizar esses cálculos, usando alguma 
#         estrutura de repetição. Mas tá funcionando. Feio, mas funcionando.

notas_100 = total // 100
notas_50 = (total % 100) // 50
notas_20 = ((total % 100) % 50) // 20
notas_10 = (((total % 100) % 50) % 20) // 10
notas_5 = ((((total % 100) % 50) % 20) % 10) // 5
notas_2 = (((((total % 100) % 50) % 20) % 10) % 5) // 2
moedas_1 = ((((((total % 100) % 50) % 20) % 10) % 5) % 2) // 1
moedas_50 = (((((((total % 100) % 50) % 20) % 10) % 5) % 2) % 1) // 0.5
moedas_25 = ((((((((total % 100) % 50) % 20) % 10) % 5) % 2) % 1) % 0.5) // 0.25
moedas_10 = (((((((((total % 100) % 50) % 20) % 10) % 5) % 2) % 1) % 0.5) % 0.25) // 0.10
moedas_05 = ((((((((((total % 100) % 50) % 20) % 10) % 5) % 2) % 1) % 0.5) % 0.25) % 0.10) // 0.05
moedas_01 = (((((((((((total % 100) % 50) % 20) % 10) % 5) % 2) % 1) % 0.5) % 0.25) % 0.10) % 0.05) // 0.01

print(f"NOTAS:")
print(f"{int(notas_100)} notas de 100")
print(f"{int(notas_50)} notas de 50")
print(f"{int(notas_20)} notas de 20")
print(f"{int(notas_10)} notas de 10")
print(f"{int(notas_5)} notas de 5")
print(f"{int(notas_2)} notas de 2")
print(f"MOEDAS:")
print(f"{int(moedas_1)} moedas de 1")
print(f"{int(moedas_50)} moedas de 0.50")
print(f"{int(moedas_25)} moedas de 0.25")
print(f"{int(moedas_10)} moedas de 0.10")
print(f"{int(moedas_05)} moedas de 0.05")
print(f"{int(moedas_01)} moedas de 0.01")

