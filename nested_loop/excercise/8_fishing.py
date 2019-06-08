daily_quota = int(input())
is_stopped = False
money = 0
cought_fish = 0

for fish in range(1, daily_quota + 1):
    name = input()
    if name == "Stop":
        is_stopped = True
        break
    fish_size = float(input())
    cought_fish += 1
    name_sum = 0
    fish_cost = 0
    for char in name:
        name_sum += ord(char)
    fish_cost = name_sum / fish_size
    if fish % 3 == 0:
        money += fish_cost
    else:
        money -= fish_cost

if not is_stopped:
    print('Lyubo fulfilled the quota!')

if money >= 0:
    print(f'Lyubo\'s profit from {cought_fish} fishes is {money:.2f} leva.')
else:
    print(f'Lyubo lost {abs(money):.2f} leva today.')
