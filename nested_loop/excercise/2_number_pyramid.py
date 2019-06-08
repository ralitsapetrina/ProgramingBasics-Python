n = int(input())
counter = 0

for num in range(1, n + 1):
    for col in range(1, num + 1):
        counter += 1
        while counter <= n:
            print(f'{counter}', end=' ')
            break
    print()