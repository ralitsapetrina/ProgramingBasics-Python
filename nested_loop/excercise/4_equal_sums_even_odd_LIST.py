num_1 = int(input())
num_2 = int(input())

test = []
for check in range(num_1, num_2 + 1):
    arr = [int(x) for x in str(check)]
    even_list = arr[1::2]
    odd_list = arr[0::2]
    even_sum = sum(even_list)
    odd_sum = sum(odd_list)
    if even_sum == odd_sum:
        test.append(str(check))

print(' '.join(test))