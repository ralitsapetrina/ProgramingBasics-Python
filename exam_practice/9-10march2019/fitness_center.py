n = int(input())

back = 0
chest = 0
legs = 0
abs = 0
prot_shake = 0
prot_bar = 0

for person in range(n):
    activity = input()
    if activity == "Back":
        back += 1
    elif activity == "Chest":
        chest += 1
    elif activity == "Legs":
        legs += 1
    elif activity == "Abs":
        abs += 1
    elif activity == "Protein shake":
        prot_shake += 1
    elif activity == "Protein bar":
        prot_bar += 1


print(f"{back} - back")
print(f"{chest} - chest")
print(f"{legs} - legs")
print(f"{abs} - abs")
print(f"{prot_shake} - protein shake")
print(f"{prot_bar} - protein bar")
print(f"{(100 / n * (back + chest + legs + abs)):.2f}% - work out")
print(f"{(100 / n * (prot_bar + prot_shake)):.2f}% - protein")