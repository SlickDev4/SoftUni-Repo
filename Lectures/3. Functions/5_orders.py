def calculate_order(product, quantity):
    result = None
    if product == "coffee":
        result = coffee * quantity
    elif product == "coke":
        result = coke * quantity
    elif product == "water":
        result = water * quantity
    elif product == "snacks":
        result = snacks * quantity

    return f"{result:.2f}"


coffee = 1.50
coke = 1.40
water = 1.00
snacks = 2.00

command = input()
quant = int(input())

print(calculate_order(command, quant))