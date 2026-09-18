prices = [4.00, 4.50, 5.00, 2.00, 1.50]

entry = input().split()

code = int(entry[0])
amount = int(entry[1])

total = amount * prices[code-1]

print(f"Total: R$ {total:.2f}")