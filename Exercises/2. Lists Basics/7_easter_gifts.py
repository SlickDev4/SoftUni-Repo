gifts = input().split()
command = ''
running = True
final_gifts = []

while running:
    command = input().split()

    if command == ['No', 'Money']:
        running = False
        break

    for gift in gifts:

        if command == ["OutOfStock", f"{gift}"]:
            i = gifts.index(gift)
            gifts.pop(i)
            gifts.insert(i, 'None')

        if len(command) == 3:
            if command[0] == "Required" and command[1] == f"{command[len(command) - 2]}":
                if int(command[2]) < len(gifts):
                    gifts.pop(int(command[2]))
                    gifts.insert(int(command[2]), command[len(command) - 2])
                    break

        if command == ["JustInCase", f"{command[len(command) - 1]}"]:
            gifts.pop(-1)
            gifts.append(command[len(command) - 1])
            break

for word in gifts:
    if word == "None":
        gifts.remove(word)

print(*gifts)
