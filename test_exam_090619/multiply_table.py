number = int(input())

arr = [int(x) for x in str(number)]

for x1 in range(1, arr[2] + 1):
    for x2 in range(1, arr[1] + 1):
        for x3 in range(1, arr[0] + 1):
            print(f'{x1} * {x2} * {x3} = {x1 * x2 * x3};')