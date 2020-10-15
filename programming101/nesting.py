name = input("what is your name?")

length = len(name)
print(length)

if length > 3:
     if length < 10:
        if length == 4:
            print('Perfect Length!')
        else:
            print("It's")

    if len(name) > 15:
        print("That is way too long.")
    else:
        print(f"Welcome {name}")