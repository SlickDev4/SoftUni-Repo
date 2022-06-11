def sum_numbers(a, b):
    return a + b


def subtract(result, c):
    return result - c


def add_and_subtract(a, b, c):
    sum_of_first_two_nums = sum_numbers(a, b)
    final_result = subtract(sum_of_first_two_nums, c)

    print(final_result)


first_num = int(input())
second_num = int(input())
third_num = int(input())

add_and_subtract(first_num, second_num, third_num)
