graduses = int(input())
time_of_day = input()

outfit = ""
shoes = ""

if time_of_day == "Morning":
    if graduses >= 10 and graduses <= 18:
        outfit = "Sweatshirt"
        shoes = "Sneakers"
    elif graduses > 18 and graduses <= 24:
        outfit = "Shirt"
        shoes = "Moccasins"
    elif graduses >= 25:
        outfit = "T-Shirt"
        shoes = "Sandals"
elif time_of_day == "Afternoon":
    if graduses >= 10 and graduses <= 18:
        outfit = "Shirt"
        shoes = "Moccasins"
    elif graduses > 18 and graduses <= 24:
        outfit = "T-Shirt"
        shoes = "Sandals"
    elif graduses >= 25:
        outfit = "Swim Suit"
        shoes = "Barefoot"
elif time_of_day == "Evening":
    if graduses >= 10 and graduses <= 18:
        outfit = "Shirt"
        shoes = "Moccasins"
    elif graduses > 18 and graduses <= 24:
        outfit = "Shirt"
        shoes = "Moccasins"
    elif graduses >= 25:
        outfit = "Shirt"
        shoes = "Moccasins"






print(f"It's {graduses} degrees, get your {outfit} and {shoes}.")