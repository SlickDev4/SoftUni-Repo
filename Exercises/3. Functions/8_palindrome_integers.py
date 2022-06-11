def palindrome_numbers(number):
    for num in number:
        if str(num) == str(num)[::-1]:
            print(True)
        else:
            print(False)


numbers = [int(i) for i in input().split(", ")]

palindrome_numbers(numbers)
