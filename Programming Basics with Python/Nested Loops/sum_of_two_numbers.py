starting_number = int(input())
end_number = int(input())

magic_number = int(input())


counter = 0
is_found = False

for x in range(starting_number, end_number + 1):
    for y in range(starting_number, end_number + 1):
        counter += 1

        if x + y == magic_number:
            is_found = True
            print(f"Combination N:{counter} ({x} + {y} = {magic_number}) ")
            break

    if is_found:
        break

if not is_found:
    print(f"{counter} combinations - neither equals {magic_number}")
