items = input().split("|")
budget = float(input())

initial_budget = budget

value_of_items = [i.split('->', 1)[-1] for i in items]
type_of_items = [i.split('->', 1)[0] for i in items]

value_of_items = [float(i) for i in value_of_items]
value_of_items = [("{:.2f}".format(i)) for i in value_of_items]

bought_items = []
profit = 0
temp_profit = 0

for index, item in enumerate(type_of_items):
    if item == "Clothes":
        if not float(value_of_items[index]) > 50.00:
            if not budget - float(value_of_items[index]) < 0:
                budget -= float(value_of_items[index])
                bought_items.append(float(value_of_items[index]) + (40 / 100 * float(value_of_items[index])))

    if item == "Shoes":
        if not float(value_of_items[index]) > 35.00:
            if not budget - float(value_of_items[index]) < 0:
                budget -= float(value_of_items[index])
                bought_items.append(float(value_of_items[index]) + (40 / 100 * float(value_of_items[index])))

    if item == "Accessories":
        if not float(value_of_items[index]) > 20.50:
            if not budget - float(value_of_items[index]) < 0:
                budget -= float(value_of_items[index])
                bought_items.append(float(value_of_items[index]) + (40 / 100 * float(value_of_items[index])))

bought_items = [("{:.2f}".format(i)) for i in bought_items]

for i in bought_items:
    temp_profit += float(i)

new_budget = temp_profit + budget
profit = new_budget - initial_budget

print(*bought_items, sep=" ")
print(f"Profit: {profit:.2f}")

if new_budget > 150:
    print("Hello, France!")
else:
    print("Not enough money.")
    