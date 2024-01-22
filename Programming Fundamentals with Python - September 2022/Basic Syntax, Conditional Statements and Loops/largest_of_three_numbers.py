first_number = int(input())
second_number = int(input())
third_number = int(input())

biggest_number = 0

if second_number < first_number > third_number:
    biggest_number = first_number
elif first_number < second_number > third_number:
    biggest_number = second_number
else:
    biggest_number = third_number

print(biggest_number)


# n1, n2, n3 = int(input()), int(input()), int(input())

# print(max(n1, n2, n3))
