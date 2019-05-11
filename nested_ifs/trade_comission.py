town = input().lower()
sale_value = float(input())

result = None

if town == "sofia":
    if sale_value >= 0 and sale_value <= 500:
        result = sale_value * (5/100)
    elif sale_value > 500 and sale_value <= 1000:
        result = sale_value * (7/100)
    elif sale_value > 1000 and sale_value <= 10000:
        result = sale_value * (8/100)
    elif sale_value > 10000:
        result = sale_value * (12/100)
elif town == "varna":
    if sale_value >= 0 and sale_value <= 500:
        result = sale_value * (4.5/100)
    elif sale_value > 500 and sale_value <= 1000:
        result = sale_value * (7.5/100)
    elif sale_value > 1000 and sale_value <= 10000:
        result = sale_value * (10/100)
    elif sale_value > 10000:
        result = sale_value * (13/100)
elif town == "plovdiv":
    if sale_value >= 0 and sale_value <= 500:
        result = sale_value * (5.5/100)
    elif sale_value > 500 and sale_value <= 1000:
        result = sale_value * (8/100)
    elif sale_value > 1000 and sale_value <= 10000:
        result = sale_value * (12/100)
    elif sale_value > 10000:
        result = sale_value * (14.5/100)

if result:
    print(f"{result:.2f}")
else:
    print("error")