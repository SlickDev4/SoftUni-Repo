first_string, second_string = input().split()
result = 0

if len(first_string) > len(second_string):

    for index in range(len(second_string)):
        result += ord(first_string[index]) * ord(second_string[index])

    for index in range(len(second_string), len(first_string)):
        result += ord(first_string[index])

elif len(second_string) > len(first_string):

    for index in range(len(first_string)):
        result += ord(first_string[index]) * ord(second_string[index])

    for index in range(len(first_string), len(second_string)):
        result += ord(second_string[index])

elif len(first_string) == len(second_string):

    for index in range(len(first_string)):
        result += ord(first_string[index]) * ord(second_string[index])

print(result)
