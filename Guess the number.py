import random
from art import logo
import os

def game(attempts):
    while attempts > 0:
        print(f"You have {attempts} remaining attempts to guess:")
        guess = int(input("Make a guess: "))
        if guess > number:
            print("Too high")
            attempts -= 1
        elif guess < number :
            print("Too low")
            attempts -= 1
        elif guess == number: 
            print(f"Congratulations You guessed right !!! .. the number is {number}" )
            return
        else:
            print("Invalid Input .. Wrong choice any way")
            attempts -= 1

        if attempts != 0:
            print("guess again")

    print("You have 0 attempts left")
    print("You run out of attempts .. You lose")
    return




os.system('cls')
print(logo)
print("************Welcome to 'Guess The Number' game **********")

print("I am thinking of a number between 0 and 100")
number = random.randint(0,100)

level = int(input("Choose the difficulty: Type '1' for easy or '2' for hard: "))
if level == 1 :  #attempts = 10
    game(10)
else: #attempts = 5
    game(5) 


