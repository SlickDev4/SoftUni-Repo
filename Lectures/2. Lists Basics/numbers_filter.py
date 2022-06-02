lines = int(input())

my_list = [int(input()) for _ in range(lines)]
result = []

command = input()

for num in my_list:

    result_command = (
            command == 'even' and num % 2 == 0 or
            command == 'odd' and num % 2 != 0 or
            command == 'positive' and num >= 0 or
            command == 'negative' and num < 0
    )

    if result_command:
        result.append(num)

print(result)
