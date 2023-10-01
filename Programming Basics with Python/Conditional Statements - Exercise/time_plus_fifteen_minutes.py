hours = int(input())
minutes = int(input())

minutes = minutes + 15
total = (hours * 60) + minutes

hours = total // 60
minutes = total % 60

if hours > 23:
    hours = hours - 24
if minutes < 10:
    print(f"{hours}:0{minutes}")
else:
    print(f"{hours}:{minutes}")
