width = int(input())
lenght = int(input())
height= int(input())

total_space = width * lenght * height

curr_command = input()
while curr_command != "Done":
    boxes = int(curr_command)
    total_space -= boxes

    if total_space <= 0:
        break

    curr_command = input()

if curr_command == "Done":
    print(f"{total_space} Cubic meters left.")
else:
    print(f"No more free space! You need {abs(total_space)} Cubic meters more.")