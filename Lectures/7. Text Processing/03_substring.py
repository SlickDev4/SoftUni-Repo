first_string = input()
second_string = input()

while True:
    final_string = second_string.replace(first_string, "")
    if first_string not in second_string:
        break
    second_string = final_string

print(final_string)
