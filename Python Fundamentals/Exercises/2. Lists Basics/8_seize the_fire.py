type_of_fire = input().split("#")
amount_of_water = int(input())

total_effort = 0
total_fire = 0

value_of_fire = [i.split('= ', 1)[-1] for i in type_of_fire]
value_of_fire = [int(i) for i in value_of_fire]
type_of_fire = [i.split(' =', 1)[0] for i in type_of_fire]

for index, fire in enumerate(type_of_fire):
    if fire == 'High':
        if 81 <= value_of_fire[index] <= 125:
            if not amount_of_water - value_of_fire[index] < 0:
                amount_of_water -= value_of_fire[index]
                total_fire += value_of_fire[index]
                total_effort += (25 / 100) * value_of_fire[index]
            else:
                value_of_fire[index] = 0
        else:
            value_of_fire[index] = 0

    if fire == 'Medium':
        if 51 <= value_of_fire[index] <= 80:
            if not amount_of_water - value_of_fire[index] < 0:
                amount_of_water -= value_of_fire[index]
                total_fire += value_of_fire[index]
                total_effort += (25 / 100) * value_of_fire[index]
            else:
                value_of_fire[index] = 0
        else:
            value_of_fire[index] = 0

    if fire == 'Low':
        if 1 <= value_of_fire[index] <= 50:
            if not amount_of_water - value_of_fire[index] < 0:
                amount_of_water -= value_of_fire[index]
                total_fire += value_of_fire[index]
                total_effort += (25 / 100) * value_of_fire[index]
            else:
                value_of_fire[index] = 0
        else:
            value_of_fire[index] = 0

print("Cells:")
for i in range(len(value_of_fire)):
    if not value_of_fire[i] == 0:
        print(f" - {value_of_fire[i]}")

print(f"Effort: {total_effort:.2f}")
print(f"Total Fire: {total_fire}")
