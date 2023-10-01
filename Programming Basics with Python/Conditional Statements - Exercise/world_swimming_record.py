import math

record_time = float(input())
distance = float(input())
time = float(input())

total_distance = distance * time
time_added = math.floor(distance / 15) * 12.5
total_time = total_distance + time_added

if total_time < record_time:
    print(f"Yes, he succeeded! The new world record is {total_time:.2f} seconds.")
else:
    print(f"No, he failed! He was {total_time - record_time:.2f} seconds slower.")


