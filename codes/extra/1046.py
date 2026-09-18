entry = input().split()

start = int(entry[0])
end = int(entry[1])

if start > end: # passou da meia noite
    total = 24-start + end
else:
    if start < end: # nao passou da meia noite
        total = end - start
    if start == end:
        total = 24
        
print(f"O JOGO DUROU {total} HORA(S)")

