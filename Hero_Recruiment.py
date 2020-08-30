command = input()
names = {}

while command != "End":
    token = command.split(" ")
    if token[0] == "Enroll":
        name = token[1]
        if name in names.keys():
            print(f"{name} is already enrolled.")
        else:
            names[name] = []
    elif token[0] == "Learn":
        name = token[1]
        spell = token[2]
        if name not in names:
            print(f"{name} doesn't exist.")
        elif spell in names[name]:
            print(f"{name} has already learnt {spell}.")
        else:
            names[name].append(spell)
    elif token[0] == "Unlearn":
        name = token[1]
        spell = token[2]
        if name not in names:
            print(f"{name} doesn't exist.")
        elif spell not in names[name]:
            print(f"{name} doesn't know {spell}.")
        else:
            names[name].remove(spell)
    command = input()

print(f"Heroes:")
for key, value in sorted(names.items(), key=lambda x: (-len(x[1]), x[0])):
    print(f"== {key}:", end=" ")
    print(f", ".join(value))
