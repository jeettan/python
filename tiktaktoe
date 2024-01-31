import random
import sys
import os
from os import system, name 


def clear(): 
    if name == 'nt': 
        x = system('cls') 
    else: 
        x = system('clear') 

A = ['1','2','3','4','5','6','7','8','9']

checker = 1
gameState = True
turn_count = 0

def createBoard():

	print("+-------------+\n"\
		f"| {A[0]} | {A[1]}  | {A[2]}  |\n"\
		f"|---|----|----|\n"\
		f"| {A[3]} | {A[4]}  | {A[5]}  |\n"\
		f"|---|----|----|\n"\
		f"| {A[6]} | {A[7]}  | {A[8]}  |\n"\
		f"+-------------+")

createBoard()

def checkGameState():

	global gameState

	if(A[0] =="O" and A[1] == "O" and A[2] == "O"):
		print("Congrats you won")
		gameState = False

	elif(A[3] =="O" and A[4] == "O" and A[5] == "O"):
		print("Congrats you won")
		gameState = False

	elif(A[6] =="O" and A[7] == "O" and A[8] == "O"):
		print("Congrats you won")
		gameState = False

	elif(A[0] =="O" and A[3] == "O" and A[6] == "O"):
		print("Congrats you won")
		gameState = False

	elif(A[1] =="O" and A[4] == "O" and A[7] == "O"):
		print("Congrats you won")
		gameState = False

	elif(A[2] =="O" and A[5] == "O" and A[8] == "O"):
		print("Congrats you won")
		gameState = False

	elif(A[0] =="O" and A[4] == "O" and A[8] == "O"):
		print("Congrats you won")
		gameState = False

	elif(A[2] =="O" and A[4] == "O" and A[6] == "O"):
		print("Congrats you won")
		gameState = False

	elif(A[0] =="X" and A[1] == "X" and A[2] == "X"):
		print("Game over!")
		gameState = False

	elif(A[3] =="X" and A[4] == "X" and A[5] == "X"):
		print("Game over! you lost")
		gameState = False

	elif(A[6] =="X" and A[7] == "X" and A[8] == "X"):
		print("Game over! you lost")
		gameState = False

	elif(A[0] =="X" and A[3] == "X" and A[6] == "X"):
		print("Game over! you lost")
		gameState = False

	elif(A[1] =="X" and A[4] == "X" and A[7] == "X"):
		print("Game over! you lost")
		gameState = False

	elif(A[2] =="X" and A[5] == "X" and A[8] == "X"):
		print("Game over! you lost")
		gameState = False

	elif(A[0] =="X" and A[4] == "X" and A[8] == "X"):
		print("Game over! you lost")
		gameState = False

	elif(A[2] =="X" and A[4] == "X" and A[6] == "X"):
		print("Game over! you lost")
		gameState = False

	else:
		print("End of turn")


your_turn = int(input("It's your turn, enter the square you want to be at: "))

if(your_turn >=1 and your_turn <= 9):

	A[your_turn-1] = "O"

	turn_count = turn_count + 1

else:
	print("invalid number, program restarting")
	os.execl(sys.executable, sys.executable, *sys.argv)

while gameState == 1:

	clear()

	createBoard()

	while checker == 1:

		AI_turn = random.randint(1,9)

		if(A[AI_turn-1] == "O" or A[AI_turn-1] == "X"):
			continue
		else:
			print("Ai has picked:", AI_turn)
			A[AI_turn-1] = "X"
			checker = 0
			
	clear()
	createBoard()
	checkGameState()

	if(gameState == False):
		exit(1)

	while checker == 0:

		your_turn = int(input("It's your turn, enter the square you want to be at: "))

		if(your_turn < 1 or your_turn > 9):
			print("Invalid number,try again")
			continue

		elif(A[your_turn-1] == "O" or A[your_turn-1] == "X"):
			print("That spot is already taken, please try again")
			continue

		else:
			A[your_turn-1] = "O"
			checker = 1
			turn_count = turn_count + 1

	clear()		
	createBoard()
	checkGameState()

	if turn_count == 5 and gameState == True:
		print("It's a draw!") 
		break
