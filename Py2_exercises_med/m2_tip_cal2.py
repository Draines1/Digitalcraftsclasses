#Tip calculator 2
#Allow the ability to divide the check into a equal parts amount a number of people. 
#The user will enter the number of people to be divided amongst. 

#while tip == 0:
 #   bill = float(input("Total bill amount?: "))
  #  split = float(input("Split how many ways?: "))
   # serv = input("Level of service? Enter good, fair, or bad: ")

#    if serv == "good":
 #       tip = float(bill * .2)
#
 #   elif serv == "fair":
  #      tip = float(bill * .15)

#    elif serv == "bad":
 #       tip = float(bill * .10)
    
  #  else:
   #     print("Please enter good, fair, or bad only.")

#total = bill + tip 
#formatted_tip = "${:,.2f}".format(tip)
#formatted_total = "${:,.2f}".format(total)
#split_amt = total/split
#formatted_split = "${:,.2f}".format(split_amt)

#print("Tip amount: %.2f" % tip)
#print("Total amount: %.2f" % total)
#print("Amount per person: %.2f" % split_amt)



total = int(input("Total Bill Amount? "))
service_level = input("Level of Service? ")

if service_level == "good":
    tip = total*0.20
elif service_level == "fair":
    tip = total*0.15
elif service_level == "bad":
    tip = total * 0.10

split = int(input("Split how many ways?\n"))

print("Tip Amount: %s" % tip)
final = total+tip
print("Total amount: %s" % final)
final_split = final/split
print("Total Each: %s" % final_split)