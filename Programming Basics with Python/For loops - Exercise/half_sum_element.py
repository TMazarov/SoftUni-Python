import sys

n = int(input())

numb_sum = 0
max_number = -sys.maxsize

for i in range(0, n):
    current_number = int(input())
    if current_number > max_number:
        max_number = current_number
    numb_sum += current_number

numb_sum -= max_number

if numb_sum == max_number:
    print("Yes")
    print(f"Sum = {numb_sum}")

else:
    diff = abs(numb_sum - max_number)
    print("No")
    print(f"Diff = {diff}")