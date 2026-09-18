entry = input().split()

x = float(entry[0])
y = float(entry[1])

# primeiro quadrante: x, y maiores que 0
# segundo quadrante: y maior q 0, x menor q 0
# terceiro quadrante: x,y menores que 0
# quarto quadrante: y menor que 0, x maior que 0

if x == 0 and y == 0:
    print(f"Origem")
else:
    if x > 0: # x maior que zero
        if y > 0: # y maior que 0
            print(f"Q1")
        else:
            if y < 0: # y menor que 0
                print(f"Q4")
            else: # y = 0
                print("Eixo X")
    else:
        if x < 0: # x menor que 0
            if y > 0: # y maior que 0
                print(f"Q2")
            else:
                if y < 0: # y menor que 0
                    print(f"Q3")
                else: # y = 0
                    print(f"Eixo X")
        else: # x = 0
            print(f"Eixo Y")
