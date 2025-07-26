import random

guess=0
iin=-1
rnd=random.randint(1,100)

print("***********WELLCOME TO GUESS THE NUMBER GAME************\n".center(60))
print("*****INSTRUCTIONS*****".center(60))
print("In this game you want to guss number wich, \nselected by game in between 1 to 100 after your guess \ni will give you a hint then guess agane, \nthe game is all about how many guess you gat to guess. \nLets begine...\n")

while True:
    
    try:
        iin=int(input("Enter your guess-->"))
    except:
        print("YOUR INPUT MUST BE INTGER")
        continue
    guess=guess+1
    if iin==rnd:
        print(f"***********GOOD JOb YOU GOT IT IN {guess} GUESS !!!.***********")
        break
    
    elif iin<rnd:
        print("TRY BIGGER SOMTHING")
        
    elif iin>rnd:
        print("TRY SMALER SOMTHING")
