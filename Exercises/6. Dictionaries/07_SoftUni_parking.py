number_of_cars = int(input())
registered = {}

for i in range(number_of_cars):
    command = input().split()
    user = command[1]
    if command[0] == "register":
        license_plate = command[2]

        if user not in registered.keys():
            registered[user] = license_plate
            print(f"{user} registered {license_plate} successfully")
        else:
            print(f"ERROR: already registered with plate number {license_plate}")

    elif command[0] == "unregister":
        if user in registered.keys():
            del registered[user]
            print(f"{user} unregistered successfully")
        else:
            print(f"ERROR: user {user} not found")

for key, value in registered.items():
    print(f"{key} => {value}")
