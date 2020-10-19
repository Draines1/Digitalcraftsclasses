#Print a box. Given a height and width, input by the user,
#print a box consisting of * characters as it's border.

width,height = int(input("Width? ")), int(input("Height? "))

on_row = 0
while on_row <= height:
    if on_row == 0 or on_row == height:
        print("*"*width)
    else:
        stars = "*" + " "*(width-2) + "*"
        print(stars)
    on_row += 1