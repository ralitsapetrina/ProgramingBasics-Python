food_money = float(input())
souvenir_money = float(input())
hotel_money = float(input())

days = 3

drive_litres = 420 / 100 * 7
drive_expence = drive_litres * 1.85

food_expence = days * food_money
souvenir_expence = days * souvenir_money
hotel_expence = hotel_money * 3 - (hotel_money * 0.1 + hotel_money * 0.15 + hotel_money * 0.2)

total_money = food_expence + souvenir_expence + hotel_expence + drive_expence

print(f'Money needed: {total_money:.2f}')