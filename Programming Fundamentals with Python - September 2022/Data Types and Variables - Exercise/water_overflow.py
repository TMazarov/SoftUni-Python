tank_capacity = 255
number_of_lines = int(input())

water_tank = 0

for i in range(number_of_lines):
    liters_of_water = int(input())

    if liters_of_water <= tank_capacity:
        tank_capacity -= liters_of_water
        water_tank += liters_of_water
    else:
        print('Insufficient capacity!')

print(f'{water_tank:.0f}')
