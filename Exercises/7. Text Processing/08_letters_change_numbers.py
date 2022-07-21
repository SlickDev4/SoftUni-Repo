text = [x.strip() for x in input().split()]
result = 0

for element in text:
    first_letter = element[0]
    last_letter = element[-1]
    current_number = ''

    for number in element:
        if number.isdigit():
            current_number += number

    if first_letter.isupper():
        result += int(current_number) / (ord(first_letter) - 64)
    else:
        result += int(current_number) * (ord(first_letter) - 96)

    if last_letter.isupper():
        result -= ord(last_letter) - 64
    else:
        result += ord(last_letter) - 96

print(f"{result:.2f}")
