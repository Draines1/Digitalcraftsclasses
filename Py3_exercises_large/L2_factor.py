#Factor a number. Given a number, print its factors.

while True:
    try:
        user_number = int(input("What number would you like to find the factors of? "))
        break
    except ValueError:
        print("Please use a number.")

max_number = user_number + 1
print("Here are your factors:")
for n in range(1, max_number):
    factor = (user_number / n)
    if factor.is_integer():
        print(int(factor))
    n += 1    