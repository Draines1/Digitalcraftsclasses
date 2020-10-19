#class Solution:
    #def fizzBuzz(self, n: int) -> List[str]:


    

#1.Fizz Buzz
# Write a program that prints the numbers from 1 to 100. 
# But for multiples of three print "Fizz" instead 
# of the number and for the multiples of five print "Buzz". 
# For numbers which are multiples of both three and five print "FizzBuzz".

#let fizzBuzz = function(n) {
  #let result = [];

for fizzbuzz in range(100):
    if fizzbuzz % 3 == 0 and fizzbuzz % 5 == 0:
        print("fizzbuzz")
        continue
    elif fizzbuzz % 3 == 0:
        print("fizz")
    elif 