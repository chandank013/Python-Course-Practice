# WAP to Guess the number between 1 - 10.

import random

num1 = random.randint(1,10)

guess = 0
while guess != num1 :
    guess = int(input("Enter the number to guess:"))
    if guess > num1:
        print("It is greater")
    elif guess < num1:
        print("It is samaller")
    else:
        print("Yes, you got the number")



 