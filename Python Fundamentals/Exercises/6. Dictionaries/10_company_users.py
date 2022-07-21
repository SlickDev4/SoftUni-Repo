companies = {}

while True:
    command = input().split(" -> ")
    if command[0] == "End":
        break

    company = command[0]
    employee = command[1]

    if company not in companies.keys():
        companies[company] = [employee]
    else:
        if employee not in companies[company]:
            companies[company].append(employee)

for key, value in companies.items():
    print(key)
    for element in value:
        print(f"-- {element}")


