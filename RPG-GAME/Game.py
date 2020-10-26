from Unit import Unit
from Item import Item
name = input("What do you want the player to be named?\n")
name = "Darren"
player = Unit(name, [5,5])


enemies = [
    Unit("Orc", [4,4], 10, 2),
    Unit("Goblin", [6,6], 6, 3)
]

items = [
    Item("Treasure", [2,3]),
    Potion("Health Potion", [3,3])
]


menu = ["Move up", "Move Down", "Move Left", "Move Right"]

def show_menu():
    for i in range(len(menu)):
        print(f"{i+1}. {menu[i]}")
    i += 2
    for item in player.inventory:
        print(f"{i}. Use {item.name}")
        i += 1
    
playing = True

while playing:
    print(player)
    show_menu()
    try:
        action = int(input("What is your choice?\n"))
    except ValueError:
        print("You must enter a valid entry.")
        action = None

    if action:
        if action == 1:
            player.move("up")
        elif action == 2:
            player.move("down")
        elif action == 3:
            player.move("left")
        elif action == 4:
            player.move("right")

    for enemy in enemies:
        if enemy.position == player.position:
            print(f"You ran into {enemy.name}")
            print("You attack!")
            player.atttack(enemy)
            print("enemy attacks!")
            enemy.atttack(player)
    
    for item in items:
        if item.positon == player.position:
            if item.name == "Treasure":
                playing = False
                print("You find the Treasure. You won the game")
            else:
                print(f"You have come across {item.name}")
                player.pickup_item(item)




# print(player.position)
# player.move("up")
# player.move("up")
# player.move("left")
# player.move("up")
# print(player.position)