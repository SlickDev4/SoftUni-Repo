text = input()
new_text = ""
power = 0

for index in range(len(text)):
    if power > 0 and text[index] != ">":
        power -= 1
    elif text[index] == ">":
        power += int(text[index + 1])
        new_text += text[index]
    else:
        new_text += text[index]

print(new_text)
