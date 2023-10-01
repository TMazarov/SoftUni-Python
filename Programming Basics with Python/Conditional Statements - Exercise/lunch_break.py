import math

series_name = input()
episode_length = int(input())
break_time = int(input())

lunch_time = break_time / 8
chill_time = break_time / 4

time_left = break_time - lunch_time - chill_time

if time_left >= episode_length:
    print(f"You have enough time to watch {series_name} and left with {math.ceil(time_left - episode_length)} minutes free time.")
else:
    print(f"You don't have enough time to watch {series_name}, you need {math.ceil(episode_length - time_left)} more minutes.")
