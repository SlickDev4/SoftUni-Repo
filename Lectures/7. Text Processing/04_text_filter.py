bans = input().split(", ")
text = input()

for element in bans:
    while element in text:
        text = text.replace(element, len(element) * "*")

print(text)
