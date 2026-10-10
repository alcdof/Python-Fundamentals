l = []
N = int(input())

for i in range(N):
    l.append(int(input("Type a value: ")))

print(l)

for j in range(len(l)):
    if l[j] % 2 != 0:
        print("Nem todos os elementos informados são pares!")
        break
    else:  
        print("Todos os elementos informados são pares!")
        break