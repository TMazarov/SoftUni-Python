n = int(input())

positives = []
negatives = []


for i in range(n):
    current_int = int(input())

    if current_int >= 0:
        positives.append(current_int)
    else:
        negatives.append(current_int)


print(positives)
print(negatives)
print(f"Count of positives: {len(positives)}")
print(f'Sum of negatives: {sum(negatives)}')
