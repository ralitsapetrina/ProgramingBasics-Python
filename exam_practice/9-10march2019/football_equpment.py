import math
tennis_rocket_price = float(input())
number_rockets = int(input())
number_shoes = int(input())

rockets_pay = tennis_rocket_price * number_rockets
shoes_pay = (tennis_rocket_price / 6) * number_shoes
other_equipment_pay = (20/100) * (rockets_pay + shoes_pay)

all_pay = rockets_pay + shoes_pay + other_equipment_pay

print(f'Price to be paid by Djokovic {math.floor(all_pay / 8)}')
print(f'Price to be paid by sponsors {math.ceil(all_pay / 8 * 7)}')