budget = int(input())
season = input()
group_count = int(input())

final_price = 0
group_discount = 0
even_discount = 5/100

spr_rent = 3000
sum_rent = 4200
aut_rent = 4200
win_rent = 2600

even_group = group_count % 2 == 0

if group_count <= 6:
    group_discount = (10/100)
elif group_count >= 7 and group_count <= 11:
    group_discount = (15/100)
elif group_count >= 12:
    group_discount = (25/100)


if season == "Spring":
    final_price = spr_rent - spr_rent * group_discount
    if even_group:
        final_price -= final_price * even_discount
elif season == "Summer":
    final_price = sum_rent - sum_rent * group_discount
    if even_group:
        final_price -= final_price * even_discount
elif season == "Autumn":
    final_price = aut_rent  - aut_rent * group_discount
elif season == "Winter":
    final_price = win_rent  - win_rent * group_discount
    if even_group:
        final_price -= final_price * even_discount


difference = budget - final_price

if budget >= final_price:
    print(f"Yes! You have {difference:.2f} leva left.")
else:
    print(f"Not enough money! You need {abs(difference):.2f} leva.")