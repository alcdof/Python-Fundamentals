A = input()
B = input()
C = input()

if A == "vertebrado":
    if B == "ave":
        if C == "carnivoro":
            print(f"aguia")
        if C == "onivoro":
            print(f"pomba")
    if B == "mamifero":
        if C == "onivoro":
            print(f"homem")
        if C == "herbivoro":
            print(f"vaca")

if A == "invertebrado":
    if B == "inseto":
        if C == "hematofago":
            print(f"pulga")
        if C == "herbivoro":
            print(f"lagarta")
    if B == "anelideo":
        if C == "hematofago":
            print(f"sanguessuga")
        if C == "onivoro":
            print(f"minhoca")


