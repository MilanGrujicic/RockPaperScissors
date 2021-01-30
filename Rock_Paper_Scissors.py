import sys
from random import randint

def startgame():
	print(
	''' What do you want to play:
		[0] Rock
		[1] Paper
		[2] Scissors

		[9] Quit
	''')


def inputValidation(userInput):

	while userInput not in [0, 1, 2, 9]:
		print('Incorrect input, please insert a value between 0 and 2')
		userInput = int(input(prompt)) 
	return userInput 

	

def result(ValidatedInput, computerMove):
	moves = {0:'Rock', 1:'Paper', 2:'Scissors'}

	print(f'You played: {moves[ValidatedInput]}\nComputer played: {moves[computerMove]}')
	
	w = 'You Win!'
	l = 'You Lose!'
	
	if ValidatedInput == computerMove:
		print("It's a draw")
	elif ValidatedInput == 0 and computerMove == 1:
		print(l)
	elif ValidatedInput == 0 and computerMove == 2:
		print(w) 	
	elif ValidatedInput == 1 and computerMove == 0:
		print(w)
	elif ValidatedInput == 1 and computerMove == 2:
		print(l)
	elif ValidatedInput == 2 and computerMove == 0:
		print(l)
	elif ValidatedInput == 2 and computerMove == 1:
		print(w)


computerMove = randint(0, 2)
prompt = '> '

startgame()

userInput = int(input(prompt))
if userInput == 9:
	sys.exit()
ValidatedInput = inputValidation(userInput)

result(ValidatedInput, computerMove)

