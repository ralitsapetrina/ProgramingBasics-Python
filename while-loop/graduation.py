name = input()
grade = 1
avg_score = 0

while grade <= 12:
    score = float(input())
    if score >= 4:
        avg_score += score
        grade += 1

print(f'{name} graduated. Average grade: {(avg_score / 12):.2f}')