name_1 = input()
name_2 = input()

points_pl_1 = 0
points_pl_2 = 0
winner = None
card_pl_1 = None
card_pl_2 = None

while True:
    card_pl_1 = input()
    if card_pl_1 == "End of game":
        print(f'{name_1} has {points_pl_1} points')
        print(f'{name_2} has {points_pl_2} points')
        break
    card_pl_2 = input()
    if card_pl_2 == "End of game":
        print(f'{name_1} has {points_pl_1} points')
        print(f'{name_2} has {points_pl_2} points')
        break
    card_diff = abs(int(card_pl_1) - int(card_pl_2))
    if int(card_pl_1) > int(card_pl_2):
        points_pl_1 += card_diff
    elif int(card_pl_1) < int(card_pl_2):
        points_pl_2 += card_diff
    elif int(card_pl_1) == int(card_pl_2):
        card_pl_1 = input()
        card_pl_2 = input()
        winner = True
        print('Number wars!')
        if int(card_pl_1) > int(card_pl_2):
            print(f'{name_1} is winner with {points_pl_1} points')
        else:
            print(f'{name_2} is winner with {points_pl_2} points')
        break