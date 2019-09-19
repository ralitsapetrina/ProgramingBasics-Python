name = input()
days = int(input())
tickets = int(input())
ticket_price = float(input())
percent_cinema = int(input())

total_profit = days * tickets * ticket_price

final_profit = total_profit - (total_profit * (percent_cinema/100))

print(f'The profit from the movie {name} is {final_profit:.2f} lv.')