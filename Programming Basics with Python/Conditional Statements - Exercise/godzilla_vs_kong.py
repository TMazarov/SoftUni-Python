# decor for movie is 10% of the budget
# above 150 statist clothing discount of 10%

movie_budget = float(input())
number_of_statist = int(input())
clothing_price = float(input())  # per statist

decor_prize = movie_budget * 0.10
total_clothing_prize = number_of_statist * clothing_price

if number_of_statist > 150:
    total_clothing_prize = total_clothing_prize - (total_clothing_prize * 0.10)

final_prize = total_clothing_prize + decor_prize

if movie_budget >= final_prize:
    print("Action!")
    print(f"Wingard starts filming with {movie_budget - final_prize:.2f} leva left.")
else:
    print("Not enough money!")
    print(f"Wingard needs {final_prize - movie_budget:.2f} leva more.")
