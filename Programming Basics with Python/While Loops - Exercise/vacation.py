money_needed = float(input())
saved_money = float(input())

days_counter = 0
spending_counter = 0

while saved_money < money_needed and spending_counter < 5:
    command = input()
    money = float(input())

    days_counter += 1

    if command == "save":
        saved_money += money
        spending_counter = 0

    elif command == "spend":
        saved_money -= money
        spending_counter += 1

        if saved_money < 0:
            saved_money = 0

if spending_counter == 5:
    print("You can't save the money.")
    print(days_counter)

if saved_money >= money_needed:
    print(f"You saved the money for {days_counter} days.")
