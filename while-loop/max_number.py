import sys

n = int(input())
counter = 0
max_number = -sys.maxsize - 1

while n > counter:
    number = int(input())
    if number > max_number:
        max_number = number
    counter += 1

print(f'{max_number}')