def calculator(operator, a, b):

    if operator == 'multiply':
        return a * b
    elif operator == 'divide':
        return int(a / b)
    elif operator == 'add':
        return a + b
    elif operator == 'subtract':
        return a - b


operations = input()
first_number = int(input())
second_number = int(input())

print(calculator(operations, first_number, second_number))
