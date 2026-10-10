originais = [2, 3, 5, 13, 17, 19, 23, 29, 43, 47]

print("Originais:", originais)

i = 0
num = int(input())

while(originais[i] < num):
    i += 1

originais.insert(i, num);

print(originais)