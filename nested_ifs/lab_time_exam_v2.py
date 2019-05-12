exam_hour = int(input())
exam_minutes = int(input())
arrival_hour = int(input())
arrival_minutes = int(input())

exam_in_min = exam_hour * 60 + exam_minutes
arrival_in_min = arrival_hour * 60 + arrival_minutes

time_diff = abs(exam_in_min - arrival_in_min)

if arrival_in_min <= exam_in_min and time_diff <= 30:
    if arrival_in_min == exam_in_min:
        print("On time")
    else:
        print(f"On time {time_diff} minutes before the start")

hours = time_diff // 60
minutes = time_diff % 60

if minutes <= 9:
    minutes = (f"0{minutes}")

if arrival_in_min < exam_in_min and time_diff > 30:
    print("Early")
    if time_diff > 59:
        print(f"Early {hours}:{minutes} hours before the start")
    else:
        print(f"{time_diff} minutes before the start")
if arrival_in_min > exam_in_min:
    print("Late")
    if time_diff > 59:
        print(f"Late {hours}:{minutes} hours after the start")
    else:
        print(f"{time_diff} minutes after the start")