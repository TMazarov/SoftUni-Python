total_price = 0

number_of_orders = int(input())

for order in range(number_of_orders):
    price_per_capsule = float(input())
    days = int(input())
    capsules_per_day = int(input())

    coffe_price = capsules_per_day * days * price_per_capsule

    if 0.01 <= price_per_capsule <= 100.00 and 1 <= days <= 31 and 1 <= capsules_per_day <= 2000:
        total_price += coffe_price
        print(f'The price for the coffee is: ${coffe_price:.2f}')

print(f'Total: ${total_price:.2f}')
