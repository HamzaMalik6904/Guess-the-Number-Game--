import random
target=random.randint(1,100)

while True:
    userchoice=int(input("Guess the number:"))
    if(userchoice ==  target):
        print("Success right Guess :)")
        break
    elif(userchoice >=target):
        print("Your num is too high guess lower :)")
    elif(userchoice<=target):
        print("Your num is too lower guess higher :) ")
    else:
        print("You enter wrong num :(")


print("----Game over---")