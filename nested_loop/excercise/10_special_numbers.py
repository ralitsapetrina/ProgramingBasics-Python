n = int(input())

for special_1 in range(1, 10):
    for special_2 in range(1, 10):
        for special_3 in range(1, 10):
            for special_4 in range(1, 10):
                if n % special_1 == 0 and n % special_2 == 0 and n % special_3 == 0 and n % special_4 == 0:
                    print(f'{special_1}{special_2}{special_3}{special_4}', end = " ")