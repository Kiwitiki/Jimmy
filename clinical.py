
########################################### Items ###########################################

class Item():
    def __init__(self, name, description,value):
        self.name = name
        self.description = description
        self.value = {}

    def __str__(self):
        return "{}\n=====\n{}\nValue: {}\n".format(self.name, self.description, self.value)


########################################### Weapons ###########################################
class Weapon(Item):
    def __init__(self, name, description, value, damage):
        self.damage = damage
        super().__init__(name, description, value)

    def __str__(self):
        return "{}\n=====\n{}\nValue: {}\nDamage: {}".format(self.name, self.description, self.value, self.damage)

class Rock(Weapon):
    def __init__(self):
        super().__init__(name = "Rock",
                        description = 'A fist sized Rock, you can throw it on something but still its heavy',
                        value = 1,
                        damage = 5)

class Gummybear(Weapon):
    def __init__(self):
        super().__init__(name = "Gummybear",
                        description = "A fluffy, yummi little thing with a bit dirt on it.",
                        value = 2,
                        damage = 10)

class BareHands(Weapon):
    def __init__(self):
        super().__init__(name = "Bare Hands",
                        description = "Your bare Hands, can easily be hurt.",
                        value = 0,
                        damage = 2)


########################################### Enemys ###########################################

class Enemy():
    def __init__(self, name, hp, damage):
        self.name = name
        self.hp = hp
        self.damage = damage

    def is_alive(self):
        return self.hp > 0

class TinySpider(Enemy):
    def __init__(self):
        super().__init__(name = "Tiny Spider",
                        hp = 8,
                        damage = 2)

class Butterfly(Enemy):
    def __init__(self):
        super().__init__(name = "Butterfly",
                        hp = 4,
                        damage = 1)

class SmokingSquirrl(Enemy):
    def __init__(self):
        super().__init__(name = "Smoking Squirrl",
                        hp = 8,
                        damage = 4)

