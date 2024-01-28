def factorial_division(num):
    if num == 0 or num == 1:
        return 1
    else:
        return num * factorial_division(num - 1)


def calculate_and_print(a, b):
    fact_of_a = factorial_division(a)
    fact_of_b = factorial_division(b)

    result = fact_of_a / fact_of_b

    return f'{result:.2f}'


first_num = int(input())
second_num = int(input())

print(calculate_and_print(first_num, second_num))
