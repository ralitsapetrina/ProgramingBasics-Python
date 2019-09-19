import math
widht_ship = float(input())
lenght_ship = float(input())
height_ship = float(input())
avg_height = float(input())

ship_volume = widht_ship * lenght_ship * height_ship

room_volume = (avg_height + 0.40) * 2 * 2

possible_astr = ship_volume // room_volume

if possible_astr >= 3 and possible_astr <= 10:
    print(f'The spacecraft holds {math.floor(possible_astr)} astronauts.')
elif possible_astr < 3:
    print('The spacecraft is too small.')
elif possible_astr > 10:
    print('The spacecraft is too big.')