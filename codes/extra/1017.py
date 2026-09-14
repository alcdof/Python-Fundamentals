consumption = 12 # km/l

spent_time = int(input()) # h
average_speed = int(input()) # km / h

distance = average_speed * spent_time # km
fuel_amount = distance / consumption

print(f"{fuel_amount:.3f}")
