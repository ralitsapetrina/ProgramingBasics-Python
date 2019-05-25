n = int(input())

p1 = 0
p2 = 0
p3 = 0
p4 = 0
p5 = 0

for num in range(n):
    number = int(input())
    if number < 200:
        p1 += 1
    elif number >= 200 and number <= 399:
        p2 += 1
    elif number >= 400 and number <= 599:
        p3 += 1
    elif number >= 600 and number <= 799:
        p4 += 1
    elif number >= 800 and number <= 1000:
        p5 += 1

print(f'{(p1 / n * 100):.2f}%')
print(f'{(p2 / n * 100):.2f}%')
print(f'{(p3 / n * 100):.2f}%')
print(f'{(p4 / n * 100):.2f}%')
print(f'{(p5 / n * 100):.2f}%')