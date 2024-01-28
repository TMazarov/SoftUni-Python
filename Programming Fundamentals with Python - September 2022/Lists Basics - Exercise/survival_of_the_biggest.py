numbers_list = [int(x) for x in input().split()]
numbers_to_remove = int(input())

biggest_nums_lst = []

for _ in range(numbers_to_remove):
    numbers_list.remove(min(numbers_list))

print(*numbers_list, sep=', ')
