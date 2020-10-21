#scope - the place in a program where a declared variable can be accessed


#global scope...
 x = 10  
  # x not declared inside a function. It's a globally scoped variable.
  def add_to_x(a):
      # can access x because it is a global variable 
      return x + a

  print(add_to_x(2)) #12

  #local scope...
    def add_two_numbers(a,b):
      c = a+b
      print(c)
      return c
  
  result = add_two_numbers(2,4)
  print(result)

  print(c) # Error c is not in global scope!
  def add_two_numbers(a,b):
      c = a+b
      print(c)
      return c

  def add_to_c(d):
      e = c+d
      print(e)
      return e 
  
  add_two_numbers(1,2) #c is in the function, but its local
  add_to_c(12) # errors .. c is not in scope


#1. Create a program that has a global varaible 'name' that is assigned a string value.
#>>define a function that has an parameter called 'message' and will print out the name coma and then the message supplied in the argument when the function is called.
#>>call that function 3 times with 3 different messages.
    #sample output
    #Clint, You are awesome and really tall.

#2. Create a program that has a global variable 'name' like the exercise above.
#>>have a function that can modify the name variable with a supplied argument.
#>>call that function changing the name 3 times.