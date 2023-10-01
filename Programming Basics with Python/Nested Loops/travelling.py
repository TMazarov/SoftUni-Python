while True:

    destination = input()
    if destination == "End":
        break

    budget = float(input())

    total_money = 0

    while True:

        saved_money = float(input())
        total_money += saved_money
        if total_money >= budget:
            print(f"Going to {destination}!")
            break
