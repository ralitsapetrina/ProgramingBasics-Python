a_input = int(input())
b_input = int(input())
c_input = int(input())
d_input = int(input())

for a in range(a_input, b_input + 1):
    for b in range (a_input, b_input + 1):
        for c in range(c_input, d_input + 1):
            for d in range(c_input, d_input + 1):
                if a + d == b + c and a != b and c != d:
                    print(f'{a}{b}\n{c}{d}\n')