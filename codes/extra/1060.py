entry = []

for _ in range(6):
    value = float(input())
    entry.append(value)

cont = 0

for n in entry:
    if n > 0.0:
        cont += 1

print(f"{cont} valores positivos")