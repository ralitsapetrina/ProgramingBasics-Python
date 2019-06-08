w = int(input())
h = int(input())

cake_size = w * h
piece_cake = 1
cake_taken = 0

while cake_size >= 0:
    pieces_taken = input()
    if pieces_taken == "STOP":
        print(f'{cake_size} pieces are left.')
        break
    cake_size -= int(pieces_taken)

if cake_size < 0:
    print(f'No more cake left! You need {abs(cake_size)} pieces more.')