n = int(input())
counter = 0
total = 0

while counter < n:
    deposit = float(input())
    if deposit < 0:
        print('Invalid operation!')
        break
    print(f'Increase: {deposit:.2f}')
    total += deposit
    counter += 1

print(f'Total: {total:.2f}')