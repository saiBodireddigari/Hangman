offset = int(input())

time = 1030
day = "Tuesday"
previous_day = "Monday"
after_day = "wednesday"

if offset in [-11, -12]:
    print("Monday")
elif offset in [14]:
    print("Wednesday")
else:
    print("Tuesday")
