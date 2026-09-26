year = int(input())

if year < 1582:
  print("Not within the Gregorian calendar period")
else:
    if year % 4 == 0:
       print("Leap Year")
    else:
       print("Common Year")
       
 