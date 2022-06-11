def get_chars(char_1, char_2):
    char_list = []

    for char in range(ord(char_1) + 1, ord(char_2)):
        char_list.append(chr(char))

    return char_list


first_char = input()
second_char = input()

result = get_chars(first_char, second_char)

print(" ".join(result))
