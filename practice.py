#변수 variable basic practice
animal = "냐옹이"
name = "몰랑이"
age = 5
is_adult = age>4
age =3

#print("우리집 " + animal + "이름은 " +name+ "에요, " "나이는 " +str(age) + "살 입니다.")
print("우리집",animal,"이름은",name,"에요," "나이는",age, "살 입니다.")
# use ',' instead of '+' /// use ',' always include one space at the end.
print(name +"는 어른인가요?" + str(is_adult))

#QUIZ1
#using variable and output
# variable = station
# "사당", "신도림", "인천공항" 순서대로 입력
#statement = xx행 열차가 들어오고 있습니다.
first_station = "사당"
second_station = "신도림"
third_station = "인천공항"

print( first_station, "행 열차가 들어오고 있습니다.")
print( second_station, "행 열차가 들어오고 있습니다.")
print( third_station, "행 열차가 들어오고 있습니다.")


#operator basic practice
print(2**3) #2^3=8
print(5%3) #2
print(10%3) #1
print(5//3) #1
print(10//3) #3
#
print(abs(-4)) #4
print(pow(4,2)) #4^2 = 16
print(max(5,12)) #12
print(round(3.14))  #3
print(round(4.88))  #5

from math import *
from sre_parse import expand_template #math library
print(floor(4.98)) #내림  4
print(ceil(4.14)) #올림  5
print(sqrt(16)) #제곱근  4
print()

from random import * #random library
print("random function(랜덤함수) ")
print(random()) # create 0.0 ~1.0 미만의 random number.
print(random()*10) #create 0.0 ~10.0 미만의 random number.
print(int(random()*10)) #create 0 ~10미만의 (no decimal) random number.
print(int(random()*10)+1) #create 1 ~10미만의 (no decimal) random number.

print(randrange(1,46)) # create 1~46 미만의 random number (1~45)
print(randint(1,46)) # create 1~46 이하의 random number(1~46)

#QUIZ 2
#random date, in 27days, except every date1~3.
#statement- 오프라인 스터디 모임 날짜는 매월  x일로 선정되었습니다.
from random import *
date = randint(4,28)
print("오프라인 스터디 모임 날짜는 매월",  date,"일로 선정되었습니다.")


#4-1) string
sentance1 ='I am a student. '
sentance2 = "and python is easy"
sentance3 = """
I am a student.
and python is easy
"""
print(sentance1)
print(sentance2)
print(sentance3)


social = "930927-224845"
print("birthyear:", "19"+social[0:2])
print("birthdate:", social[2:6])
print("last 4 digit:", social[-4:])

python = "Python is Amazing"

print(python.lower())
print(python.upper())
print(python[1].isupper())
print(python.replace("Python","C++"))
print(python.replace("python","C++"))

index = python.index("n") #find first place of "n"
print(index)
index = python.index("n",index+1) #find second place of "n" 
print(index)
print(python.count("n"))

#문자열 포맷
print("I am %d years old" %20) 
print("I love %s." %"cats and dogs") #s means string
print("Love is start with alphabet %c." %"L") #c means character
print("I love %s and %s color." %("orange", "univertial blue")) #s means string
print("I am {} years old".format(30))
print("I love color {} and color {}".format("yellow","black"))
print("I love color {0} and color {1}".format("yellow","black"))
print("I love color {1} and color {0}".format("yellow","black"))
print("I am {age} years old and I love color {color}".format(age =19, color ="blue"))
age = 20 
color = "red"
print(f"I am {age} years old and I love color {color}.")

#탈출문자
#\n: 줄바꿈
print("백문이 붙여일견 \
백견이 불여일타")
print("백문이 붙여일견 \n백견이 불여일타")
print("I am practicing with 'nado coding' ") #output quotation mark
print('I am practicing with "nado coding" ')
print("I am practicing with \"nado coding\" ")
print('I am practicing with \'nado coding\' ')

#\\ : 문장 내에서  \ (하나의 slace)
print("C:\\FIND MY DOCUMENT \\ SHOW ME \\\\THIS ")
# \r : 커서를 맨 앞으로 이동
print(" Red apple \rPine")
#\b: 백 스페이스 (한 글자 삭제 )
print("Redd\b Apple")
#\t: 탭
print("Red\tApple")


#Quiz3) 
#make a password 
# example http://naver.com
#rule1: http://부분은 제외 => naver.com
#rule2: 처음 만나는 점(.) 이후 부분은 제외 => naver
#rule3: 남은 글자 중 처음 세자리 + 글자 갯수 + 글자 내 'e' 갯수 + "!"로 구성
#                         (nav)                        (5)                  (1)                          (!)
#sample: nav51!
url = "http://naver.com"
my_str = url.replace("http://","")
print(my_str) #rule1
my_str = my_str[:my_str.index(".")]
print(my_str) #rule2
password = my_str[:3] + str(len(my_str)) + str(my_str.count("e")) +"!" #int는 str( ) 로 감싸주기
print("Website {}'s password will be ({}).".format(url,password))


#5.1) LIST
subway = [10,20,30]
print(subway)
subway = ["noze", "mumu", "nozeworld", "way_b"]
print(subway)
subway.append("lachica") # add to the end list
print(subway)
subway.insert(2,"iky") #list 사이에 insert
print(subway)
print(subway.pop()) #take out a list  (lachica)
print(subway) #after take out  (no more lachica is showing)
subway.append("noze")
print(subway.count("noze"))

#sort
num_list = [4,56,3123,6,1,99,77]
num_list.sort()
print(num_list)

#reverse
num_list.reverse()
print(num_list)

#clear
num_list.clear()
print(num_list)

#다양한 자료형 사용 
multi_list = [31,"noze", False]
num_list = [4,56,3123,6,1,99,77]
multi_list.extend(num_list)
print(multi_list)

#사전
cabinet = {3:"noze", 4:"world"} 
str_cabinet = {"a-3":"hook", "a-4":"lachica"} 
print(cabinet[3]) #key가  없으면 멈춤
print(cabinet.get(3)) #key가 없으면 none으로 표시되고 계속됨.
print(cabinet.get(5,"usable"))#key가 없으면 usable라고 표시됨. 

print(str_cabinet["a-3"]) #key가  없으면 멈춤
print(str_cabinet.get("a-4")) #key가 없으면 none으로 표시되고 계속됨.

print(3 in cabinet) #true
print (5 in cabinet) #false

str_cabinet["a-3"] = "iky" #update with key
str_cabinet["a-5"] = "muze" #add new key 
print(str_cabinet)

del str_cabinet["a-5"] #delete key
print(str_cabinet)

print(str_cabinet.keys()) #only print keys
print(str_cabinet.values()) #only print values
print(str_cabinet.items()) #print both key and values
str_cabinet.clear() #clear all data 
print(str_cabinet)

#5.3) tuple튜플 (can not edit like list. but it is more faster then the list)
menu = ("pizza","pasta","deliver")
print(menu[0])
#menu.add("donkatsu") ERROR! can no add it to tuple.
(name,age,hobby) = ("noze", "27","dance")
print(name,age,hobby)

#5.4) set 집합 (중복이 안되고, 순서가 없음)
my_set = {1,2,3,4,5,5,5,3,2,1,}
print(my_set) #output: {1,2,3,4,5}

java = {"iky", "noze", "honeyj"}
python = set(["noze","iky"])
#교집합(java와 python을 모두 할수있는 )
print(java&python)
print(java.intersection(python))
#합집합 (java나 python을 할 수있는 )
print(java | python)
print(java.union(python))
#차집합 (java는 할수 있지만 python은 할수없는)
print(java-python)
print(java.difference(python))

#자료구조의 변경 
menu = {"coffee","cookies","juice","bagles"}
print(menu,type(menu))

menu = list(menu) #change set to list
print(menu,type(menu)) 

menu = tuple(menu) # change list to tuple
print(menu,type(menu))

menu = set(menu)
print(menu,type(menu))

#QUIZ4) 
# 댓글 작성자들중 추첨으로 1명은 치킨, 3명은 커피 쿠폰
# 댓글은 20명이 작성하였고 아이디는 1~20개 
#무작위 추첨, 중복 불가
#use random module's suffle and sample
#sample
#from random import *
#1st = [1,2,3,4,5]
#print(1st)
#shuffle(1st)
#print(1st)
#print(sample(1st,1))

from random import *
ppl = range(1,21) #[1,2,3,4,5,6,7,8,9,10,11,12,13,14.....,20.] #type is range
print(type(ppl))
ppl = list(ppl)
print(type(ppl))
print(ppl)
shuffle(ppl)
print(ppl)
winners =sample(ppl,4) #4명중 1명은 치킨, 나머진 커피 
print(winners)
print("1st place: {0}".format(winners[0]))
print("2st place: {0}" .format(winners[1:]))


#6.1) if
# temp = int(input("what is the temp for today: "))
# if 0<= temp <=10:
#     print("its a cold day. bring a jacket.")
# elif 11 <= temp <=30:
#     print("its a nice weahter!")
# elif 31 <= temp <= 40:
#     print("its very hot, stay at home!")
# else:
#     print("very very cold. freezing outside. do not go out.")

#6.2) for
for waiting_no in range(5): #0,1,2,3,4
    print("waiting number: {0}".format(waiting_no))

for waiting_no2 in range(1,5): #1,2,3,4
    print("waiting number2: {0}".format(waiting_no2)    )








