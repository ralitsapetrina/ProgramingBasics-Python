w = int(input())
l = int(input())
h = int(input())

space = w * l * h
box_space = 0

while box_space <= space:
    box_move = input()
    if box_move == "Done":
        print(f"{space - box_space} Cubic meters left.")
        break
    else:
        box_space += int(box_move)

if box_space > space:
    print(f"No more free space! You need {box_space - space} Cubic meters more.")