def even_numbers(sequence_of_numbers):

    even_nums = list(filter(lambda x: x % 2 == 0, sequence_of_numbers))

    return even_nums


num_sequence = [int(x) for x in input().split()]
print(even_numbers(num_sequence))

