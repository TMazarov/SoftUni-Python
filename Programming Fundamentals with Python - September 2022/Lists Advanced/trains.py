number_of_wagons = int(input())
train = [0] * number_of_wagons

while True:

    command = input().split()

    if 'End' in command:
        break

    elif 'add' in command:
        # add the number of people in the LAST WAGON
        people = int(command[1])
        train[-1] += people

    elif 'insert' in command:
        # add the number of people at the given wagon
        index = int(command[1])
        people = int(command[2])

        train[index] += people

    elif 'leave' in command:
        # remove the number of people from the wagon
        index = int(command[1])
        people = int(command[2])

        train[index] -= people

print(train)
