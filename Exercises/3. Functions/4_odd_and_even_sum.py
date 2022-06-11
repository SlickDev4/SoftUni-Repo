def sum_of_odd_and_even(num):

    even_numbers = []
    odd_numbers = []

    sum_of_evens = 0
    sum_of_odds = 0

    for digit in str(num):
        if int(digit) % 2 == 0:
            even_numbers.append(digit)
        else:
            odd_numbers.append(digit)

    for even in even_numbers:
        sum_of_evens += int(even)

    for odd in odd_numbers:
        sum_of_odds += int(odd)

    print(f"Odd sum = {sum_of_odds}, Even sum = {sum_of_evens}")


number = int(input())

sum_of_odd_and_even(number)
