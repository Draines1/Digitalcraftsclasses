#in game terms mob stands for mobile. It can be anything that moves including enemies, npc, and the player's characters.
# class Mob:
#     def __init__(self, name, health = 10, power = 2):
#         self.name = name
#         self.health = health
#         self.power = power
      
# # The first argument of every method is self.
#     def get_hit(self, power):
#         self.health = self.health - power
#         print(f'I, %s, have been hit for %s!' % (self.name, power))
# ###you can modify an attribute inside of a method.
#     def attack(self, enemy):
#         enemy.get_hit(self.power)

# bad_guy = Mob("Evil")
# hero = Mob("Sir Barksalot", 30,10)
# #self is not placed here. The class handles that itself. Never call self in an argument
# hero.get_hit(2)

# bad_guy.attack(hero)
# bad_guy.attack(hero)
# bad_guy.attack(hero)

# print(bad_guy.health)


#1. Using our vehicle class from the previous lesson, add a speed, top_speed, position, and acceleration attribute.
#>>speed and position should start at 0, top_speed and acceleration are numbers.
#>>add a class method called move. When the move method is called have the position increase by the speed of the car.
#>>add a class method called accelerate and using the very simplified equation to have the vehicle accelerate when the accelerate method is called on that instance:
#  speed = speed + acceleration
#>>in the accelerate method, do not allow the vehicle to pass the top speed.
#>>modify the instances of the vehicles to include acceleration and top speed when you instance the vehicles.
#>>using a while loop and assuming each iteration of the loop is a 'second' have the vehicles 'race' by accelerating as much as possible on a drag strip for 20, 40, and 60 seconds to see who wins.
#>>(challange) instead of racing for a timeframe, make the race different distances. Position can be considered in meters.


class Vehicle:
    def __init__(self, category, wheels=4):
        self.category = category
        self.wheels = wheels

suv = Vehicle("suv")
print(suv.category)

motorcycle = Vehicle("motorcycle",2)
print(motorcycle.wheels)

truck = Vehicle("truck")
print(truck.category)

sedan = Vehicle("car")
print(sedan.category)