n = int(input())

for i in range(n):
    new_string = input()

    if ',' in new_string or '.' in new_string or '_' in new_string:
        print(f'{new_string} is not pure!')
    else:
        print(f'{new_string} is pure.')

