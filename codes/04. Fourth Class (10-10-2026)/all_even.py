l1 = []
N = int(input())
flag = 0

for i in range(N):
    l1.append(int(input("Type a number: ")))
    if l1[i] % 2 == 0:
        flag = 1
    else:
        flag = 0

if flag:
    print("All numbers on the list are even.")
else:
    print("Not all the numbers on the list are even.")