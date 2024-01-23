coffee_needed = 0
events_list = ['coding', 'dog', 'cat', 'movie']
events_list_upper_case = str(events_list).upper()
while True:

    command = input()

    if command == 'END':
        break

    elif command in events_list:
        coffee_needed += 1

    elif command in events_list_upper_case:
        coffee_needed += 2

    else:
        continue

if coffee_needed > 5:
    print('You need extra sleep')
else:
    print(f'{coffee_needed}')
