l1 = []
count_even = 0

N = int(input())

for i in range(N):
    l1.append(int(input(f"Value {i+1}: ")))
    if l1[i] % 2 == 0:
        count_even += 1

even_percentual = count_even / N 
odd_percentual = (N-count_even) / N 

print(f"Even: {even_percentual * 100:.1f}%, Odd: {odd_percentual * 100:.1f}%")