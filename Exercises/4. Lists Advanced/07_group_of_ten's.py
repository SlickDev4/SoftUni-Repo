nums = input().split(", ")
numbers = [int(i) for i in nums]
max_number = max(numbers)

if max_number % 10 == 0:
    groups = max_number // 10
else:
    groups = max_number // 10 + 1

boundary = 0

main_list = []
small_list = []

while len(numbers) > 0:
    boundary += 10
    for number in numbers:
        if number <= boundary:
            small_list.append(number)
            numbers = [x for x in numbers if x not in small_list]
    main_list.append(small_list.copy())
    small_list.clear()
    print(f"Group of {boundary}'s: {main_list[int(boundary / 10 - 1)]}")










