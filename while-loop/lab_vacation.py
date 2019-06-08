trip_money = float(input())
saved_money = float(input())

counter = 0
spend_counter = 0
spend_limit = 5

while saved_money < trip_money:
    balance = input()
    balance_sum = float(input())
    counter += 1

    if balance == "spend":
        spend_counter += 1
        if balance_sum > saved_money:
            saved_money -= saved_money
        else:
            saved_money -= balance_sum

    if balance == "save":
        spend_counter = 0
        saved_money += balance_sum

    if spend_counter == spend_limit:
        print("You can't save the money.")
        print(f'{counter}')
        break

if saved_money >= trip_money:
    print(f'You saved the money for {counter} days.')
