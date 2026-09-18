entry = input().split()

A = int(entry[0])
B = int(entry[1])

if A == 0 or B == 0:
    print(f"Sao Multiplos")
else:
    if B % A == 0 or A % B == 0:
        print(f"Sao Multiplos")
    else:
        print(f"Nao sao Multiplos")
