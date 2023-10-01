current_day = input()

working_days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']
weekend = ['Saturday', 'Sunday']

if current_day in working_days:
    print("Working day")
elif current_day in weekend:
    print("Weekend")
else:
    print("Error")
    