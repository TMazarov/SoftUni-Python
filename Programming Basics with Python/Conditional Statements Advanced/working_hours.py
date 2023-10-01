time = int(input())
day = input()

working_days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']

if day in working_days:
    if 10 <= time < 18:
        print("open")
    else:
        print("closed")
else:
    print("closed")
