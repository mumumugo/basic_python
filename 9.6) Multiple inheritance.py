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
        print("{0} : {1} attacking now. [[[damage {2}]]]"\
            .format(self.name, location, self.damage))
    
    def damaged(self, damage):
        print("{0} : {1} damaged".format(self.name, damage))
        self.hp -= damage
        print("{0} : Now HP is {1}" .format(self.name, self.hp))
        if self.hp <=0:
            print("{0} : Unit is dead.". format(self.name))

#dropship: transportation. no attack damage.
class Flyable:
    def __init__(self, flying_speed):
        self.flying_speed = flying_speed

    def fly(self, name, location):
        print("{0} : Heading to <{1}> now. [speed {2}]"\
            .format(name, location, self.flying_speed))

# flyable attacker
class FlyableAttackUnit (AttackUnit, Flyable):
    def __init__(self, name, hp, damage, flying_speed):
        AttackUnit.__init__(self, name, hp, damage)
        Flyable.__init__(self, flying_speed)
            
#valkyrie: flyable attacker, 14 shot per attack.
valkyrie = FlyableAttackUnit("valkyrie", 200, 6, 5)
valkyrie.fly(valkyrie.name, "East")

