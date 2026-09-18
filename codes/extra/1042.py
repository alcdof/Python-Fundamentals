entry = input().split()

vecOri = [int(entry[0]), int(entry[1]), int(entry[2])]
vec = [int(entry[0]), int(entry[1]), int(entry[2])]

for i in range(len(vec)):
    for j in range(len(vec)-1) :
        if vec[j+1] < vec[j]:
            aux = vec[j]
            vec[j] = vec[j+1]
            vec[j+1] = aux

print(f"{vec[0]}\n{vec[1]}\n{vec[2]}")
print(f"\n{vecOri[0]}\n{vecOri[1]}\n{vecOri[2]}")