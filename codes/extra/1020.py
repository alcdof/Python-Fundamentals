total = int(input())

years = total // 365
months = (total % 365) // 30
days = (total % 365) % 30

print(f"{years} ano(s)\n{months} mes(es)\n{days} dia(s)")