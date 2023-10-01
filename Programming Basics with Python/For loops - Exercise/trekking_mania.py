number_of_groups = int(input())


musala_group = 0
monblan_group = 0
kilimandjaro_group = 0
k2_group = 0
everest_group = 0

total_people = 0

for group in range(number_of_groups):
    group_size = int(input())
    total_people += group_size

    if group_size <= 5:
        musala_group += group_size
    elif group_size <= 12:
        monblan_group += group_size
    elif group_size <= 25:
        kilimandjaro_group += group_size
    elif group_size <= 40:
        k2_group += group_size
    else:
        everest_group += group_size

musala_percent = musala_group / total_people * 100
monblan_percent = monblan_group / total_people * 100
kilimandjaro_percent = kilimandjaro_group / total_people * 100
k2_percent = k2_group / total_people * 100
everest_percent = everest_group / total_people * 100

print(f'{musala_percent:.2f}%')
print(f'{monblan_percent:.2f}%')
print(f'{kilimandjaro_percent:.2f}%')
print(f'{k2_percent:.2f}%')
print(f'{everest_percent:.2f}%')
