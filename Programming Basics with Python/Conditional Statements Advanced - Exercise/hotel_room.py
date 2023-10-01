month = input()
stays = int(input())

studio_price = 0
apartment_price = 0

if month == "May" or month == "October":
    studio_price = 50
    apartment_price = 65

    if 7 < stays < 14:
        studio_price -= studio_price * 0.05
    elif stays > 14:
        studio_price -= studio_price * 0.30
        apartment_price -= apartment_price * 0.10

elif month == "June" or month == "September":
    studio_price = 75.20
    apartment_price = 68.70

    if stays > 14:
        studio_price -= studio_price * 0.20
        apartment_price -= apartment_price * 0.10

elif month == "July" or month == "August":
    studio_price = 76
    apartment_price = 77

    if stays > 14:
        apartment_price -= apartment_price * 0.10


apartment_price *= stays
studio_price *= stays

print(f"Apartment: {apartment_price:.2f} lv.")
print(f"Studio: {studio_price:.2f} lv.")
