steps_cnt = 0

curr_command = input()
while curr_command != "Going home":
    steps = int(curr_command)
    steps_cnt += steps

    if steps_cnt >= 10000:
        break

    curr_command = input()

if curr_command == "Going home":
    steps_home = int(input())
    steps_cnt += steps_home

steps_diff = abs(steps_cnt - 10000)

if steps_cnt >= 10000:
    print("Goal reached! Good job!")
    print(f"{steps_diff} steps over the goal!")
else:
    print(f"{steps_diff} more steps to reach goal.")

