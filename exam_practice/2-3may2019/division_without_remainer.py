numbers = int(input())
p1 = 0
p2 = 0
p3 = 0

for n in range(numbers):
    num = int(input())

    if num % 2 == 0:
        p1 += 1
    if num % 3 == 0:
        p2 += 1
    if num % 4 == 0:
        p3 += 1

p1 = 100 / numbers * p1
p2 = 100 / numbers * p2
p3 = 100 / numbers * p3

print(f'{p1:.2f}%\n{p2:.2f}%\n{p3:.2f}%')