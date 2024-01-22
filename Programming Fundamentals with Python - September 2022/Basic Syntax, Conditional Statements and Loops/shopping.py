budget = int(input())

while True:
    command = input()

    if command == 'End':
        print('You bought everything needed.')
        break
    else:
        price_per_product = int(command)
        budget -= price_per_product

        if budget < 0:
            print('You went in overdraft!')
            break

