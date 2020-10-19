#Print the first 100 triangle numbers. 
# formula >>> n(n+1)/2

i = 1
while i <= 100:
    print("%i. %i" % (i,int(i*(i+1)/2)))
    i+=1