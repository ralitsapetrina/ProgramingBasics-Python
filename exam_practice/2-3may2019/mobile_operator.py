contract_lenght = input()
contract_type = input()
internet = input()
months = int(input())

pay_month = 0
total_pay = 0

if contract_lenght == "one":
    if contract_type == "Small":
        pay_month = 9.98
    elif contract_type == "Middle":
        pay_month = 18.99
    elif contract_type == "Large":
        pay_month = 25.98
    elif contract_type == "ExtraLarge":
        pay_month = 35.99
elif contract_lenght == "two":
    if contract_type == "Small":
        pay_month = 8.58
    elif contract_type == "Middle":
        pay_month = 17.09
    elif contract_type == "Large":
        pay_month = 23.59
    elif contract_type == "ExtraLarge":
        pay_month = 31.79

if internet == "yes":
    if pay_month <= 10:
        pay_month += 5.5
    elif pay_month <= 30:
        pay_month += 4.35
    elif pay_month > 30:
        pay_month += 3.85

total_pay = pay_month * months

if contract_lenght == "two":
    total_pay -= total_pay * 0.0375 # 3.75% discount

print(f'{total_pay:.2f} lv.')