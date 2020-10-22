
  input_string = input("Give me a number please!\n")
  # inputs are a string so we need to convert it
  try:
      number_value = int(input_string)
      print("Our number is %s" % number_value)
  except ValueError: 
      print('You did not give a number')