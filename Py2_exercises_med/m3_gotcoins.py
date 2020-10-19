#How many coins? Write a program that will prompt you for how manny coins you want.
#Initially you have no coins. It will ask you if you want a coin? If you type "yes",
#it will give you one coin, and print out the current tally. If you type no, it will
#stop the program.

#coins = 0
#get_coin = "yes "
#while get_coin == "yes ":
#    print("You have %s coins." % coins)
#    get_coin = input("Do you want another coin? ")
#    if get_coin == "yes ":
#        coins += 1
#
#    print("Bye")

coins = 0
print(f"You have {coins} coins.")
more = input("Do you want another? ")

while more == "yes":
    coins += 1
    print(f"You have {coins} coins ")
    more = input("Do you want another? ")
if more == "no":
    coins == coins
    print(f"You have {coins} coins")
    print("See ya later")