month = input().lower()
nights = int(input())

studio_price = 0
apartment_price = 0

if month == "may" or month == "october":
    studio_price = 50 * nights
    if nights > 7 and nights < 14:
        studio_price -= studio_price * (5/100) # 5% discount
    elif nights > 14:
        studio_price -= studio_price * (30/100) # 30% discount
    apartment_price = 65 * nights
    if nights > 14:
        apartment_price -= apartment_price * (10/100) # 10% discount
elif month == "june" or month == "september":
    studio_price = 75.20 * nights
    if nights > 14:
        studio_price -= studio_price * (20/100) # 20% discount
    apartment_price = 68.7 * nights
    if nights > 14:
        apartment_price -= apartment_price * (10/100) # 10% discount
elif month == "july" or month == "august":
    studio_price = 76 * nights
    apartment_price = 77 * nights
    if nights > 14:
        apartment_price -= apartment_price * (10/100) # 10% discount

print(f"Apartment: {apartment_price:.2f} lv.")
print(f"Studio: {studio_price:.2f} lv.")