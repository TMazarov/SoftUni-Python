def min_max_and_sum_func(nums):
    min_num = min(nums)
    max_num = max(nums)
    sum_of_nums = sum(nums)

    return (f"The minimum number is {min_num}\n"
            f"The maximum number is {max_num}\n"
            f"The sum number is: {sum_of_nums} \n")


numbers = [int(x) for x in input().split()]
print(min_max_and_sum_func(numbers))
