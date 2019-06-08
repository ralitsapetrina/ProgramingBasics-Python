bad_grade_limit = int(input())
counter = 0
avarage_score = 0
last_problem = ""
poor_grades = 0

while True:
    task_name = input()

    if task_name == 'Enough':
        print(f'Average score: {(avarage_score / counter):.2f}')
        print(f'Number of problems: {counter}')
        print(f'Last problem: {last_problem}')
        break

    score = int(input())
    counter += 1
    avarage_score += score

    if score <= 4:
        poor_grades += 1

    if poor_grades == bad_grade_limit:
        print(f'You need a break, {poor_grades} poor grades.')
        break

    last_problem = task_name
