def odd_and_even_sum(number):
    odd_lst = []
    even_lst = []

    for num in number:
        if int(num) % 2 == 0:
            even_lst.append(int(num))
        else:
            odd_lst.append(int(num))

    sum_of_odd = sum(odd_lst)
    sum_of_even = sum(even_lst)

    return f'Odd sum = {sum_of_odd}, Even sum = {sum_of_even}'


n = input()

print(odd_and_even_sum(n))
