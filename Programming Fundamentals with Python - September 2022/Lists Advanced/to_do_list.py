tasks = []

while True:

    command = input()

    if command == "End":
        break
    split_command = command.split("-")
    priority_command = int(split_command[0])
    current_task = split_command[1]

    tasks.append((priority_command, current_task))

sorted_tasks = [task_data[1] for task_data in sorted(tasks)]
print(sorted_tasks)

