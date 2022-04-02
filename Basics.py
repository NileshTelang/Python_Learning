from pprint import pprint
from re import X


print("Hey Nova \n")
# myAge = 21
# myself = "My Age is " + str(myAge) + " .\n"
# myAge = "25"
# yo = myself + "I have an elder brother of "+ myAge +" Age .\n"
# print(yo.upper())
# print(yo.isupper())
# print(yo.upper().isupper())
# print(len(yo))
# print(yo[31])
# print(yo.index("brother"))
# print("\n"+yo.replace("elder","older"))

# print(3 + 5 * 7)
# from math import*

# print(ceil(40.31))
# print(floor(31.41))
# print(pow(41,31))
# print(sqrt(1681))

# hey = input("Hey in spanish Is : ")
# solong = input("so long in years : ")
# print(hey + " Amigo My Friend ! It's been Like what " + solong + " years now .\n")

# from turtle import*
# color("red")
# begin_fill()
# pensize(3)
# left(50)
# forward(133)
# circle(50,200)
# right(140)
# circle(50,200)
# forward(133)
# end_fill()

# friends = ["trisha" , "hemamalini" , "dheera" , "sanu" , "justinTatya 420" ]
# print("My BFF Is : " + friends[0])
# friends.insert(1,"puja")
# friends.remove("sanu")
# friends.append("justinGod")
# friends.append("sani ka ?")
# friends.append("justinGod")
# print(friends[:2])
# print(friends[2:5])
# print(friends.pop())
# print(friends.count("sani ka ?"))
# friends.sort()
# print(friends)

# # stringReversing
# name = input("String To be reversed Is  : ")
# print("The reversed string Is : " + name[::-1])

# pets = ("cat","dog")
# paw = [(4),(5,4),(6,9,7)]
# print("I have a " + pets[0] + " and she has " + str(paw[0]) + " paws .")

# def fu() :
#     print("EZEKIEL : Hey ... ")
#     print("TONY : hellow ...")
#     print("EZEKIEL : guess what ?!!") 
#     print("TONY : what ...")  
#     print("EZEKIEL : you really wanna know ") 
#     print("TONY : yeahhh ..ss") 
#     print("EZEKIEL : fff Fuck Youu sss....")
#     print("TONY : Fuck you ")
#     print("EZEKIEL : fuckk youuu")
#     print("TONY : no fuckk youuuuuu")
#     print("EZEKIEL : what's your name ?? ...")
#     print("TONY : what ??")  
#     print("EZEKIEL : what Is your NAME sss ?? ...")
#     print("TONY : TONY ...") 
#     print("EZEKIEL : Fuck You , TONY yy ....")
#     print("TONY : what's your name ??") 
#     print("EZEKIEL : EZEKIEL ...")
#     print("TONY : Fuck You EZEKIEL ..lll") 
#     print("EZEKIEL : fuck youu")
#     print("TONY : fuck you ")
#     print("FUCK YOU")

# call = input("Enter Your Choice (1 / 0) : ")
# if call == 'True' or '1' :
#     fu()
# else : 
#     print("Fuck You !")

# # dictionaries
# getP = {
#     "Nil" : "Trisha",
#     "Hikkie" : "Yukinan",
#     "Ayanakoji" : "Horikita",
#     "Eren Yeager" : "Mikasa",
#     "Tatakae" : "Fight" ,
#     "41" : '31' ,
# }

# partnerName = input("Enter Your Name : ")
# print("Your Pride Is : " + getP.get(partnerName , "DeadAlready"))  # or getP["Nil" / partnerName]

# # while Loop
# i = 0
# while i <= 10 :
#     print(i)
#     i += 1
# print("while loop Is Over")

# secret_word = "Nil"
# guess = ""
# guessCount = 0
# guess_limit = 3
# outOf_guesses = False



# while guess != secret_word and not (outOf_guesses):
#     if guessCount < guess_limit :
#         guess = input ("Enter The Secret Word : ")
#         guessCount += 1
#     else :
#         outOf_guesses = True
# if outOf_guesses :
#     print("You done bruh ' !")
# else :
#     print("You won")

# for  letter in "Nilesh Telang" :
#     print(letter)

# def facto (num) :
#     res = 1
#     for i in range (num) :
#         i = num
#         res = res * i 
#         num -= 1
#     return res

# num = int(input("Enter num to find facto : "))
# print(facto(num))

# # try except block
# try : 
#     num = int(input("Enter The num : "))
#     print(num)
# except ValueError as err:
#     print(err)
#     # print("Invalid Input")

# file = open("Hola.txt","w") #w = create & overwrite, a = append , r = read , r+ = read / write
# file.write("Hola Amigo\nGosh you are beautiful !\n")
# file = open("Hola.txt","a")
# file.write("Fuck")
# file = open("Hola.txt","r")
# print(file.readable())
# print(file.read())
# file.close()

# from student import  student 
# student1 = student("Nilesh Telang" , "2nd Year" , "Computer" , 9.2)
# print(student1.name)

from answ import answer
qprompt = [
    "what's my petName ?? \n a) Nil \n b) Hikkie \n c) Nova \n d)daddy \n\n",
    "what's my pet's Name ?? \n a)meow \n b)mani \n c)mani jr \n d)weiwie \n\n"
]
answers = [
    answer(qprompt[0],"a"),
    answer(qprompt[1],"c")
]

def test(ques) :
    score = 0
    for que in ques :
        answer = input(que.prompt)
        if answer == que.anny :
            score += 1
    print("You Got "+str(score)+"/"+str(len(ques))+" Correct !") 
    
test(answers) 

print("\n")

