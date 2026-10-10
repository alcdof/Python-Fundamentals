l1 = []
count_even = 0

for i in range(7):
    l1.append(int(input(f"Value {i+1}: ")))
    if l1[i] % 2 == 0:
        count_even += 1

even_percentual = count_even / 7 
odd_percentual = (7-count_even) / 7 

print(f"Even: {even_percentual * 100:.1f}%, Odd: {odd_percentual * 100:.1f}%")