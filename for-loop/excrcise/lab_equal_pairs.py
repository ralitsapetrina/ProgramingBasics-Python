from sys import maxsize
n = int(input())

pair_sum = 0
previous_pair_sum = 0
diff = 0
max_diff = 0
is_equal = None


for num in range(n):
    n1 = int(input())
    n2 = int(input())
    pair_sum = n1 + n2
    if not num == 0:
        if pair_sum == previous_pair_sum:
            is_equal = True
            if not diff == 0:
                is_equal = False
        else:
            diff = abs(previous_pair_sum - pair_sum)
            if diff > max_diff:
                max_diff = diff
    previous_pair_sum = pair_sum

if is_equal or n == 1:
    print(f'Yes, value={pair_sum}')
else:
    print(f'No, maxdiff={max_diff}')