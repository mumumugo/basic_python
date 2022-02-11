class Unit:
    def __init__(self,name,hp,damage):
        self.name = name
        self.hp = hp
        self.damage = damage
        print ("{0} Unit has created.".format(self.name))
        print("HP: {0}, AP: {1}".format(self.hp, self.damage))
#character1 = Unit("marine",1500, 120)

wraith1 =  Unit("captine", 2500, 300)
print("unit name : {0}, AP: {1}".format(wraith1.name, wraith1.damage))

wraith2 =  Unit("taken_captine", 2500, 300)
wraith2.clocking = False
if wraith2.clocking == True:
    print("{0} is clocking statues".format(wraith2.name))
