#return- in programming terms, returning is the value that a function sends out of the result of calling the function.

# def add_numbers(a,b):
#     result = a+b
#     return result #anything after the return statement will not print

# num_length = len([2,3,5])

# final = add_numbers(1,3) / add_numbers(4,6)
# print(final)

#implicit retun-

#1. Write a program that has a function with two parameters.
#>>return the concatinated value of the two parameters.
#>>print the results.

def slamdunk(a,b):
    result = (a+b)
    return result

print(slamdunk("a","b"))
print("a" + "b")



#2. Write a program that has a function named total_count that expects a list of strings as it argument when the function is called.
#>>have the returned value be a dictionary with the keys 'list_length' and 'total_chars'.
#>>the list_length value needs to be the length of the list and the total_chars needs to be the total count of characters of all of the items in the array.
#>>call the function 3 times with 3 different lists.
#>>(hint) len is usable on lists and strings.

def total_count