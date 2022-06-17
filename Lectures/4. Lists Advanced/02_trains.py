number_of_wagons = int(input())
train = [0 for i in range(number_of_wagons)]

while True:
    command = input()

    if command == "End":
        break

    data = command.split()
    current_command = data[0]

    if current_command == "add":
        people_to_add = int(data[1])
        train[-1] += people_to_add

    elif current_command == "insert":
        index = int(data[1])
        number_of_people = int(data[2])
        train[index] += number_of_people

    elif current_command == "leave":
        index = int(data[1])
        people_to_leave = int(data[2])
        train[index] -= people_to_leave

print(train)