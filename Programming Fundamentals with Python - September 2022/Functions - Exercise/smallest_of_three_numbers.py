def find_the_smallest(a, b, c):
    if b > a < c:
        return a
    elif a > b < c:
        return b
    else:
        return c


first_num, second_num, third_num = int(input()), int(input()), int(input())

print(find_the_smallest(first_num,second_num,third_num))
