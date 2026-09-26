password = 12345617

num = None
limit = 5
while num != password and limit > 0:
    num = float(input())
    limit = limit - 1
    if num == password:
        print("Access guaranteed.")
    else:
        print(f"Access denied. {limit} attempts remaining.")
    
