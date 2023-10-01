# price for 1 pack of pens - 5.80 lv
# price for 1 pack of markers - 7.20 lv
# price for 1 lt. of chemicals - 1.20 lv

pack_of_pens = int(input())
pack_of_markers = int(input())
liters_of_checmicals = int(input())

percent_discount = int(input()) / 100

total_price_for_pens = pack_of_pens * 5.80
total_price_for_markers = pack_of_markers * 7.20
total_price_for_chemicals = liters_of_checmicals * 1.20

total_price = total_price_for_chemicals + total_price_for_pens + total_price_for_markers
discounted_price = total_price - (total_price * percent_discount)

print(discounted_price)
