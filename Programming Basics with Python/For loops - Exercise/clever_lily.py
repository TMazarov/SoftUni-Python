lilys_age = int(input())
washing_machine_price = float(input())
toy_price = int(input()) # per toy

toys_cnt = 0
money_saved = 0


for age in range(1, lilys_age + 1):
    if age % 2 != 0:
        toys_cnt += 1
    else:
        money_received = (age * 5) - 1
        money_saved += money_received

money_from_toys = toys_cnt * toy_price
money_saved += money_from_toys

if money_saved >= washing_machine_price:
    print(f"Yes! {money_saved - washing_machine_price:.2f}")
else:
    print(f"No! {washing_machine_price - money_saved:.2f}")
