adventure_days = int(input())
number_of_players = int(input())
group_energy = float(input())
water_per_day = float(input())
food_per_day = float(input())

total_water = adventure_days * number_of_players * water_per_day
total_food = adventure_days * number_of_players * food_per_day

current_energy = group_energy
current_water = total_water
current_food = total_food

for i in range(1, adventure_days + 1):
    lost_energy = float(input())

    current_energy -= lost_energy

    if current_energy <= 0:
        break

    if i % 2 == 0:
        current_energy += 5 / 100 * current_energy
        current_water -= 30 / 100 * current_water

    if i % 3 == 0:
        current_food -= current_food / number_of_players
        current_energy += 10 / 100 * current_energy

if current_energy > 0:
    print(f"You are ready for the quest. You will be left with - {current_energy:.2f} energy!")
else:
    print(f"You will run out of energy. You will be left with {current_food:.2f} food and {current_water:.2f} water.")
