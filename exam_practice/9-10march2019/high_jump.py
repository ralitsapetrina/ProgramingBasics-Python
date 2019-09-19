goal_height = int(input())
jumps = 0
current_height = goal_height - 30

while current_height <= goal_height:
    jump_trys = 0
    while jump_trys < 3:
        jump_cm = int(input())
        jumps += 1
        jump_trys += 1
        if jump_cm > current_height and current_height == goal_height:
            print(f'Tihomir succeeded, he jumped over {goal_height}cm after {jumps} jumps.')
            break
        elif jump_cm > current_height:
            jump_trys = 0
            break
    if jump_trys == 3:
        print(f'Tihomir failed at {current_height}cm after {jumps} jumps.')
        break
    current_height += 5