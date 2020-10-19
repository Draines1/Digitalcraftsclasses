#Print a square 2 #Print a NxN square of * characters. 
#Prompt the user for N.

#total = int(input("How big is the square?\n"))
#r = 0
#while r < total:
#    c = 0
#    out = ""
#    while c < total:
#       out += "*"
#       c += 1
#    print(out)
#    r += 1

# If they looked things up they may come up with this
total = int(input("How big is the square?\n"))
r = 0
while r < total:
    print("*"*total)         
    r += 1