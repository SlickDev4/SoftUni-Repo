my_dict = {}
total_quantity = 0
while True:
    products = input().split(": ")

    key = products[0]
    value = int(products[1]) if key != "statistics" else 0

    if key == "statistics":
        break

    if key not in my_dict:
        my_dict[key] = value
    else:
        total_quantity += value

total_products = len(my_dict)
test = ""

for key, value in my_dict.items():
    test += f"- {key}: {value}\n"

print(f"Products in stock:\n{test}Total Products: {total_products}\nTotal Quantity: {total_quantity}")