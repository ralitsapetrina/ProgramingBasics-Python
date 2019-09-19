from math import floor

number_plays = int(input())
start_points = int(input())

won_play = 0
tour_points = 0

for play in range(number_plays):
    play_outcome = input()
    if play_outcome == "W":
        tour_points += 2000
        won_play += 1
    elif play_outcome == "F":
        tour_points += 1200
    elif play_outcome == "SF":
        tour_points += 720

avarage_points = 100 / number_plays * won_play

print(f'Final points: {start_points + tour_points}')
print(f'Average points: {floor(tour_points / number_plays)}')
print(f'{avarage_points:.2f}%')