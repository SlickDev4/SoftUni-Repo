to_do_list = []

while True:
    command = input().split("-")

    if command[0] == "End":
        break

    importance = int(command[0])
    task = command[1]

    to_do_list += [(importance, task)]

sorted_list = [tasks[1] for tasks in sorted(to_do_list)]
print(sorted_list)