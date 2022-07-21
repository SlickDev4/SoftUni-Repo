products = input().split()
products_for_search = input().split()

products_dict = {}

for i in range(0, len(products), 2):
    products_dict[products[i]] = int(products[i + 1])

for element in products_for_search:
    if element in products_dict:
        print(f"We have {products_dict.get(element)} of {element} left")
    else:
        print(f"Sorry, we don't have {element}")