products = input().split()
my_dict = {}

for i in range(0, len(products), 2):
    my_dict[products[i]] = int(products[i + 1])

print(my_dict)
