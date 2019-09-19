budget = float(input())
counter = 0
paid_money = 0

while True:
    product = input()
    if product == "Stop":
        print(f'You bought {counter} products for {paid_money:.2f} leva.')
        break
    price = float(input())
    counter += 1
    if counter % 3 == 0:
        price = price / 2
    if price > budget:
        print(f'You don\'t have enough money!')
        print(f'You need {(price - budget):.2f} leva!')
        break

    budget -= price
    paid_money += price