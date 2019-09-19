won_games = 0
lost_games = 0
all_games_count = 0

while True:
    tournament = input()
    if tournament == 'End of tournaments':
        break

    games_in_tour = int(input())
    games_counter = 0
    while games_counter < games_in_tour:
        our_team = int(input())
        other_team = int(input())
        games_counter += 1
        all_games_count += 1
        if our_team > other_team:
            won_games += 1
            print(f'Game {games_counter} of tournament {tournament}: win with {our_team - other_team} points.')
        else:
            lost_games += 1
            print(f'Game {games_counter} of tournament {tournament}: lost with {other_team - our_team} points.')


percent_win = 100 / all_games_count * won_games
percent_lost = 100 / all_games_count * lost_games

print(f'{percent_win:.2f}% matches win')
print(f'{percent_lost:.2f}% matches lost')