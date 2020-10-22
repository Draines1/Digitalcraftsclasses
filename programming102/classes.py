#instantiation - in programming terms this is creating an self contained 'instance' of a class that can be used in the program.
#attributes - are values in class that can be accessed using the attribute name. Much like key in a dictionary. 


# class Person:
#     def __init__(self,name,age):#two underscores on each side. # "self" is conisdered the standard for a class. It's not an argument.
#         print(self)
#         print("You created a new instance of person.")
#         self.name = name
#         self.age = age


# clint = Person("Clint", 38)
# anna = Person("Anna",37)

# print(clint.age)
# print(anna.name)

#1. Create a program that has a class named Vehicle.
#>>Make the Vehicle have a 'category' which can be anything like, sport, truck, motorcycle, minivan.
#>>Make the Vehicle class have 'wheels' as an attribute.
#>>Make the Vehicle class have 4 as the default value for the class.
#>>Create 5 different instances of the class with at least one being a motorcycle.

# class Vehicle:
#     def __init__(self, category, wheels = 4):
#         self.category = category
#         self.wheels

# suv = Vehicle("suv")
# print(suv.category)

# motorcycle = Vehicle("motorcycle", 2)
# print(motorcycle.wheels)

# truck = Vehicle("truck")
# print(truck.category)

# sedan = Vehicle("car")
# print(sedan.category)



class Vehicle:
    def __init__(self, make, model, category, color, wheels=4):
        print("You created a new vehicle")
        self.make = make
        self.model = model
        self.category = category
        self.wheels = wheels
        self.color = color
truck = Vehicle("Ford", "F-150", "Truck", "black", 4)
truck2 = Vehicle("Ford", "F-250", "Truck", "black", 4)
truck3 = Vehicle("Ford", "F-350", "Truck", "black", 4)
truck4 = Vehicle("Ford", "F-450", "Truck", "black", 4)
motorcycle = Vehicle("Ducati", "Scrambler", "Motorcycle", "black", 2)
print(f"{motorcycle.wheels}")