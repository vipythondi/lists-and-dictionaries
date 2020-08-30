tanks = input().split(", ")
commands = int(input())

for c in range(1, commands + 1):
    command = input().split(", ")
    if command[0] == "Add":
        name = command[1]
        if name not in tanks:
            tanks.append(name)
            print("Tank successfully bought")
        else:
            print(f"Tank is already bought")
    elif command[0] == "Remove":
        name = command[1]
        if name in tanks:
            print(f"Tank successfully sold")
            tanks.remove(name)
        else:
            print("Tank not found")
    elif command[0] == "Remove At":
        index = int(command[1])
        if 0 <= index < (len(tanks)):
            print("Tank successfully sold")
            tanks.remove(tanks[index])
        else:
            print("Index out of range")
    elif command[0] == "Insert":
        index = int(command[1])
        name = command[2]
        if 0 <= index < (len(tanks)) and name in tanks:
            print("Tank is already bought")
        elif 0 <= index < (len(tanks)) and name not in tanks:
            print("Tank successfully bought")
            tanks.insert(index, name)
        else:
            print("Index out of range")

print(", ".join(tanks))