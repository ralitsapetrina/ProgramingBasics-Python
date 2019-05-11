fruit = input().lower()
day = input().lower()
quantity = float(input())

result = None

if day == "monday" or day == "tuesday" or day == "wednesday" or day == "thursday" or day == "friday":
    if fruit == "banana":
        result = quantity * 2.5
    elif fruit == "apple":
        result = quantity * 1.2
    elif fruit == "orange":
        result = quantity * 0.85
    elif fruit == "grapefruit":
        result = quantity * 1.45
    elif fruit == "kiwi":
        result = quantity * 2.7
    elif fruit == "pineapple":
        result = quantity * 5.5
    elif fruit == "grapes":
        result = quantity * 3.85

elif day == "saturday" or day == "sunday":
    if fruit == "banana":
        result = quantity * 2.7
    elif fruit == "apple":
        result = quantity * 1.25
    elif fruit == "orange":
        result = quantity * 0.9
    elif fruit == "grapefruit":
        result = quantity * 1.6
    elif fruit == "kiwi":
        result = quantity * 3
    elif fruit == "pineapple":
        result = quantity * 5.6
    elif fruit == "grapes":
        result = quantity * 4.2

if result:
    print(f"{result:.2f}")
else:
    print("error")