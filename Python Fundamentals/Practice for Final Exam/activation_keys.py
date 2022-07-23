def contains_func(key: str, text: str):
    """
            Checks if the text (substring) is in the key from the input
            :param key
            :param text
            :return new_key
    """

    if text in key:
        return f"{key} contains {text}"
    else:
        return "Substring not found!"


def flip_func(key: str, side: str, start_index: int, end_index: int):
    """
            Changes the key to Upper or Lower letters in a specific range of indices
            :param key
            :param side
            :param start_index
            :param end_index
            :return new_key
    """

    new_key = ""
    for index, element in enumerate(key):
        if start_index <= index < end_index:
            if side == "Upper":
                new_key += element.upper()
            else:
                new_key += element.lower()
        else:
            new_key += element
    return new_key


def slice_func(key: str, start_index: int, end_index: int):
    """
            Deletes the key part within the indices
            :param key
            :param start_index
            :param end_index
            :return new_key
    """
    new_key = ""
    for index, element in enumerate(key):
        if not start_index <= index < end_index:
            new_key += element
    return new_key


raw_activation_key = input()
final_activation_key = raw_activation_key

while True:
    """
            1. Taking the command input in a while loop
            2. Checking if the command is Generate in order to break the loop
            3. Checking the type of command and collecting the needed data
            4. Calling the specified function and passing the dynamic data as arguments
    """

    command = input()
    if command == "Generate":
        break

    split_command = command.split(">>>")
    function = split_command[0]

    if function == "Contains":
        substring = split_command[1]
        print(contains_func(final_activation_key, substring))

    elif function == "Flip":
        sides = split_command[1]
        start_indices = int(split_command[2])
        end_indices = int(split_command[3])

        final_activation_key = flip_func(final_activation_key, sides, start_indices, end_indices)
        print(final_activation_key)

    elif function == "Slice":
        start_indices = int(split_command[1])
        end_indices = int(split_command[2])

        final_activation_key = slice_func(final_activation_key, start_indices, end_indices)
        print(final_activation_key)

print(f"Your activation key is: {final_activation_key}")
