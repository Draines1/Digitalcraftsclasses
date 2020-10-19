#Your task is to write a program that calculates 
#how much of a tip to leave at a restaurant.
#Prompt the user for two things: The total bill amount,
#The level of service, which can be one of the following: good, fair, or bad
#Calculate the tip amount and the total amount (bill amount + tip amount).
#The tip percentage based on the level of service is based on:

#good -> 20%
#fair -> 15%
#bad -> 10%

total = int(input("Total Bill Amount? "))
service_level = input("Level of Service? ")

if service_level == "good":
    tip = total*0.20
elif service_level == "fair":
    tip = total*0.15
elif service_level == "bad":
    tip = total * 0.10
else:
    tip = 10000 #jk

print("Tip Amount: %s" % tip)
final = total+tip
print("Total amount : %s" % final)