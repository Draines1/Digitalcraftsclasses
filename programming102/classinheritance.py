class Mob:
    def __init__(self, name, health = 10, power = 2):
        self.name = name
        self.health = health
        self.attack_power = attack_power
      

    def get_hit(self, power):
        self.health = self.health - power
        

    def attack(self, enemy):
        enemy.get_hit(self.attack_power)

class Hero(Mob):

    def __init__(self):
        self.name = "Sir Barksalot"
        self.health = 22
        self.attack_power = 5
        self.defense = 1

    def get_hit(self, power):
        print('Hey yall I am getting hit and it hurts. ')
        super().get_hit(power-self.defense)

    def yell(self):
        print("I %s, say to thou villian. Preapare to die!" % self.name)


#hero = Hero()
bad_guy = Mob("Baddy")
hero.yell()
hero.attack(bad_guy)
print(bad_guy.health)

bad_guy.attack(hero)
#print(hero.attack power)