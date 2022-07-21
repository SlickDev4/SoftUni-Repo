legendary = {"shards": 0, "fragments": 0, "motes": 0}
junk = {}
obtained = False
command = input().split()

while True:
    for index in range(0, len(command), 2):
        value = int(command[index])
        key = command[index + 1].lower()
        if key in legendary.keys():
            legendary[key] += value
        else:
            if key not in junk.keys():
                junk[key] = 0
            junk[key] += value
        if legendary["shards"] >= 250:
            print("Shadowmourne obtained!")
            legendary["shards"] -= 250
            obtained = True
        elif legendary["fragments"] >= 250:
            print("Valanyr obtained!")
            legendary["fragments"] -= 250
            obtained = True
        elif legendary["motes"] >= 250:
            print("Dragonwrath obtained!")
            legendary["motes"] -= 250
            obtained = True
        if obtained:
            break
    if obtained:
        break
    command = input().split()

for key, value in legendary.items():
    print(f"{key}: {value}")

for key, value in junk.items():
    print(f"{key}: {value}")



