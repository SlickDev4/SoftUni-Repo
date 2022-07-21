numbers = [int(i) for i in input().split(", ")]
result = [index for index, number in enumerate(numbers) if number % 2 == 0]
print(result)