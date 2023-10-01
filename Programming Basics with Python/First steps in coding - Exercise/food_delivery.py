# Chicken Menu price - 10.35 lv
# Fish Menu price - 12.40 lv
# Veggie Menu price - 8.15 lv

# Delivery price - 2.50 lv

# Dessert price is 20% from total price without delivery price

chicken_menus = int(input()) * 10.35
fish_menus = int(input()) * 12.40
veggie_menus = int(input()) * 8.15

total = chicken_menus + fish_menus + veggie_menus

dessert = total * 0.20
delivery_cost = 2.50

final_price = total + dessert + delivery_cost

print(final_price)
