n = int(input())

even_lst = []
odd_lst = []
negatives_lst = []
positives_lst = []

for i in range(n):
    integers = int(input())

    if integers >= 0:
        positives_lst.append(integers)
        if integers % 2 == 0:
            even_lst.append(integers)
        else:
            odd_lst.append(integers)
    else:
        negatives_lst.append(integers)
        if integers % 2 == 0:
            even_lst.append(integers)
        else:
            odd_lst.append(integers)

command = input()

if command == 'even':
    print(even_lst)
elif command == 'odd':
    print(odd_lst)
elif command == 'positive':
    print(positives_lst)
else:
    print(negatives_lst)

