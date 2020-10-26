#Virtual Pet without object-oriented Programming #lists, dictionaries, loops, and functions

# puppy = {              # lines 3-7 are what's called a dictionary. A dictionary is a set of keys and 
#     "name": "Cujo",    # values inside of curly braces, which are separted by a colon. The left side
#     "fullness": 50,    # of the colon is the key, and the right side is the value. Dictionaries allow
#     "happiness": 20,   # you to group information together, and call upon it at a later time.
# }                      #

# def feed_pet(pet):                # lines 9-17 are examples of functions. A function allows you to 
#     pet["fullness"] += 10         # reduce coding redundancy. 
                                  
# def play_with_pet(pet):           # += is the increment operator which assign values to variables.
#     pet["happiness"] += 10

# def get_hungry_and_mopey(pet):
#     pet["fullness"] -= 5
#     pet["happiness"] -= 5

# while True:

#     print("""
# %s's stats:
# Fullness %d
# Happiness: %d
# """ % (puppy["name"], puppy["fullness"], puppy["happiness"]))

#     choice = int(input("""
# 1. Feed puppy
# 2. Play with puppy
# 3. Do nothing
# """))
#     if choice == 1:
#         feed_pet(puppy)
#     elif choice == 2:
#         play_with_pet(puppy)
#     else: 
#         pass

#Virtual Pet with object-oriented Programming
#attributes-
#methods-

class Pet:
    def __init__(self, name, fullness=50, happiness=50, hunger=5, mopiness=5):
        self.name = name
        self.fullness = fullness
        self.happiness = happiness
        self.hunger = hunger
        self.mopiness = mopiness
        self.toys = []

    def eat_food(self):
        self.fullness += 30

    def get_love(self):
        self.happiness += 30

    def be_alve(self):
        self.fullness -= self.hunger
        self.happiness -= self.mopiness
        for toy in self.toys:
            self.happiness += toy.use()

    def __str__(self):
        return """
        %s:
        Fullness: %d
        Happiness:
        """ % (self.name, self.fullness, self.happiness)

class CuddlyPet(Pet): #cuddlypet is a subclass of pet. Putting pet in () signiies that.
    def __init__(self, name, fullness=50, hunger=5, cuddle_level=1):
        super().__init__(name, fullness, 100, hunger, 1)
        self.cuddle_level = cuddle_level

    def be_alve(self):
        self.fullness -= self.hunger
        self.happiness -= self.mopiness/2
             for toy in self.toys:
            self.happiness += toy.use()
    
    def cuddle(self, other_pet):
        for i in range(self.cuddle_level):
            other_pet.get_love()

benji = CuddlyPet("Benji", 50, 20, 20, 1)
print(benji.fullness, benji.fullness)
# this will print from the parent class Pet 50 20

benji.be_alve()
print(benji.fullness, benji.happiness)
# this will print from the parent class Pet 30 19



# cujo = pet("Cujo", 50, 20)


# benji = pet("Benji", 50 100)