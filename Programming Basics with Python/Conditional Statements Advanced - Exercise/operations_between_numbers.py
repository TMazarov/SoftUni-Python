number_one = int(input())
number_two = int(input())
operator = input()

result = 0
odd_or_even = ""

if operator == "+":
    result = number_one + number_two

elif operator == "-":
    result = number_one - number_two

elif operator == "*":
    result = number_one * number_two

elif operator == "/":
    if number_two == 0:
        print(f"Cannot divide {number_one} by zero")
    else:
        result = number_one / number_two

elif operator == "%":
    if number_two == 0:
        print(f"Cannot divide {number_one} by zero")
    else:
        result = number_one % number_two

if result % 2 == 0:
    odd_or_even = "even"
else:
    odd_or_even = "odd"

if operator == "+" or operator == "-" or operator == "*":
    print(f"{number_one} {operator} {number_two} = {result} - {odd_or_even}")

elif operator == "/" and number_two != 0:
    print(f"{number_one} {operator} {number_two} = {result:.2f}")

elif operator == "%" and number_two != 0:
    print(f"{number_one} {operator} {number_two} = {result}")
