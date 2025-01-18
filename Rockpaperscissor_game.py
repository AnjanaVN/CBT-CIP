#python program for rock paper scissor game
import random

options = ("rock","paper","scissor")
running = True

while running:
    player = None
    sys = random.choice(options)
    while player not in options:
         player = input("Enter a choice (Rock,Paper,Scissor::)").lower()
    print(f"player:{player}")
    print(f"system:{sys}")

    if player == sys:
        print("Its a tie!")
    elif player == "rock" and sys == "scissor":
        print("You Win!")
    elif player == "paper" and sys == "rock":
        print("You Win!")
    elif player == "scissor" and sys == "paper":
        print("You Win!")
    else:
        print("You Lose!")

    nextmove = input("Wanna to play Again(y/n): ").lower()
    if nextmove == "n":
        running = False

print("Thanks for playing..........!")
