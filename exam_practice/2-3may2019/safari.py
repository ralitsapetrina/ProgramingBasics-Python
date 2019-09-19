budget = float(input())
litres_drive = float(input())
day = input()

guide = 100
sat_discount = 10/100
sun_discount = 20/100

drive_price = litres_drive * 2.1
total_price = drive_price + guide

if day == "Saturday":
    total_price -= total_price * sat_discount
elif day == "Sunday":
    total_price -= total_price * sun_discount

diff = abs(budget - total_price)

if budget >= total_price:
    print(f'Safari time! Money left: {diff:.2f} lv.')
else:
    print(f'Not enough money! Money needed: {diff:.2f} lv.')