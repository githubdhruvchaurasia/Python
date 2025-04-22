# ------- This program is not completed -------


import random

options = ("stone", "paper", "scissor")
player = None
computer = random.choice(options)
running = True

while running:
    while player not in options:
        player = input("Enter a choice (Stone, Paper, Scissor) : ").lower()

print(f"Player : {player}")
print(f"Computer : {computer}")

if player == computer:
    print("Its a tie!")
elif player == "Stone" and computer == "Scissor":
    print("You Win!")
elif player == "Paper" and computer == "Stone":
    print("You Win!")
elif player == "Scissor" and computer == "Paper":
    print("You Win!")
else:
    print("You Lose!")

    if not input("Play Again? (y/n) : ").lower() == "y":
        running = False

print("Thanks for playing!")


# ------- This program is not completed -------
