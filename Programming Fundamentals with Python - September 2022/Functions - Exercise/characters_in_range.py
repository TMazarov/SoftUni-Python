def character_in_range(a, b):
    chars_lst = []

    for char in range(ord(a) + 1, ord(b)):
        chars_lst.append(chr(char))

    return chars_lst


starting_string, ending_string = input(), input()

result = character_in_range(starting_string, ending_string)
print(*result, sep=' ')
