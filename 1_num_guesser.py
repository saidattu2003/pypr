import numpy as np
import random
number_of_chances=10
real_number=random.randint(1,100)
print("Welcome to the number guesser game!")
print("You have 10 chances to guess the number between 1 and 100")
for i in range(number_of_chances):
    guess=int(input("please enter an number between 1 and 100\n"))
    if(guess>real_number):
        print("your guess is greater")
    elif(guess<real_number):
        print("your guess is smaller")
    else:
        print("Congratulations! You have guessed the number")
        break
    print("You have",number_of_chances-i-1,"chances left")
print("The number was",real_number)
if(i==number_of_chances-1):
    print("You have used all your chances")
    print ("Game Over")




