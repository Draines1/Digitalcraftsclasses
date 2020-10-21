#Dicitonary- In python a dictionary is a data type that is a grouping of data that uses
#keys to print to a value. Some languages have data types that are similar called things
#like maps, structs, or objects.
#Key- in programming, a key is a string, integer, or one of a varity of data types
#that will allow the developer to access a value.



#1.Create a program that starts with an empty dictionary.
#Add 3 different key value pairs to the empty dictionary.

movie = {
    "name": "Star Wars",
    "epsiode":4, #example..."epsiode" is a key, "4" is the value.
    "year":"1977"
}
print(movie)

# for key in movie: #this will only print the keys name, epsiode, and year.
#     print(key)

for key in movie:
    print(key, movie[key]) #this will print both the keys and values.

#2. Create a program with a dictionary called person.
#>>the person dictionary needs to have the keys, first_name, last_name, age, hair_color.
#>>print each one of these key/values pairs without directly using the key's name as a string by using a loop.
#>>after each key value pair, print out a sentence using each one of the keys
person =


#3. Create a program that has a list of dicitonaries of people, with each dictionary including name, phone, email.
#>>for each dictionary print the items in the dictionary. 