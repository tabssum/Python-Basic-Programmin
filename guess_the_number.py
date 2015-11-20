#!/bin/usr/python
from random import randint
def guess_a_number():
    attempt_number=1
    random_number=randint(1,10)
    print(random_number)
    while(attempt_number<=3):       
        guess_number=input("Guess a number between 1 to 10 for "+str(attempt_number)+" attempt:=")
        if random_number == guess_number :
            print("Congratulations...............Your guess is correct")
            return
        else:
            if random_number < guess_number:
                print("Guessed Number is too high")
            else:
                print("Guessed Number is too low")            
        attempt_number=attempt_number+1
    print("No more attempts allowed")



guess_a_number()
