#Work or sleep in?
#Prompt the user for a day of the week just like the previous problem. 
#But this time, print "Go to work" if it's a 
#a work day and "Sleep in" if it's a weekend day. 

day = int(input('Day (0-6)? '))
if day == 0 or day == 6:
    print("Sleep in!")
else:
    print("Go to work!")