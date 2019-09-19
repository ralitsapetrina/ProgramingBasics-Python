country = input()
discipline = input()

hardness = 0
performance = 0

if discipline == "ribbon":
    if country == "Russia":
        hardness = 9.1
        performance = 9.4
    elif country == "Bulgaria":
        hardness = 9.6
        performance = 9.4
    elif country == "Italy":
        hardness = 9.2
        performance = 9.5
elif discipline == "hoop":
    if country == "Russia":
        hardness = 9.3
        performance = 9.8
    elif country == "Bulgaria":
        hardness = 9.55
        performance = 9.75
    elif country == "Italy":
        hardness = 9.45
        performance = 9.35
elif discipline == "rope":
    if country == "Russia":
        hardness = 9.6
        performance = 9.0
    elif country == "Bulgaria":
        hardness = 9.5
        performance = 9.4
    elif country == "Italy":
        hardness = 9.7
        performance = 9.15

percent = (20 - (hardness + performance)) / 20 * 100

print(f'The team of {country} get {(hardness + performance):.3f} on {discipline}.')
print(f'{percent:.2f}%')