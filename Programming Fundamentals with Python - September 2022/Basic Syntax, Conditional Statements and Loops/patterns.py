pattern_number = int(input())

for i in range(1, pattern_number + 1):
    for j in range(0, i):
        print('*', end='')
    print()

for i in range(pattern_number - 1, 0, -1):
    for j in range(0, i):
        print('*', end='')
    print()
