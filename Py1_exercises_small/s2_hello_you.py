#HELLO YOU! 
#Same as the first exercise, but this time print the user's name in ALL CAPS, 
#and also tell them the number of letters in their name.  

name = input('What is your name? ').upper()
num = len(name)
print(f"Hello, {name.upper()}!")

print(f"Your name has {num} letters in it! Awesome!")

## Also acceptable if not applying upper to the input
## name = name.upper()


#### Also acceptable

#print("Hello, "+name)
#print(f"Hello, {name}")
#print("Hello, %s" % name)