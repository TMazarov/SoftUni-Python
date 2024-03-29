group_size = int(input())
days_of_adventure = int(input())

coins_earned = 0
food_per_day_cost = 2

for day in range(1, days_of_adventure + 1):

    if day % 10 == 0:
        group_size -= 2

    if day % 15 == 0:
        group_size += 5

    coins_earned += (50 - (group_size * food_per_day_cost))

    if day % 3 == 0:
        coins_earned -= 3 * group_size

    if day % 5 == 0:
        coins_earned += 20 * group_size
        if day % 3 == 0:
            coins_earned -= 2 * group_size


coins_per_person = int(coins_earned / group_size)

print(f"{group_size} companions received {coins_per_person} coins each.")
