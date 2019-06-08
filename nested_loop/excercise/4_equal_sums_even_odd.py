number_1 = int(input())
number_2 = int(input())

for check in range(number_1, number_2 + 1):
    even_sum = 0
    odd_sum = 0
    check_str = str(check)
    even_sum = int(check_str[1]) + int(check_str[3]) + int(check_str[5])
    odd_sum = int(check_str[0]) + int(check_str[2]) + int(check_str[4])
    if even_sum == odd_sum:
        print(check, end=' ')
