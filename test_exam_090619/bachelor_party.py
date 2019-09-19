guest_price = int(input())
money = 0
guests = 0

while True:
    group = input()
    if group == "The restaurant is full":
        break
    guests += int(group)
    if int(group) < 5:
        money += int(group) * 100
    elif int(group) >= 5:
        money += int(group) * 70

if money >= guest_price:
    print(f'You have {guests} guests and {money - guest_price} leva left.')
else:
    print(f'You have {guests} guests and {money} leva income, but no singer.')