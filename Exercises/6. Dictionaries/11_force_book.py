forces = {}
command = input()
while command != "Lumpawaroo":
    if " | " in command:
        split_command = command.split(" | ")
        side, user = split_command
        present = False
        for value in forces.values():
            if user in value:
                present = True
                break
        if not present:
            if side not in forces.keys():
                forces[side] = [user]
            else:
                forces[side].append(user)
    else:
        split_command = command.split(" -> ")
        user, side = split_command
        for key, value in forces.items():
            if user in value:
                forces[key].pop(value.index(user))
                break
        if side not in forces.keys():
            forces[side] = [user]
        else:
            forces[side] += [user]
        print(f"{user} joins the {side} side!")
    command = input()

for side in forces.keys():
    if len(forces[side]) > 0:
        print(f"Side: {side}, Members: {len(forces[side])}")
        [print(f"! {user}") for user in forces[side]]

