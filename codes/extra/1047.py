entry = input().split()

startHour = int(entry[0])
startMinute = int(entry[1])
endHour = int(entry[2])
endMinute = int(entry[3])

totalHours =  endHour - startHour
totalMinutes = endMinute - startMinute

if totalMinutes < 0:
    totalHours = totalHours - 1
    totalMinutes = totalMinutes + 60
if totalHours < 0:
    totalHours = totalHours + 24
if totalHours == 0 and totalMinutes == 0:
    totalHours = 24

print(f"O JOGO DUROU {totalHours} HORA(S) E {totalMinutes} MINUTO(S)")