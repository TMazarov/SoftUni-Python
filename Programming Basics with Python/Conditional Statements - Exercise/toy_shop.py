# Puzzle price 2.60 lv
# Talking doll prize 3 lv
# Teddy Bear prize 4.10 lv
# Minion toy prize 8.20 lv
# Truck toy 2 lv
# --------------------------------------------------------------
# if total toys are above 50 apply 25% discount from total price
# 10% of total prize goes to rent

holiday_price = float(input())
number_of_puzzles = int(input())
number_of_talking_dolls = int(input())
number_of_teddy_bears = int(input())
number_of_minion_toys = int(input())
number_of_truck_toys = int(input())

total_number_of_toys = number_of_truck_toys + number_of_teddy_bears + number_of_talking_dolls + \
                       number_of_puzzles + number_of_minion_toys

total_prize_of_toys = (number_of_puzzles * 2.60) + (number_of_teddy_bears * 4.10) + (number_of_talking_dolls * 3)\
                      + (number_of_minion_toys * 8.20) + (number_of_truck_toys * 2)

if total_number_of_toys >= 50:
    total_prize_of_toys = total_prize_of_toys - (total_prize_of_toys * 0.25)
    total = total_prize_of_toys - (total_prize_of_toys * 0.10)
else:
    total = total_prize_of_toys - (total_prize_of_toys * 0.10)

if total >= holiday_price:
    print(f'Yes! {total - holiday_price:.2f} lv left.')
else:
    print(f'Not enough money! {holiday_price - total:.2f} lv needed.')

