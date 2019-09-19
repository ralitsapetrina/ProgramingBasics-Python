days = int(input())
hours = int(input())

total = 0

for day in range(1, days + 1):
    pay = 0
    for hours in range(1, hours + 1):
        if day % 2 == 0 and hours % 2 != 0:
            pay += 2.5
        elif day % 2 != 0 and hours % 2 == 0:
            pay += 1.25
        else:
            pay += 1

    total += pay
    print(f'Day: {day} - {pay:.2f} leva')

print(f'Total: {total:.2f} leva')
