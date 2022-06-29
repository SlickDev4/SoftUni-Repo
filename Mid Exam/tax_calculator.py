vehicles = input().split(">>")
valid_vehicles = ["family", "heavyDuty", "sports"]
vehicle_type = []
paying_years = []
traveled_distance = []

tax = 0
total_tax = 0

for element in vehicles:
    split_data = element.split(" ")
    vehicle_type.append(split_data[0])
    paying_years.append(int(split_data[1]))
    traveled_distance.append(int(split_data[2]))

for i in range(len(vehicles)):
    if vehicle_type[i] not in valid_vehicles:
        print("Invalid car type.")
        continue

    if vehicle_type[i] == "family":
        tax += int(traveled_distance[i] / 3000) * 12 + (50 - (paying_years[i] * 5))
        print(f"A {vehicle_type[i]} car will pay {tax:.2f} euros in taxes.")
        total_tax += tax
        tax = 0

    elif vehicle_type[i] == "heavyDuty":
        tax += int(traveled_distance[i] / 9000) * 14 + (80 - (paying_years[i] * 8))
        print(f"A {vehicle_type[i]} car will pay {tax:.2f} euros in taxes.")
        total_tax += tax
        tax = 0

    elif vehicle_type[i] == "sports":
        tax += int(traveled_distance[i] / 2000) * 18 + (100 - (paying_years[i] * 9))
        print(f"A {vehicle_type[i]} car will pay {tax:.2f} euros in taxes.")
        total_tax += tax
        tax = 0

print(f"The National Revenue Agency will collect {total_tax:.2f} euros in taxes.")
