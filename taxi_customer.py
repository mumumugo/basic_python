from random import *

counter = 0

for i in range (1,51): # 1~51의 taxi customer
    time = randrange(5,51) # 5~50 min travel time 
    if 1 <= time <=15:
        print("[승차O]{0}번째 손님 (소요시간: {1})".format(i,time))
        counter+=1
    else:
        print("[승차X]{0}번째 손님 (소요시간: {1})".format(i,time))
print("총 탑승가능 승객: {0}분".format(counter))