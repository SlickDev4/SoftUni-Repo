text = input()
encrypted_text = ""

for element in text:
    encrypted_text += chr(ord(element) + 3)

print(encrypted_text)
