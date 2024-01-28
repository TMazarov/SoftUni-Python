def rounding(numbers_lst):
    rnd_lst = []

    for num in numbers_lst:
        rnd_lst.append(round(num))

    return rnd_lst


numbers = [float(x) for x in input().split()]

print(rounding(numbers))
