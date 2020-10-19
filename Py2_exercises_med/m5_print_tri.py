#Print a triangle consisting * characters

#level = 0
#width = 9
#for level in range(0, width, 2):
#    level += 1
#    in_rows = "*" * int(level)
#    print("{:^30}".format(in_rows))

# with String multiplcation
#base = 13
#stars = 1
#while stars <= base:
#    blanks = int((base-stars)/2)
#    print(" "*blanks+"*"*stars+" "*blanks)
#    stars = stars+2

# Not using string multiplcation
base = 11
stars = 1
while stars <= base:
    blanks = int((base-stars)/2)
    b = 0
    blank_out = ""
    while b <=blanks:
        blank_out += " "
        b += 1
    s = 0
    stars_out = ""
    while s < stars:
        stars_out += "*"
        s += 1
    print(blank_out+stars_out+blank_out)
    stars = stars+2