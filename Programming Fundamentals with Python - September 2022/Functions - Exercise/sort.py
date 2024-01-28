def sorting_func(sequence_of_numbers):
    sorted_list = sorted(sequence_of_numbers)

    return sorted_list


numbers = [int(x) for x in input().split()]
print(sorting_func(numbers))
