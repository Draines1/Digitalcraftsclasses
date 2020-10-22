from Unit import Unit
from Item import Item
name = input("What do you want the player to be named?")
name = "Clint"
player = Unit(name, [5,5])


enemies = [
    Unit("Orc", [4,4], 10, 2),
    Unit("Goblin", [6,6], 6, 3)
]
menu = ["Move up", "Move Down", "Move Left", "Move Right"]

def show_menu():
    for i in range(len(menu)):
        print(f"{i+1}. {menu[i]}")
    
playing = True

while playing:
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
            print("enemy Attacks!")
            enemy.atttack(player)
    
    
    print(player.health)



# print(player.position)
# player.move("up")
# player.move("up")
# player.move("left")
# player.move("up")
# print(player.position)