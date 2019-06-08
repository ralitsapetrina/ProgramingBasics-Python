import sys

n = int(input())
counter = 0
min_number = sys.maxsize

while n > counter:
    number = int(input())
    if number < min_number:
        min_number = number
    counter += 1

print(f'{min_number}')