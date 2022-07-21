version = input().split(".")
numbers = [int(i) for i in version]
numbers[-1] += 1
for i in range(len(numbers) - 1, -1, -1):
    if numbers[i] > 9:
        numbers[i] = 0
        if i >= 0:
            numbers[i - 1] += 1

print('.'.join(str(number) for number in numbers))





