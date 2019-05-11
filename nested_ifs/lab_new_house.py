type_flower = input()
quantity = int(input())
budget = int(input())

final_price = 0

roses_price = 5
dahlias_price = 3.8
tulips_price = 2.8
narcissus_price = 3
gladiolus_price = 2.5

if type_flower == "Roses":
    final_price = quantity * roses_price
    if quantity > 80:
        final_price -= final_price * (10/100)
elif type_flower == "Dahlias":
    final_price = quantity * dahlias_price
    if quantity > 90:
        final_price -= final_price * (15/100)
elif type_flower == "Tulips":
    final_price = quantity * tulips_price
    if quantity > 80:
        final_price -= final_price * (15/100)
elif type_flower == "Narcissus":
    final_price = quantity * narcissus_price
    if quantity < 120:
        final_price += final_price * (15/100)
elif type_flower == "Gladiolus":
    final_price = quantity * gladiolus_price
    if quantity < 80:
        final_price += final_price * (20/100)

difference = budget - final_price

if final_price <= budget:
    print(f"Hey, you have a great garden with {quantity} {type_flower} and {difference:.2f} leva left.")
else:
    print(f"Not enough money, you need {abs(difference):.2f} leva more.")