final_message = []

while True:
    commands = input().split()
    command = commands[0]

    if command == "end":
        break

    for index, element in enumerate(commands):
        if index == 0:
            continue
        if command == "Chat":
            final_message.append(element)
        elif command == "Delete":
            if element in final_message:
                final_message.remove(element)
        elif command == "Edit":
            if element in final_message:
                index = final_message.index(element)
                final_message.pop(index)
                final_message.insert(index, commands[2])
        elif command == "Pin":
            if element in final_message:
                final_message.remove(element)
                final_message.insert(len(final_message), element)
        elif command == "Spam":
            final_message.append(element)

print("\n".join(final_message))
