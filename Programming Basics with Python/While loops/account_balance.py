total_amount = 0

while True:

    current_deposit = input()

    if current_deposit == "NoMoreMoney":
        break

    current_deposit = float(current_deposit)

    if current_deposit <= 0:
        print('Invalid operation!')
        break
    else:
        total_amount += current_deposit
        print(f'Increase: {current_deposit:.2f}')

print(f'Total: {total_amount:.2f}')
