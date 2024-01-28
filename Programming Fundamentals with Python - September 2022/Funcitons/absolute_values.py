def abs_values_func(numbers):
    numbers_lst = [float(x) for x in numbers]
    abs_values_lst = []

    for number in numbers_lst:
        abs_values_lst.append(abs(number))

    return abs_values_lst


numbers_sequence = input().split()
print(abs_values_func(numbers_sequence))
