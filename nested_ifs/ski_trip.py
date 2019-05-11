days = int(input()) - 1
room_type = input()
review = input()

result = 0

if room_type == "room for one person":
    result = days * 18
elif room_type == "apartment":
    if days < 10:
        result = days * 25
        result -= result * (30/100)
    elif days >= 10 and days <= 15:
        result = days * 25
        result -= result * (35/100)
    elif days > 15:
        result = days * 25
        result -= result * (50/100)
elif room_type == "president apartment":
    if days < 10:
        result = days * 35
        result -= result * (10/100)
    elif days >= 10 and days <= 15:
        result = days * 35
        result -= result * (15/100)
    elif days > 15:
        result = days * 35
        result -= result * (20/100)


if review == "positive":
    result *= 1.25
elif review == "negative":
    result *= 0.9

print(f"{result:.2f}")