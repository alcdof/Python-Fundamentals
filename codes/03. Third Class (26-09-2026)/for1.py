num = int(input())

for n in range(1, 11):
    print(f"{num} x {n:>2} = {num*n:>2}")

print()

for n in range(1, 11):
    print("%d X %2d = %2d" % (num, n, num*n))