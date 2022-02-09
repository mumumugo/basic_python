#write on file
# score_file = open("score.txt", "w", encoding ="utf8") #write
# print("Math: 80", file=score_file)
# print("English: 80", file=score_file)
# score_file.close() #the file must  be closed after finish

# score_file = open("score.txt", "a", encoding="utf8") #add
# score_file.write("Science: 85")
# score_file.write("\nCoding: 100")
# score_file.close() #the file must be closed after finish


#read  file
# score_file = open("score.txt", "r", encoding ="utf8") #read
# #print(score_file.read()) # read all text
# print(score_file.readline()) # read line by line
# print(score_file.readline(), end="") # no space between line add end=" "
# print(score_file.readline())
# print(score_file.readline())
# score_file.close()

# score_file = open("score.txt", "r", encoding ="utf8")
# while True:
#     line = score_file.readline()
#     if not line:
#         break
#     print(line, end="")
# score_file.close()

score_file = open("score.txt", "r", encoding ="utf8")
lines = score_file.readlines() #store in LIST
for line in lines:
    print(line, end ="")
score_file.close()







