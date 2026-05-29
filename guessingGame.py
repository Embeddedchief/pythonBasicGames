####Algorithm
#Import modules for random
#Welcome users
#Take input from user for range of random numbers to generate
#Check if input is digit, if no (quit the program) if yes (go throught to next step)
#Check if digit is greater than 0, if no(Ask the user to pick a number greater than zero and quit) if yes (go throught to the next step)
#Convert digit to int
#Create random number with user range
#Ask user to make a guess between 0 and the selected range
#Check if guess is digit, if no (ask user to type number and retake the inital step) if yes (go throught to next step)
#Check if guess = generated random, if yes (You are correct and end the game) if no(you are in correct return to guessing step)


#Import modules for random
import random

#Welcome users
print("Welcome to a guessing game, im excited to have you")

#Take input from user for range of random numbers to generate
guess_range = input("Type the range of numbers you want to guess from ")

#Check if input is digit, if no (quit the program) if yes (go throught to next step)
#Check if digit is greater than 0, if no(Ask the user to pick a number greater than zero and quit) if yes (go throught to the next step)

if guess_range.isdigit() :
    guess_range = int(guess_range)
    if guess_range <= 0:
        print("Kindly input a number greater than 0")
        quit()
else : 
    print("Kindly type a digit")
    quit()


#Convert digit to int
guess_range = int(guess_range)

#Create random number with user range
random_number = random.randint(0, guess_range)


#Check if guess is digit, if no (ask user to type number and retake the inital step) if yes (go throught to next step)
while True:
    #Ask user to make a guess between 0 and the selected range
    guess_number = input("Now make a guess between 0 and " + str(guess_range) + " ")
    if guess_number.isdigit() :
        guess_number = int(guess_number)
    else :
        print("Kindly type a number next time")
        continue

    #Check if guess = generated random, if yes (You are correct and end the game) if no(you are in correct return to guessing step)
    if guess_number == random_number :
        print("You are correct")
    else :
        print("You are incorrect, guess again")

