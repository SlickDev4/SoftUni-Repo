characters = input()
new_string = ""

for index, character in enumerate(characters):
    try:
        if character != characters[index + 1]:
            new_string += character
    except IndexError:
        new_string += character

print(new_string)
