#the items in a list can be a variable value.


#index-in a list or an array, it is the integer representatioin of the 
#position of an item in the list or array.

#my_kids = ["Alex", "Sky"]

#print(my_kids[0])

#1.Create a program that has a list of at least 3 of your favorited foods in order
#and assign that list to a variable named "favorite_foods"

favorite_foods = ["chicken", "rice", "apples"]
print(favorite_foods[-1])

#2.Create a program that contains a list of 4 different "things" around you.
#print out each item on a new line with the number of it's index in front of the item.

aroundme = ["0. imac", "1. tv", "2. notepad", "3. desk"]

print(aroundme[0])
print(aroundme[1])
print(aroundme[2])
print(aroundme[3])

#3.Using the code from exercise 2, prompt the user for which item the user thinks is the
#most interesting. Tell the user to use numbers to pick. (IE 0-3)
#When the user has entered the value print out the selection that the user chose with 
#some sort of pithy message associated with the choice.


i = (input("What do you like? 0-3 "))
if i == '0' :
    print(f'You chose a {things[0]}. You must like apple!')
elif i == '1':
    print(f'You chose {things[1]}. You must like tv!')
elif i == '2':
    print