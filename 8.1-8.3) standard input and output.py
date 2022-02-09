print("python", "java", "c++", sep=" vs ")
print("python", "java", "c++", sep=" vs ", end="?")

print(" ")
print("------------------------------------------------")

import sys
print ("python","java", file=sys.stdout)  #표준 출력
print ("python","java", file=sys.stderr) #따로 에러 처리

print("------------------------------------------------")

scores = {"math":0,"English":50, "Coding":  100}
for subject, score in scores.items():
    print(subject, score)
    #print(subject.ljust(8), str(score).rjust(4), sep=":")

print("------------------------------------------------")

#wait line number
for num in range(1,6):
    print("Waiting List: "  + str(num).zfill(3)) #fill out number like 001,002,003...

print("------------------------------------------------")

#get answer from user
# answer = input("enter any input: ")
# print ("user's input: " + answer + ".") #all ways string when user is input

print("------------------------------------------------")

#빈 자리는 빈공간으로 두고, 오른쪽 정렬을 하되, 총 10자리 공간을 확보
print("{0: >10}".format(500))
#show "+" when it is positive, show "-" when negative
print("{0: >+10}".format(500))
print("{0: >+10}".format(-500)) 
# 왼쪽으로 정렬하고, 빈칸을 _로 채움
print("{0:_>10}".format(500)) 
print("{0:_<10}".format(500))  #carefull! no spaces are allows between 0:_<10
# "," betwwen 3 digits
print("{0:,}".format(10000000000000))
# "," betwwen 3 digits and +,- 
print("{0:+,}".format(10000000000000))
print("{0:+,}".format(-10000000000000))
