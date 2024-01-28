def is_perfect_num(num):
    if num <= 0:
        return "It's not so perfect."

    divisors_sum = sum(divisor for divisor in range(1, number) if number % divisor == 0)

    if divisors_sum == number:
        return "We have a perfect number!"
    else:
        return "It's not so perfect."


number = int(input())
print(is_perfect_num(number))
