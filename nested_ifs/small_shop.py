product = input().lower()
city = input().lower()
quantity = float(input())

price = 0


if city == "sofia":
    if product == "coffee":
        price = quantity * 0.5
    elif product == "water":
        price = quantity * 0.8
    elif product == "beer":
        price = quantity * 1.2
    elif product == "sweets":
        price = quantity * 1.45
    elif product == "peanuts":
        price = quantity * 1.6
elif city == "plovdiv":
    if product == "coffee":
        price = quantity * 0.4
    elif product == "water":
        price = quantity * 0.7
    elif product == "beer":
        price = quantity * 1.15
    elif product == "sweets":
        price = quantity * 1.3
    elif product == "peanuts":
        price = quantity * 1.5
elif city == "varna":
    if product == "coffee":
        price = quantity * 0.45
    elif product == "water":
        price = quantity * 0.7
    elif product == "beer":
        price = quantity * 1.1
    elif product == "sweets":
        price = quantity * 1.35
    elif product == "peanuts":
        price = quantity * 1.55

print(price)