# print("This is the argument") #the argument are the items that's in between the () when you call the function.
# len(1,4,5)

# def add_two_numbers(a,b): # the parameters (a&b) that are being treated as variables within the function.
#     print(a+b) 
# #parameters can be anything you want them to be
# add_two_numbers(1,3)
# add_two_numbers(3,4)

# def me_print(any):
#     print(any)

# me_print(1)
# me_print(True)
# me_print([3, 4, 5,])
# me_print({"eky": "Huh"})

#1. Create a program that has a function that will multipy two numbers together and print out the results.
#>>make the program properly handle an exception if something besides a number is passed as an argument.
#>>have it print out 3 different sets of numbers.


#   input_string = input("Give me a number please!\n")
#   # inputs are a string so we need to convert it
#   try:
#       number_value = int(input_string)
#       print("Our number is %s" % number_value)
#   except ValueError: 
#       print('You did not give a number')



# def multiply(a,b):
#     try:
#         print(int(a*b))
#     except ValueError: 
#         print('You did not give a number')

# multiply(4,5)
# multiply(6,7)
# multiply(5,"a")


#2. Create a program that has a function that will acccepts 3 arguments as title, genre
#>>>year and then print out the values in list format.
#ex...
#1. Title : Star Wars - A new Hope
#2. Genre : Sci-fi
#3. Year : 1977

# def movie(title, genre, year):
#     print(f"1. Title : {title}")
#     print(f"2. Genre : {genre}")
#     print(f"3. Year : {year}")

# mvoie("Clint", "Yup", 1983)


#3. Create a program that does the same thing as above, but the function only accepst a single argument to get the same results.
#>>(hint) you will need to use a datatype other than a string in the argument. 

# solution 1...
# def movie(movie_item):
#     title = movie_item[0]
#     genre = movie_item[1]
#     year = movie_item[2]

    
#     print(f"1. Title : {title}")
#     print(f"2. Genre : {genre}")
#     print(f"3. Year : {year}")

# movie(["Clint", "Yup", 1983])

#solution 2...
def movie(movie_item):
    idx = 1
    for item in movie_item:
        print(f"{idx}. {item} : {movie_item[item]}")
        idx += 1

movie({"Genre":"Horror", "Title":"Clint at the Beach", "year":2020})

movie({"Nothing":"No Movies"})

