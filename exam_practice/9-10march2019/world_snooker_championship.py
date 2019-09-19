champ_stage = input().lower()
ticket_type = input().lower()
ticket_count = int(input())
picture = input()

picture_price = 40 * ticket_count
ticket_price = 0
discount_price = 0

if champ_stage == "quarter final":
    if ticket_type == "standard":
        ticket_price = 55.5
    elif ticket_type == "premium":
        ticket_price = 105.2
    elif ticket_type == "vip":
        ticket_price = 118.9
elif champ_stage == "semi final":
    if ticket_type == "standard":
        ticket_price = 75.88
    elif ticket_type == "premium":
        ticket_price = 125.22
    elif ticket_type == "vip":
        ticket_price = 300.4
elif champ_stage == "final":
    if ticket_type == "standard":
        ticket_price = 110.1
    elif ticket_type == "premium":
        ticket_price = 160.66
    elif ticket_type == "vip":
        ticket_price = 400

all_pay_ticket = ticket_price * ticket_count

if picture == "Y":
    if all_pay_ticket > 4000:
        all_pay_ticket -= all_pay_ticket * (25/100)
    elif all_pay_ticket > 2500:
        all_pay_ticket = (all_pay_ticket - all_pay_ticket * (10/100)) + picture_price
    else:
        all_pay_ticket += picture_price
elif picture == "N":
    if all_pay_ticket > 4000:
        all_pay_ticket -= all_pay_ticket * (25/100)
    elif all_pay_ticket > 2500:
        all_pay_ticket -= all_pay_ticket * (10/100)

print(f'{all_pay_ticket:.2f}')

