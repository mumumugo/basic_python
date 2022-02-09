gun=10 

def checkpoint(soldiers):
    global gun 
    gun = gun- soldiers
    print("함수 내 남은 총: {0}".format(gun))

print("전체 총:{0}".format(gun))
checkpoint(2)
print("남은총:{0}".format(gun))

#-----------------------------------
def checkpoint_ret(gun,soldiers):
    gun = gun- soldiers
    print("ret함수 내 남은 총: {0}".format(gun))

print("ret전체 총:{0}".format(gun))
checkpoint_ret(gun,2)
print("ret남은총:{0}".format(gun))