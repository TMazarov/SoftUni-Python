# prices per night
room_for_one_person_price = 18
apartment_price = 25
president_apartment_price = 35

number_of_stays = int(input()) - 1
room_type = input()
review = input()

total = 0

# discounts
if room_type == "apartment":
    total = number_of_stays * apartment_price
    if number_of_stays < 10:
        total -= total * 0.30
    elif 10 <= number_of_stays <= 15:
        total -= total * 0.35
    else:
        total -= total * 0.50

elif room_type == "president apartment":
    total = number_of_stays * president_apartment_price

    if number_of_stays < 10:
        total -= total * 0.10
    elif 10 <= number_of_stays <= 15:
        total -= total * 0.15
    else:
        total -= total * 0.20
else:
    total = number_of_stays * room_for_one_person_price


if review == "positive":
    total += total * 0.25
else:
    total -= total * 0.10

print(f"{total:.2f}")
