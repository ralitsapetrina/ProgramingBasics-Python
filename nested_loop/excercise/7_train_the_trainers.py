n = int(input())
grade_count = 0
final_grade = 0

while True:
    presentation = input()
    if presentation == "Finish":
        break
    avg_grade = 0
    counter = 0
    while counter < n:
        grade = float(input())
        avg_grade += grade
        final_grade += grade
        counter += 1
        grade_count += 1
    print(f'{presentation} - {(avg_grade / n):.2f}.')

print(f'Student\'s final assessment is {(final_grade / grade_count):.2f}.')
