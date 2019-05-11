proj_type = input().lower()
rows = int(input())
columns = int(input())

result = 0

premiere_price = 12
normal_price = 7.5
discount_price = 5
hall_places = rows * columns

if proj_type == "premiere":
    result = hall_places * premiere_price
elif proj_type == "normal":
    result = hall_places * normal_price
elif proj_type == "discount":
    result = hall_places * discount_price

print(f"{result:.2f}")
