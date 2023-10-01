product = input()
day_of_the_week = input()
quantity = float(input())

week_day_prices = {'banana': 2.50, 'apple': 1.20, 'orange': 0.85, 'grapefruit': 1.45,
                   'kiwi': 2.70, 'pineapple': 5.50, 'grapes': 3.85}

weekend_prices = {'banana': 2.70, 'apple': 1.25, 'orange': 0.90, 'grapefruit': 1.60,
                  'kiwi': 3.00, 'pineapple': 5.60, 'grapes': 4.20}

week_days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']
weekend = ["Saturday", 'Sunday']

if day_of_the_week in weekend:
    if product in weekend_prices.keys():
        total_amount = weekend_prices[product] * quantity
        print(f'{total_amount:.2f}')
    else:
        print("error")
elif day_of_the_week in week_days:
    if product in week_day_prices.keys():
        total_amount = week_day_prices[product] * quantity
        print(f'{total_amount:.2f}')
    else:
        print("error")
else:
    print("error")
