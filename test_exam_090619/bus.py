start_count = int(input())
stops = int(input())

passenger_count = start_count

for passenger in range(1, stops + 1):
    out_passenger = int(input())
    in_passenger = int(input())
    passenger_count += in_passenger - out_passenger

if not stops % 2 == 0:
    passenger_count += 2

print(f'The final number of passengers is : {passenger_count}')