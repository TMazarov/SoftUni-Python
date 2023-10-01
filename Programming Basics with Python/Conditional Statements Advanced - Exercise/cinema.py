type_of_projection = input()
number_of_rows = int(input())
number_of_colums = int(input())

cinema_capacity = number_of_rows * number_of_colums

total_sum = 0

projections = ['Premiere', 'Normal', 'Discount']

if type_of_projection == projections[0]:
    total_sum = cinema_capacity * 12.00
elif type_of_projection == projections[1]:
    total_sum = cinema_capacity * 7.50
elif type_of_projection == projections[2]:
    total_sum = cinema_capacity * 5.00

print(f'{total_sum:.2f} leva')
