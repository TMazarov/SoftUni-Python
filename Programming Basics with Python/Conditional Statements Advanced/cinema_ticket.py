current_day = input()

ticket_prices = {'Monday': 12, 'Tuesday': 12, 'Wednesday': 14, 'Thursday': 14, 'Friday': 12,
                 'Saturday': 16, 'Sunday': 16}

if current_day in ticket_prices.keys():
    print(ticket_prices[current_day])
