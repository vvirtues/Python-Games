from random import randrange
import os

os.system('cls' if os.name == 'nt' else 'clear')
print("     Welcome to 'Guess my Number'! \n \nI'm thinking of a number between 1 and 100. \nTry to guess it in as few attempts as possible.")

question = str("Take a guess: ")
num = randrange(1,100)
guess = int(input(question))

while num != guess:
	if guess < num:
		os.system('cls' if os.name == 'nt' else 'clear')
		print("Too Low. \n \n ")
		guess = int(input(question))
	elif guess > 100:
		os.system('cls' if os.name == 'nt' else 'clear')
		print("The number only goes up to 100! \n \n")
		guess = int(input(question))
	elif guess > num:
		os.system('cls' if os.name == 'nt' else 'clear')
		print("Too High. \n \n ")
		guess = int(input(question))
# doesnt work at all
	elif guess != int():
		os.system('cls' if os.name == 'nt' else 'clear')
		print("Not a number. \n \n ")
		guess = int(input(question))
	else:
		break
os.system('cls' if os.name == 'nt' else 'clear')
print("That was the correct number, congratulations!")
