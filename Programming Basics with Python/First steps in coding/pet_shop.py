# Dog food price -> 2.50lv
# Cat food price -> 4 lv

dog_food_amount = int(input())
cat_food_amount = int(input())

total_dog_food_price = dog_food_amount * 2.50
total_cat_food_price = cat_food_amount * 4

total_price = total_dog_food_price + total_cat_food_price

print(f'{total_price} lv.')