control_minutes = int(input())
control_seconds = int(input())
lenght = float(input())
seconds_for_100 = int(input())

control_time = control_minutes * 60 + control_seconds
slow_down = 0

if lenght >= 120:
    slow_down = lenght / 120 * 2.5

real_time = (lenght / 100) * seconds_for_100 - slow_down

if real_time <= control_time:
    print('Marin Bangiev won an Olympic quota!')
    print(f'His time is {real_time:.3f}.')
else:
    print(f'No, Marin failed! He was {(real_time - control_time):.3f} second slower.')