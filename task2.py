import random

number=random.randint(1,10)

#Guess the number

guess=int(input("Enter the guess number 1 to 10:"))

if(guess==number):
    print("Corect Guess!!:")

else:
    print("Wrong Guess!!")
    print("Correct Number:",number)
