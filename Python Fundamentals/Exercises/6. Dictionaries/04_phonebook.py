phonebook = {}

while True:
    main_input = input().split("-")

    if len(main_input) == 1:
        for i in range(int(main_input[0])):
            name = input()

            if name in phonebook.keys():
                print(f"{name} -> {phonebook[name]}")
            else:
                print(f"Contact {name} does not exist.")
        break

    person = main_input[0]
    number = main_input[1]

    phonebook[person] = number

