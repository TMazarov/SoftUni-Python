flowers_type = input()
number_of_flowers = int(input())
budget = int(input())

total = 0

if flowers_type == "Roses":
    total = number_of_flowers * 5
    if number_of_flowers > 80:
        total = total - (total * 0.10)

elif flowers_type == "Dahlias":
    total = number_of_flowers * 3.80
    if number_of_flowers > 90:
        total = total - (total * 0.15)

elif flowers_type == "Tulips":
    total = number_of_flowers * 2.80
    if number_of_flowers > 80:
        total = total - (total * 0.15)

elif flowers_type == "Narcissus":
    total = number_of_flowers * 3
    if number_of_flowers < 120:
        total = total + (total * 0.15)

elif flowers_type == "Gladiolus":
    total = number_of_flowers * 2.50
    if number_of_flowers < 80:
        total = total + (total * 0.20)

if budget >= total:
    print(f"Hey, you have a great garden with {number_of_flowers} {flowers_type} and {budget - total:.2f} leva left.")
else:
    print(f"Not enough money, you need {total - budget:.2f} leva more.")
