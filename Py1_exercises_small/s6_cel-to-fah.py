#Celsius to Fahrenheit
#Prompt the user for a number in degrees Celisus, and convert
#the value to degrees in Fahrenheit and display it to the user. 
#Use the following formula: F = (C * 9/5) + 32

# The key is to make sure that c is wrapped in an int
c = input("Temperature in C?\n")
f = (int(c) * 9/5) + 32
print(f,'F')