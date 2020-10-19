#Madlib
#Prompt the user for the missing words to a Madlib sentence using the input function. 
#You can make up your own Madlib sentence, but here's an example:

print('''
Please fill in the blanks below:
____(name)____'s favorite subject in school is ____(subject)____.
''')

#Any variation of print or multiple prints that gets it on two lines is fine
name = input("What's your name? ")
subject = input("What's the subject? ")
print(f"{name} favorite subject in school is {subject}.")
##interpoloation, concatenation, and print comas is fine