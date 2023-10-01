# Price for nylon - 1.50 for sq meter
# Price for paint - 14.50 for liter
# Price for thinner - 5.00 for liter
# -----------------------------------
# Add bag price - 0.40
# Add additional 10% for paint
# Add additional 2 sq meters for nylon

# Price for labor is 30% of total price for all the materials

sq_meters_nylon_needed = int(input())
paint_needed = int(input())
thinner_needed = int(input())
labor_hours = int(input())

bag = 0.40

total_price_for_nylon = (sq_meters_nylon_needed + 2) * 1.50
total_price_for_paint = (paint_needed * 1.1) * 14.50
total_price_for_thinner = thinner_needed * 5.00

total_price_for_materials = total_price_for_nylon + total_price_for_paint + total_price_for_thinner + bag
labors_pay = total_price_for_materials * 0.3 * labor_hours

final_price = total_price_for_materials + labors_pay

print(final_price)
