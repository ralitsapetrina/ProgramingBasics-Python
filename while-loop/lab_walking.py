goal = 10000 # steps to reach
step_count = 0

while step_count < goal:
    step_command = input()
    if step_command == ('Going home'):
        step_command = input()
        step_count += int(step_command)
        if step_count < goal:
            print(f'{goal - step_count} more steps to reach goal.')
        break
    else:
        step_count += int(step_command)

if step_count >= goal:
    print('Goal reached! Good job!')