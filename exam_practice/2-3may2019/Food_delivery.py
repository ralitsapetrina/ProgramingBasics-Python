chicken_menu = int(input())
fish_menu = int(input())
veggie_menu = int(input())

delivery = 2.5

menu_price = chicken_menu * 10.35 + fish_menu * 12.40 + veggie_menu * 8.15

dessert_price = menu_price * 0.2 # 20 % of the whole price

total = menu_price + dessert_price + delivery

print(f'Total: {total:.2f}')