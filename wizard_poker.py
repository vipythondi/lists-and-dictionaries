cards=input().split(":")
command=input()
deck=[]
while command!="Ready":
    token=command.split(" ")
    if token[0] == "Add":
        name=token[1]
        if name in cards:
            deck.append(name)
        else:
            print("Card not found.")
    elif token[0] == "Insert":
        name=token[1]
        index=int(token[2])
        if name in cards:
            deck.insert(index, name)
        else:
            print("Error!")
    elif token[0] == "Remove":
        name=token[1]
        if name in deck:
            deck.remove(name)
        else:
            print("Card not found.")
    elif token[0] == "Swap":
        card1=token[1]
        card2=token[2]
        c1=deck.index(card1)
        c2=deck.index(card2)
        deck[c1], deck[c2] = deck[c2], deck[c1]
    elif token[0] == "Shuffle":
        deck=reversed(deck)

    command=input()

print(" ".join(deck))