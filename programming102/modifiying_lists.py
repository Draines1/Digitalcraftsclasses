#method-in python (and other languages) a method is a function that
#a datatype can run from it's own instance.
# my_pets = ["Red", "Bear", "Pluto"]
# my_pets.append("Rainbow")
# print(my_pets)

#you can concatenate your lists
# my_dogs = ["Red", "Bear"]
# my_cat = ["Pluto"]

# my_pets = my_dogs + my_cat
# print(my_pets)

# new_set_of_pets = []
#extend-another method that modifies the list
# new_set_of_pets.extend(my_dogs)
# print(new_set_of_pets)
# new_set_of_pets.extend(my_cat)


# print(new_set_of_pets)

#1.Write a program that has a list of names.
# Add two new names to that list.
# Print the results.
names = ["Bob", "Sam", "Mike"] 

newnames = ["Liz", "Ben"] + ["Bob", "Sam", "Mike"]
print(names, newnames)


#2.Write a program that has 5 names in a list.
# Replace the items at index 2 and 4 with "Foo" and "Bar" respectively.
stars = ["John", "Ralph", "Gucci", "Bolt", "Jess"]
stars[2] = "foo"
stars[4] = "bar"
print(stars)


#3.Write a program that has a list of 5 names.
# Loop through the array printing the item at index 0 
# and then removing that item from the array until there are no items in the array.
# (hint) This will use a while loop.
names_air = ["John", "Ralph", "Gucci", "Bolt", "Jess"]

while len(names_air):
    print(names_air[0])
    del(names_air[0])
