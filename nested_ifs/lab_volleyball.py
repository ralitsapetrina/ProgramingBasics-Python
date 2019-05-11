import math

year_type = input()
p_holidays = int(input())
h_weekends = int(input())

sofia_weekends = 48 - h_weekends
not_working =  sofia_weekends * (3/4)
holiday_plays = p_holidays * (2/3)

plays = not_working + holiday_plays + h_weekends

if year_type == "leap":
    plays += plays * (15/100) # 15 % more plays

print(math.floor(plays))