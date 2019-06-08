magic_num = int(input())

for x1 in range(0, 10):
    for x2 in range(0, 10):
        for x3 in range(0, 10):
            for x4 in range(0, 10):
                for x5 in range(0, 10):
                    for x6 in range(0, 10):
                        if x1 * x2 * x3 * x4 * x5 * x6 == magic_num:
                            print(f'{x1}{x2}{x3}{x4}{x5}{x6} ', end = "")