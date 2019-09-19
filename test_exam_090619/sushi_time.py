from math import ceil

sushi_type = input()
place = input()
portions = int(input())
order = input()
true_place = True
sushi_pay = 0

if place == 'Sushi Zone':
    if sushi_type == 'sashimi':
        sushi_pay = portions * 4.99
    elif sushi_type == 'maki':
        sushi_pay = portions * 5.29
    elif sushi_type == 'uramaki':
        sushi_pay = portions * 5.99
    elif sushi_type == 'temaki':
        sushi_pay = portions * 4.29
elif place == 'Sushi Time':
    if sushi_type == 'sashimi':
        sushi_pay = portions * 5.49
    elif sushi_type == 'maki':
        sushi_pay = portions * 4.69
    elif sushi_type == 'uramaki':
        sushi_pay = portions * 4.49
    elif sushi_type == 'temaki':
        sushi_pay = portions * 5.19
elif place == 'Sushi Bar':
    if sushi_type == 'sashimi':
        sushi_pay = portions * 5.25
    elif sushi_type == 'maki':
        sushi_pay = portions * 5.55
    elif sushi_type == 'uramaki':
        sushi_pay = portions * 6.25
    elif sushi_type == 'temaki':
        sushi_pay = portions * 4.75
elif place == 'Asian Pub':
    if sushi_type == 'sashimi':
        sushi_pay = portions * 4.5
    elif sushi_type == 'maki':
        sushi_pay = portions * 4.8
    elif sushi_type == 'uramaki':
        sushi_pay = portions * 5.5
    elif sushi_type == 'temaki':
        sushi_pay = portions * 5.5
else:
    true_place = False
    print(f'{place} is invalid restaurant!')


if order == "Y" and true_place:
    print(f'Total price: {ceil(sushi_pay + sushi_pay * 0.2)} lv.')
elif order == "N" and true_place:
    print(f'Total price: {ceil(sushi_pay)} lv.')