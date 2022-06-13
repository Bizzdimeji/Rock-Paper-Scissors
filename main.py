import random
from tkinter import END


while True:
	print("[1]. For Rock, \n [2]. For Paper, and \n [3]. For Scissor \n")	
	option = int(input("User turn: "))
	while option > 3 or option < 1:
		option = int(input("Please enter a valid input: "))
		
	if option == 1:
		choice = 'Rock'
	elif option == 2:
		choice = 'Paper'
	else:
		choice = 'Scissor'
		
	print("Player\'s option is: " + choice)
	print("\nCPU\'s turn.......")

	comp_choice = random.randint(1, 3)
	

	while comp_choice == option:
		comp_choice = random.randint(1, 3)

	if comp_choice == 1:
		comp_choice_name = 'Rock'
	elif comp_choice == 2:
		comp_choice_name = 'Paper'
	else:
		comp_choice_name = 'Scissor'

	print("Player: ", choice , end = ' ; ')	
	print("CPU: ", comp_choice_name )
	

	#print("Computer\'s choice is: " + comp_choice_name )
	#print('User\'s choice is', choice)

	if((option == 1 and comp_choice == 2) or
	(option == 2 and comp_choice ==1 )):
		print("Paper wins => ", end = "")
		result = "Paper"
		
	elif((option == 1 and comp_choice == 3) or
		(option == 3 and comp_choice == 1)):
		print("Rock wins =>", end = "")
		result = "Rock"
	else:
		print("Scissor wins =>", end = "")
		result = "Scissor"

	if result == choice:
		print("<==> Player wins <==>")
	else:
		print("<==> CPU wins <==>")
		
	print("Do you want to play again? (Y/N)")
	ans = input('>>>>>')

	if ans == 'n' or ans == 'N':
		break
	
print("\nThanks for playing")
