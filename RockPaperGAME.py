import random

options = ["Rock", "Paper", "Scissor"]
player = 0
computer = random.choice(options)

while player not in options:
    player = input("Enter the Option (Rock, Paper, Scissor): ")




print(f"player: {player}")
print(f"computer: {computer}")

if player == computer:
    print("It's a TIE")

elif player == "Rock" and computer == "Scissor":
    print("Player Wins")

elif player == "Paper" and computer == "Rock":
    print("Player Wins")

elif player == "Scissors" and computer == "Paper":
    print("Player Wins")

else:
    print("Computer Wins")
