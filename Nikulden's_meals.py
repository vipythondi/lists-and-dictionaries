command = input()
names = {}
unlike = 0
while command != "Stop":
    token = command.split("-")
    if token[0] == "Like":
        name = token[1]
        meal = token[2]
        if name not in names:
            names[name] = []
        if meal in names[name]:
            command = input()
            continue
        names[name].append(meal)
    elif token[0] == "Unlike":
        name = token[1]
        meal = token[2]
        if name not in names:
            print(f"{name} is not at the party.")
        elif name in names:
            if meal in names[name]:
                print(f"{name} doesn't like the {meal}.")
                names[name].remove(meal)
                unlike += 1
            elif meal not in names[name]:
                print(f"{name} doesn't have the {meal} in his/her collection.")
    command = input()

names = dict(sorted(names.items(), key=lambda g: (-len(g[1]), g[0])))

for key, value in names.items():
    print(f"{key}: {', '.join(value)}")

print(f"Unliked meals: {unlike}")
