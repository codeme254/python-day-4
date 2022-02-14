# The Rock, Paper, Scissors game
# rock wins agains scissors
# scissors wins against paper
# paper wins against rock

import random
user_choice = int(input("What do you choose? Type 0 for rock, 1 for paper and 2 for scissors: "))
computer_choice = random.randint(0, 2)

if user_choice >= 3 or user_choice < 0:
    print("You typed an invalid number you loose")
elif user_choice == 0 and computer_choice == 2:
    print(f"You win")
elif computer_choice == 0 and user_choice == 2:
    print("You loose")
elif computer_choice > user_choice:
    print(f"You loose")
elif user_choice > computer_choice:
    print(f"You loose")
elif computer_choice == user_choice:
    print("It's a draw.")



