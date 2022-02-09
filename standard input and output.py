print("python", "java", "c++", sep=" vs ")
print("python", "java", "c++", sep=" vs ", end="?")

#---------
import sys
print ("python","java", file=sys.stdout)  #표준 출력
print ("python","java", file=sys.stderr) #따로 에러 처리

#---------
scores = {"math":0,"English":50, "Coding":  100}
for subject, score in scores.items():
    print(subject, score)
    #print(subject.ljust(8), str(score).rjust(4), sep=":")