tabs = int(input())
salary = int(input())

for open in range(tabs):
    open_tab = input().lower()
    if open_tab == "facebook":
        salary -= 150
    elif open_tab == "instagram":
        salary -= 100
    elif open_tab == "reddit":
        salary -= 50
    if salary <= 0:
        print('You have lost your salary.')
        break

if salary > 0:
    print(f'{(salary)}')