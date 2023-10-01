import math

number_of_tournaments = int(input())
starting_points = int(input())

points = 0
total_points = starting_points
win_tournaments = 0

for _ in range(number_of_tournaments):
    current_position = input()

    if current_position == "W":
        total_points += 2000
        points += 2000
        win_tournaments += 1
    elif current_position == "F":
        total_points += 1200
        points += 1200
    elif current_position == "SF":
        total_points += 720
        points += 720

average_points = points / number_of_tournaments
win_tournaments_percent = (win_tournaments / number_of_tournaments) * 100

print(f"Final points: {total_points}")
print(f"Average points: {math.floor(average_points)}")
print(f"{win_tournaments_percent:.2f}%")
