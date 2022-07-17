inp = input()
d = {}

for char in inp:
    if char != " ":
        d[char] = inp.count(char)

for k, v in d.items():
    print(f"{k} -> {v}")

