square_meters_for_landscaping = float(input())

total_price_for_landscaping = square_meters_for_landscaping * 7.61

discount = total_price_for_landscaping * 0.18

total_price_with_discount = total_price_for_landscaping - discount

print(f"The final price is: {total_price_with_discount} lv.")
print(f"The discount is: {discount} lv.")
