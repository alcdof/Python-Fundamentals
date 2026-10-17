l1 = []
N = int(input())

for i in range(N):
    l1.append(int(input("Type a number: ")))

print(l1)
print(f"{min(l1)} is the smallest number. {max(l1)} is the biggest number.")
