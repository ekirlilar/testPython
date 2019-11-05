def winorlose(status):
	print("called win or lose")
	print("************(ツ)************\n")
	print ("you", status, "!Would you like to play again?")

	choice = input("Y / N")
	print(choice)

	if (choice is "N" ) or (choice is "n"):
		print("You chose to quit.")
		exit()

	elif (choice is "Y") or (choice is "y"):
	
		global player_lives
		global computer_lives
		global player
		global computer
		global choices
		player_lives = 5
		computer_lives = 5
		player = False
		player = choices[radiant(0,2)]