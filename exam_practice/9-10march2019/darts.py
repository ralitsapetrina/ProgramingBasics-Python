name = input()

start_points = 301
good_shots = 0
bad_shots = 0

while not start_points == 0:
    play = input()
    if play == "Retire":
        print(f'{name} retired after {bad_shots} unsuccessful shots.')
        break
    points = int(input())
    if play == "Single":
        if start_points >= points:
            start_points -= points
            good_shots += 1
        else:
            bad_shots += 1
    elif play == "Double":
        if start_points >= points * 2:
            start_points -= 2 * points
            good_shots += 1
        else:
            bad_shots += 1
    elif play == "Triple":
        if start_points >= points * 3:
            start_points -= 3 * points
            good_shots += 1
        else:
            bad_shots += 1

if start_points == 0:
    print(f'{name} won the leg with {good_shots} shots.')