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



prompt = '> '

c = True
while c:

	computerMove = randint(0, 2)

	startgame()

	userInput = int(input(prompt))

	if userInput == 9:
		sys.exit()

	ValidatedInput = inputValidation(userInput)

	result(ValidatedInput, computerMove)

	continue_input = input('Play again [y/n]? ').upper()

	while continue_input not in 'YyNn':
		print('Incorrect input, please type y or n')
		continue_input = input((prompt))
			
	if continue_input == 'N':
		c = False

