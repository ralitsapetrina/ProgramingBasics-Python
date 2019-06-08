name = input()
grade = 1
avg_score = 0
fail_count = 0

while grade <= 12:
    score = float(input())
    if score >= 4:
        avg_score += score
        grade += 1
    else:
        fail_count += 1

    if fail_count > 1:
        print(f'{name} has been excluded at {grade} grade')
        break

if not fail_count > 1:
    print(f'{name} graduated. Average grade: {(avg_score / 12):.2f}')