class Unit:
    def __init__(self, name, position, health = 10, attack_power = 2):
        self.name = name
        self.health = health
        self.attack_power = attack_power
        self.position = position #[1,1]

    def get_hit(self, power):
        self.health = self.health - power
        

    def attack(self, enemy):
        enemy.get_hit(self.attack_power)

    def move(self, dir):
        if dir == "up":
            self.position = [self.position[0], self.position[1]-1]
        elif dir == "down":
            self.position = [self.position]
        elif dir == "left"
        elif dir == "right"
