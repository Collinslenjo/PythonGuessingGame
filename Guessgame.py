'''
@Author name = Collins Lenjo
@email = collinslenjo.cl@gmail
@Url = collinslenjo.co.nf
My Simple python Workflow to guess a number between 1 to 100
'''
import random
def main():
	#Initialize the programm
	print "Guess a number between 1 and 100"
	# randomNumber = 35 this was for debugging purposes Only
	randomNumber = random.randint(1,100)
	found = False # Flag variable to see if you guessed it
	# Run through the Guessing process
	while not found:
		userGuess = input("Your Guess: ")
		if userGuess == randomNumber:
			print "You got it!"
			found = True
		elif userGuess > randomNumber:
			print "Guess a Lesser number"
		else:
			print "Guess a Higher Number"
	# print Congratulations and say Good Bye
	print "Thanks for Playing My Game"
if __name__ == "__main__":
	main()
