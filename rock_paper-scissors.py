import random
import sys

player_choice = input("Kindly choose one option \n 1. Rock \n 2. Paper \n 3. Scissors \n")
computer_choice = random.randint(1, 3)

player = int(player_choice)
computer = int(computer_choice)

if player < 1 | player > 3:
    sys.exit("Kindly choose a valid option")
elif player == computer:
    print("You Lost!, system chosed " + str(computer))
else:
    print("You Won! system chosed " + str(computer))
    