def add_and_subtract(a, b, c):

    def sum_numbers(a, b):
        return a + b

    def subtract(number, c):
        return number - c

    sum_result = sum_numbers(first_num, second_num)
    subtract_result = subtract(sum_result, third_num)

    return subtract_result


first_num, second_num, third_num = int(input()), int(input()), int(input())

print(add_and_subtract(first_num,second_num,third_num))
