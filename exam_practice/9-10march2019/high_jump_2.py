goal_height = int(input())

current_height = goal_height - 30
jumps = 0



while True:
    bad_jumps = 0
    while bad_jumps < 3:
        current_jump = int(input())
        jumps += 1
        if current_jump <= current_height:
            bad_jumps += 1
        elif current_jump > current_height:
            bad_jumps = 0
            break
    if bad_jumps == 3:
        print(f'Tihomir failed at {current_height}cm after {jumps} jumps.')
        break
    elif current_height >= goal_height:
        print(f'Tihomir succeeded, he jumped over {goal_height}cm after {jumps} jumps.')
        break
    else:
        current_height += 5
