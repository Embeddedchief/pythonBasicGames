import random
import sys
from enum import Enum

# class game(Enum):
#     Rock = 1
#     Paper = 2
#     Scissors = 3

#     print(game.Rock.value)
#     sys.exit()

player_choice = input("Kindly choose one option \n 1. Rock \n 2. Paper \n 3. Scissors \n")
computer_choice = random.randint(1, 3)

player = int(player_choice)
computer = int(computer_choice)

if player < 1 | player > 3:
    sys.exit("Kindly choose a valid option")
elif player == computer:
    print("You Lost!, system chosed "+ computer)
else:
    print("You Won! system chosed🥳 " + computer)


student_names = ["Isreal", "Isaiah", "Choi"]
print(student_names[0])    