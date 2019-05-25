from sys import maxsize

n = int(input())
max_num = -maxsize - 1
sum_num = 0

for num in range (n):
    num_input = int(input())
    if num_input > max_num:
        max_num = num_input
    sum_num += num_input

if sum_num - max_num == max_num:
    print('Yes')
    print(f'Sum = {max_num}')
else:
    print(f'No\nDiff = {abs(max_num - (sum_num - max_num))}')