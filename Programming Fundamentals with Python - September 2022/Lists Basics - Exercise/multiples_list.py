factor = int(input())
count = int(input())

multiples_lst = []

for number in range(1, count + 1):
    multiples_lst.append(number * factor)


print(multiples_lst)
