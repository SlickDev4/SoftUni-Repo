product_price = {}
product_quantity = {}

while True:
    command = input().split()
    if command[0] == "buy":
        break
    product = command[0]
    price = command[1]
    quantity = int(command[2])

    product_price[product] = price

    if product not in product_quantity.keys():
        product_quantity[product] = quantity
    else:
        product_quantity[product] += quantity

for key, value in product_price.items():
    for key1, value1 in product_quantity.items():
        if key == key1:
            print(f"{key} -> {(float(value) * float(value1)):.2f}")




