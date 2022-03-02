#general unit
class Unit:
    def __init__(self, name, hp):
        self.name = name
        self.hp = hp


#attacker
class AttackUnit(Unit):
    def __init__(self, name, hp, damage):
        Unit.__init__(self, name, hp)
        self.damage = damage

    def attack(self, location):
        print("{0} : degree {1}' attacking now. [[[damage {2}]]]"\
            .format(self.name, location, self.damage))
    
    def damaged(self, damage):
        print("{0} : {1} damaged".format(self.name, damage))
        self.hp -= damage
        print("{0} : Now HP is {1}" .format(self.name, self.hp))
        if self.hp <=0:
            print("{0} : Unit is dead.". format(self.name))

#medic : no attack damage

# Attacker: firebat
firebat1 = AttackUnit("firebat", 50,16)
firebat1.attack("5")
#firbat attacked  by two times
firebat1.damaged(25)
firebat1.damaged(25)

