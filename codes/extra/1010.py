entry_1 = input().split()

code_1 = int(entry_1[0])
unit_1 = int(entry_1[1])
price_1 = float(entry_1[2])

entry_2 = input().split()

code_2 = int(entry_2[0])
unit_2 = int(entry_2[1])
price_2 = float(entry_2[2])

total = (unit_1 * price_1) + (unit_2 * price_2)

print(f"VALOR A PAGAR: R$ {total:.2f}")