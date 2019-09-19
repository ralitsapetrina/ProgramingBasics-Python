movie = input()
menu_type = input()
tickets = int(input())

price = 0

if movie == "John Wick":
    if menu_type == "Drink":
        price = 12
    elif menu_type == "Popcorn":
        price = 15
    elif menu_type == "Menu":
        price = 19
elif movie == "Star Wars":
    if menu_type == "Drink":
        price = 18
    elif menu_type == "Popcorn":
        price = 25
    elif menu_type == "Menu":
        price = 30

    if tickets >= 4:
        price -= price * (30/100) # 30% family discount

elif movie == "Jumanji":
    if menu_type == "Drink":
        price = 9
    elif menu_type == "Popcorn":
        price = 11
    elif menu_type == "Menu":
        price = 14

    if tickets == 2:
        price -= price * (15/100) # 15% discount

print(f'Your bill is {(price * tickets):.2f} leva.')