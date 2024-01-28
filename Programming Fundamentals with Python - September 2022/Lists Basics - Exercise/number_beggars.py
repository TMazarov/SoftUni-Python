numbers = [int(x) for x in input().split(', ')]
beggars_count = int(input())

beggars_sum_lst = [0] * beggars_count


for i in range(len(numbers)):
    beggar_index = i % beggars_count

    beggars_sum_lst[beggar_index] += numbers[i]


print(beggars_sum_lst)
