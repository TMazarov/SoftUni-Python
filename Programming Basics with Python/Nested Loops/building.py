number_of_floors = int(input())
number_of_rooms_per_floor = int(input())

flat_name = ''

for floor in range(number_of_floors, 0, -1):
    for room in range(number_of_rooms_per_floor):
        flat_number = str(floor) + str(room)

        if floor == number_of_floors:
            flat_name = (f"L{flat_number}")

        elif floor % 2 != 0:
            flat_name = (f"A{flat_number}")

        else:
            flat_name = (f"O{flat_number}")

        print(flat_name, end=" ")

    print()
