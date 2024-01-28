def is_num_palindrome(nums):
    results = []

    for num in nums:
        results.append(num == num[::-1])

    return results


nums = [x for x in input().split(', ')]
result = is_num_palindrome(nums)

print(*result, sep='\n')
