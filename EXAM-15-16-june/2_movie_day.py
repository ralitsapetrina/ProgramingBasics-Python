shooting_time = int(input())
scenes = int(input())
scene_time = int(input())

prepare = (15/100) * shooting_time # 15% of the shooting time
shoots = scene_time * scenes + prepare

diff = abs(shooting_time - shoots)

if shooting_time >= shoots:
    print(f'You managed to finish the movie on time! You have {round(diff)} minutes left!')
else:
    print(f'Time is up! To complete the movie you need {round(diff)} minutes.')