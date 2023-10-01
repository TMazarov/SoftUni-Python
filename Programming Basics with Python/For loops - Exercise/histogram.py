n = int(input())

r1_cnt = 0
r2_cnt = 0
r3_cnt = 0
r4_cnt = 0
r5_cnt = 0

for i in range(0, n):
    current_numbers = int(input())

    if current_numbers < 200:
        r1_cnt += 1
    elif current_numbers <= 399:
        r2_cnt += 1
    elif current_numbers <= 599:
        r3_cnt += 1
    elif current_numbers <= 799:
        r4_cnt += 1
    else:
        r5_cnt += 1

p1 = (r1_cnt / n) * 100
p2 = (r2_cnt / n) * 100
p3 = (r3_cnt / n) * 100
p4 = (r4_cnt / n) * 100
p5 = (r5_cnt / n) * 100

print(f"{p1:.2f}%")
print(f"{p2:.2f}%")
print(f"{p3:.2f}%")
print(f"{p4:.2f}%")
print(f"{p5:.2f}%")