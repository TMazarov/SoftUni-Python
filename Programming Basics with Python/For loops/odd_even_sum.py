number = int(input())

odd_number = 0
even_number = 0

for i in range(number):
    current_number = int(input())

    if i % 2 == 0:
        even_number += current_number

    else:
        odd_number += current_number

if even_number == odd_number:
    print(f"Yes")
    print(f"Sum = {even_number}")
else:
    diff = abs(even_number - odd_number)
    print(f"No")
    print(f"Diff = {diff}")