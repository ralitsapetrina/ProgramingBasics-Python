exam_hour = int(input())
exam_minutes = int(input())
arr_hour = int(input())
arr_minutes = int(input())

arrival = ""

if arr_hour > exam_hour:
    arrival = 'Late'
elif arr_hour == exam_hour and arr_minutes > exam_minutes:
    arrival = 'Late'
elif arr_hour == exam_hour and arr_minutes - exam_minutes <= 30:
    arrival = 'On time'
elif arr_hour < exam_hour and (60 - arr_minutes) + exam_minutes <= 30:
    arrival = 'On time'
elif arr_hour == exam_hour and arr_minutes - exam_minutes > 30:
    arrival = 'Early'
elif arr_hour < exam_hour and (60 - arr_minutes) + exam_minutes > 30:
    arrival = 'Early'

diff_min = None
diff_hour = None

if arr_hour > exam_hour:
    if (60 - arr_minutes) + exam_minutes > 60:
        diff_min = arr_minutes + (60 - exam_minutes)
        if arr_hour - exam_hour > 1:
            diff_hour = arr_hour - exam_hour - 1
    else:
        diff_hour = arr_hour - exam_hour
        diff_min = (arr_minutes + (60 - exam_minutes)) - 60
elif arr_hour == exam_hour and arr_minutes > exam_minutes:
    diff_min = arr_minutes - exam_minutes
elif arr_hour < exam_hour:
    if (60 - arr_minutes) + exam_minutes < 60:
        diff_min = (60 - arr_minutes) + exam_minutes
        if exam_hour - arr_hour > 1:
            diff_hour = exam_hour - arr_hour - 1
    else:
        diff_hour = exam_hour - arr_hour
        diff_min = ((60 - arr_minutes) + exam_minutes) - 60
elif arr_hour == exam_hour and arr_minutes < exam_minutes:
    diff_min = exam_minutes - arr_minutes

print(arrival)

if diff_hour:
    if arrival == 'On time' or arrival == 'Early':
        if diff_min <= 9:
            print(f'{diff_hour}:0{diff_min} hours before the start')
        else:
            print(f'{diff_hour}:{diff_min} hours before the start')
    else:
        if diff_min <= 9:
            print(f'{diff_hour}:0{diff_min} hours after the start')
        else:
            print(f'{diff_hour}:{diff_min} hours after the start')
elif not diff_hour and diff_min:
    if arrival == 'On time' or arrival == 'Early':
        print(f'{diff_min} minutes before the start')
    else:
        print(f'{diff_min} minutes after the start')