string = input()
numbers = ""
letters = ""
symbols = ""

for element in string:
    if element.isdigit():
        numbers += element
    elif element.isalpha():
        letters += element
    else:
        symbols += element

print(numbers)
print(letters)
print(symbols)
