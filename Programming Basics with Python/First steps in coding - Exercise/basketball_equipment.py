# shoes price is 40% from yearly tax
# Outfit price is 20% from shoes price
# Ball price is 1/4 from outfit price
# Accessories price is 1/5 from ball price

yearly_tax_for_practice = int(input())

shoes_price = yearly_tax_for_practice - (yearly_tax_for_practice * 0.40)
outfit_price = shoes_price - (shoes_price * 0.20)
ball_price = outfit_price / 4
accessories_price = ball_price / 5

total_price = shoes_price + outfit_price + ball_price + accessories_price + yearly_tax_for_practice

print(total_price)
