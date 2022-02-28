class Unit:
    def __init__(self,name,hp,damage):
        self.name = name
        self.hp = hp
        self.damage = damage
        print ("{0} Unit has created.".format(self.name))
        print("HP: {0}, AP: {1}".format(self.hp, self.damage))

#attacker
class AttackUnit:
    def __init__(self,name,hp,damage):
        self.name = name
        self.hp = hp
        self.damage = damage

    def attack(self, location):
        print("{0} : {1} attacking now. [[[damage {2}]]]"\
            .format(self.name, location, self.damage))
    
    def damaged(self, damage):
        print("{0} : {1} damaged".format(self.name, damage))
        self.hp -= damage
        print("{0} : Now HP is {1}" .format(self.name, self.hp))
        if self.hp <=0:
            print("{0} : Unit is dead.". format(self.name))

# Attacker: firebat
firebat1 = AttackUnit("firebat", 50,16)
firebat1.attack("5")

firebat1.damaged(25)
firebat1.damaged(25)

