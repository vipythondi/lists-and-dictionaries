command = input()
names = {}
while command != "Statistics":
    token = command.split("->")
    if token[0] == "Add":
        name = token[1]
        if name not in names:
            names[name] = []
        else:
            print(f"{name} is already registered")
    elif token[0] == "Send":
        name = token[1]
        email = token[2]
        names[name].append(email)
    elif token[0] == "Delete":
        name = token[1]
        if name in names:
            del names[name]
        else:
            print(f"{name} not found!")
    command = input()

print(f"Users count: {len(names)}")
names = dict(sorted(names.items(), key=lambda x: (-len(x[1]), x[0])))
for key, value in names.items():
    print(key)
    for v in value:
        print(f"- {v}")