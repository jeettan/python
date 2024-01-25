
import random

#What is the goal. First it has two areas, the computer and ourself

computer = ["rock","paper","scissors"]
self = input("Rock, paper or scissors\n")

if self == "scissor" or self == "Scissor":
	self = "scissors"

self = self.lower()

if (self != 'rock' and self != 'paper' and self != 'scissors'):
	print("incorrect input")
	quit()

print("You have chosen", self)

computer = random.choice(computer)

print("Computer has chosen", computer)

#define draw conditions

if (computer == self):
	print("It's a draw")
	quit()

#define losing conditions

if(computer == "rock" and self == "scissors") or (computer == "paper" and self == "rock") or (computer == "scissors" and self == "paper"):
	print("You lose")
	quit()

else:
	print("Congratulations, you won")







