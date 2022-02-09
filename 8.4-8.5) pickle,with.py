import pickle
#what is pickle?=텍스트 상태의 데이터가 아닌 파이썬 객체 자체를 파일로 저장하는 것 입니다.

#Pickle Write
# profile_file = open("profile.pickle", "wb") #wb = write and binary
# profile = {"name": "mumu", "age": 20, "hobby": ["snowboard","game","tennis","coding"]}
# print(profile)
# pickle.dump(profile, profile_file) #profile's info save it to file.
# profile_file.close()
#OUTPUT: {'name': 'mumu', 'age': 20, 'hobby': ['snowboard', 'game', 'tennis', 'coding']}


#Pickle Read
profile_file = open("profile.pickle", "rb") #rb = read and binary
profile = pickle.load(profile_file) #bring to profile  from file
print(profile)
profile_file.close()
#OUTPUT: {'name': 'mumu', 'age': 20, 'hobby': ['snowboard', 'game', 'tennis', 'coding']}


#WITH
# with open("study.txt", "w", encoding="utf8") as study_file:
#     study_file.write("I LOVE PYTHON!")
with open("study.txt", "r", encoding="utf8") as study_file:
    print(study_file.read())
