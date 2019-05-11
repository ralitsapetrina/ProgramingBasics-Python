budget = float(input())
season = input()

destination = ""
place = ""
spent = 0

if budget <= 100:
    destination = "Bulgaria"
    if season == "summer":
        spent = budget * (30/100) # 30% from budget
        place = "Camp"
    elif season == "winter":
        spent = budget * (70/100) # 70% from budget
        place = "Hotel"
elif budget <= 1000:
    destination = "Balkans"
    if season == "summer":
        spent = budget * (40/100) # 40% from budget
        place = "Camp"
    elif season == "winter":
        spent = budget * (80/100) # 80% from budget
        place = "Hotel"
elif budget > 1000:
    destination = "Europe"
    place = "Hotel"
    spent = budget * (90/100) # 90% from budget

print(f"Somewhere in {destination}")
print(f"{place} - {spent:.2f}")