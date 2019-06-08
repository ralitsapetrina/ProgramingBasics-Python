number_1 = int(input())
number_2 = int(input())

for check in range(number_1, number_2 + 1):
    check_str = str(check)
    left_sum = int(check_str[0]) + int(check_str[1])
    right_sum = int(check_str[3]) + int(check_str[4])
    if left_sum == right_sum:
        print(check, end=' ')
    elif left_sum < right_sum:
        if left_sum + int(check_str[2]) == right_sum:
            print(check, end=' ')
    elif left_sum > right_sum:
        if right_sum + int(check_str[2]) == left_sum:
            print(check, end=' ')
