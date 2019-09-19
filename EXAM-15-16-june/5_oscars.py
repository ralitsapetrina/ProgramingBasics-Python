actor = input()
academy_points = float(input())
jury_count = int(input())


for jury in range(1, jury_count + 1):
    person = input()
    points = float(input())
    given_points = (len(person) * points) / 2
    academy_points += given_points
    if academy_points > 1250.5:
        print(f"Congratulations, {actor} got a nominee for leading role with {academy_points:.1f}!")
        break

if academy_points <= 1250.5:
    print(f'Sorry, {actor} you need {(1250.5 - academy_points):.1f} more!')