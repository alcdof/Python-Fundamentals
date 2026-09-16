entry = input().split()

A = int(entry[0])
B = int(entry[1])
C = int(entry[2])
D = int(entry[3])

# TODO: Refatorar, não gostei de como as coisas ficaram aqui.

if B > C:
    if D > A:
        if (C+D > A+B):
            if C > 0:
                if D > 0:
                    if (A % 2 == 0):
                        print(f"Valores aceitos")
                    else:
                        print(f"Valores nao aceitos")
                else:
                    print(f"Valores nao aceitos")
            else:
                print(f"Valores nao aceitos")
        else:
            print(f"Valores nao aceitos")
    else:
        print(f"Valores nao aceitos")
else:
    print(f"Valores nao aceitos")