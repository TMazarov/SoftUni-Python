city = input()
sales = float(input())

valid_cities = ["Sofia", "Varna", "Plovdiv"]

if city not in valid_cities or sales < 0:
    print("error")

elif 0 <= sales <= 500:
    if city == valid_cities[0]:
        print(f"{sales * 0.05:.2f}")
    elif city == valid_cities[1]:
        print(f"{sales * 0.045:.2f}")
    elif city == valid_cities[2]:
        print(f"{sales * 0.055:.2f}")
elif 500 <= sales <= 1000:
    if city == valid_cities[0]:
        print(f"{sales * 0.07:.2f}")
    elif city == valid_cities[1]:
        print(f"{sales * 0.075:.2f}")
    elif city == valid_cities[2]:
        print(f"{sales * 0.08:.2f}")
elif 1000 <= sales <= 10000:
    if city == valid_cities[0]:
        print(f"{sales * 0.08:.2f}")
    elif city == valid_cities[1]:
        print(f"{sales * 0.1:.2f}")
    elif city == valid_cities[2]:
        print(f"{sales * 0.12:.2f}")
elif sales > 10000:
    if city == valid_cities[0]:
        print(f"{sales * 0.12:.2f}")
    elif city == valid_cities[1]:
        print(f"{sales * 0.13:.2f}")
    elif city == valid_cities[2]:
        print(f"{sales * 0.145:.2f}")
