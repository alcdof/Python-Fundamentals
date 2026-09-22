DDD = int(input())

match DDD:
    case 11:
        print(f"Sao Paulo")
    case 19: 
        print(f"Campinas")
    case 21:
        print(f"Rio de Janeiro")
    case 27:
        print(f"Vitoria")
    case 31:
        print(f"Belo Horizonte")
    case 32:
        print(f"Juiz de Fora")
    case 61:
        print(f"Brasilia")
    case 71:   
        print(f"Salvador")
    case _: 
        print(f"DDD nao cadastrado")

# no python 3.9 (que é o usado no beecrowd), não tem o match case.
# por isso, tem o arquivo 1050_v2.py
