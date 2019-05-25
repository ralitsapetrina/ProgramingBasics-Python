from sys import maxsize

n = int(input())

odd_sum = 0
odd_max = - maxsize - 1
odd_min = maxsize
even_sum = 0
even_max = - maxsize - 1
even_min = maxsize


for num in range (1, n + 1):
    number = float(input())
    if not num % 2 == 0:
        odd_sum += number
        if number > odd_max:
            odd_max = number
        if number < odd_min:
            odd_min = number
    else:
        even_sum += number
        if number > even_max:
            even_max = number
        if number < even_min:
            even_min = number

print(f'OddSum={odd_sum:.2f},')
if n == 0:
    print('OddMin=No,')
    print('OddMax=No,')
else:
    print(f'OddMin={odd_min:.2f},')
    print(f'OddMax={odd_max:.2f},')
print(f'EvenSum={even_sum:.2f},')
if n == 0 or n == 1:
    print('EvenMin=No,')
    print('EvenMax=No')
else:
    print(f'EvenMin={even_min:.2f},')
    print(f'EvenMax={even_max:.2f}')