#Print the multiplication table for numbers from 1 up to 10.

f=1
while f <= 10:
    s = 1
    while s <= 10:
        v = f*s
        print(f"{f}x{s} = {v}")
        s += 1
    f += 1

# Alternative dirty recursive with no loops
def multi(m,a,b):
    if a == 10 and b == 10:
        return
    print(f"{a} x {b} = {a*b}")
    if m == "a":
        a += 1
        if a == 10:
            m = "b"
    else:
        b += 1
        a = 1
        m = 'a'
    multi(m,a,b)

multi("a",1,1)  