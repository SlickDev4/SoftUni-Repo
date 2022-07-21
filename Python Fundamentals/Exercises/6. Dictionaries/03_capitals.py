# with zip

countries = input().split(", ")
capitals = input().split(", ")
the_dict = {}

for country, capital in zip(countries, capitals):
    if country not in the_dict.keys():
        the_dict[country] = capital

for k, v in the_dict.items():
    print(f"{k} -> {v}")

# with comprehension

countries = input().split(", ")
capitals = input().split(", ")

the_dict = {countries[index]: capitals[index] for index in range(len(countries))}

for k, v in the_dict.items():
    print(f"{k} -> {v}")
