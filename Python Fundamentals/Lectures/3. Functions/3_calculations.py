def calculate(a, b, operation):
    result = None
    if operation == "multiply":
        result = a * b
    elif operation == "divide":
        result = int(a / b)
    elif operation == "add":
        result = a + b
    elif operation == "subtract":
        result = a - b

    return result


operator = input()
first_num = int(input())
second_num = int(input())

print(calculate(first_num, second_num, operator))
