cake_lenght = int(input())
cake_width = int(input())

cake_pieces = cake_width * cake_lenght

curr_command = input()
while curr_command != "STOP":
    pieces = int(curr_command)
    cake_pieces -= pieces

    if cake_pieces <= 0:
        break

    curr_command = input()

if curr_command == "STOP":
    print(f"{cake_pieces} pieces are left.")
else:
    print(f"No more cake left! You need {abs(cake_pieces)} pieces more.")