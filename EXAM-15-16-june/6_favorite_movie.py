import sys
max_points = - sys.maxsize - 1
counter = 0
best_movie = ''

while counter < 7:
    name = input()
    if name == "STOP":
        print(f'The best movie for you is {best_movie} with {max_points} ASCII sum.')
        break
    lenght_name = len(name)
    points = 0
    for letter in name:
        if letter.isupper():
            points += ord(letter) - lenght_name
        elif letter.islower():
            points += ord(letter) - 2 * lenght_name
        else:
            points += ord(letter)
    if points > max_points:
        max_points = points
        best_movie = name
    counter += 1

if counter == 7:
    print(f'The limit is reached.')
    print(f'The best movie for you is {best_movie} with {max_points} ASCII sum.')