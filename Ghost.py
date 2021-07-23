from random import randint
import time 


#welcome user

print("what is your name? ")
name = input(" ")

time.sleep(1)
print("Get ready to play the \033[1;31;40mGhost Game!!! \033[0;37;40m")
time.sleep(0.5)

brave = True
score = 0

while brave:
    ghostDoor = randint(1,3)
    print(" ")
    print("There are 3 door ahead..")
    time.sleep(1)
    print("One has a ghost behind it")
    time.sleep(0.5)
    print(" ")
    print("which door do you open? 1, 2 or 3?")
    door = int(input(" "))


    if door == ghostDoor:
        print(" ")
        print("You open the door...")
        time.sleep(0.5)
        print("THERE IS A GHOST BEHIND IT")
        brave = False

    else:
        print("There is no Ghost")
        time.sleep(1)
        print(" ")
        print("You have entered the next room!!")
        score = score + 1


print("Run Away!!")
time.sleep(0.5)
print("Too slow")
time.sleep(1)
print("Game over! Your score was ", score, "Try again!")
