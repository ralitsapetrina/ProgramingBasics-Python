age = int(input())
machine_price = float(input())
p = int(input())

money_gift = 0
brother_takes = 1
all_money = 0

for birthday in range (1, age + 1):
    if birthday % 2 == 0:
        money_gift += 10
        all_money += money_gift - brother_takes
    else:
        all_money += p

diff = abs(all_money - machine_price)

if all_money >= machine_price:
    print(f'Yes! {diff:.2f}')
else:
    print(f'No! {diff:.2f}')