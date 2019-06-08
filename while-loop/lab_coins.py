change = float(input())
coin_count = 0
change_coins = int(change * 100)

while change_coins > 0:
    if change_coins >= 200:
        coin_count += change_coins // 200
        change_coins -= change_coins // 200 * 200
    elif change_coins >= 100:
        coin_count += 1
        change_coins -= 100
    elif change_coins >= 50:
        coin_count += 1
        change_coins -= 50
    elif change_coins >= 20:
        coin_count += change_coins // 20
        change_coins -= change_coins // 20 * 20
    elif change_coins >= 10:
        coin_count += 1
        change_coins -= 10
    elif change_coins >= 5:
        coin_count += 1
        change_coins -= 5
    elif change_coins >= 2:
        coin_count += change_coins // 2
        change_coins -= change_coins // 2 * 2
    elif change_coins >= 1:
        coin_count += 1
        change_coins -= 1

print(int(coin_count))