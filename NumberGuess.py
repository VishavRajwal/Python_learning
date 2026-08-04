# random number is 27
# num[10]   num<target
# num[90]   num>target

import random
 
target = random.randint(0,100)


while True:
    userchoice = int(input("guess the target : "))
    if(userchoice == target):
        print("success : Correct Guess")
        break
    elif(userchoice < target):
        print("Your number is too small, Try taking a bigger guess....")
    elif(userchoice > target):
        print("Your number is too big, Try taking a smaller one......")

print("*****GAME OVER*****")   