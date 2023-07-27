import random

Option = ['a','b','c']
Chance = 3
NoOfChange = 0
ComputerPoint = 0
UserPoint = 0
Tie = 0
Error = 0

UserName = input("[*] Enter Your Name: ")
print("\n\t\tWelcome to Stone Paper Scissor Game")
print("\n\t\t\t<<< Game Rules >>>\n")
print("User Want To Stone Put Option[a]\nUser Want To Paper Put Option[b]\nUser Want To Scissor Put Option[c]\n")
print("\t\t\tOnly Three Rounds\n")

while NoOfChange < Chance:

	UserInputOption = input("[*] <<< Stone-Paper-Scissor >>> Options[a,b,c] : ")
	ComputerInputOption = random.choice(Option)
	
	if UserInputOption == ComputerInputOption:
		Tie = Tie + 1
		print("\nZero Points Match Tied! \n[*] User Option: {} \n[*] Computer Option: {}".format(UserInputOption,ComputerInputOption))
		
	elif UserInputOption == 'a' and ComputerInputOption == 'b':
		ComputerPoint = ComputerPoint + 1
		print("\n[*] User choice: {} \n[*] Computer Choice {}".format(UserInputOption,ComputerInputOption))
		print("Computer Won!")
		print("\nUser Point: {} \n Computer Point: {}".format(UserPoint,ComputerPoint))
		
	elif UserInputOption == 'b' and ComputerInputOption == 'a':
		UserPoint = UserPoint + 1
		print("\n[*] User choice: {} \n[*] Computer Choice {}".format(UserInputOption,ComputerInputOption))
		print("User({}) Won!".format(UserName))
		print("\nUser Point: {} \nComputer Point: {}".format(UserPoint,ComputerPoint))
		
	elif UserInputOption == 'b' and ComputerInputOption == 'c':
		ComputerPoint = ComputerPoint + 1
		print("\n[*] User choice: {} \n[*] Computer Choice {}".format(UserInputOption,ComputerInputOption))
		print("Computer Won!")
		print("\nUser Point: {} \nComputer Point: {}".format(UserPoint,ComputerPoint))
		
	elif UserInputOption == 'c' and ComputerInputOption == 'b':
		UserPoint = UserPoint + 1
		print("\n[*] User choice: {} \n[*] Computer Choice {}".format(UserInputOption,ComputerInputOption))
		print("User({}) Won!".format(UserName))
		print("\nUser Point: {} \nComputer Point: {}".format(UserPoint,ComputerPoint))
		
	elif UserInputOption == 'c' and ComputerInputOption == 'a':
		ComputerPoint = ComputerPoint + 1
		print("\n[*] User choice: {} \n[*] Computer Choice {}".format(UserInputOption,ComputerInputOption))
		print("Computer Won!")
		print("\nUser Point: {} \nComputer Point: {}".format(UserPoint,ComputerPoint))
		
	elif UserInputOption == 'a' and ComputerInputOption == 'c':
		UserPoint = UserPoint + 1
		print("\n[*] User choice: {} \n[*] Computer Choice {}".format(UserInputOption,ComputerInputOption))
		print("User({}) Won!".format(UserName))
		print("\nUser Point: {} \nComputer Point: {}".format(UserPoint,ComputerPoint))
		
	else:
		Error = Error + 1
		print("Your Option Is Wrong :-) Try Options ['a','b','c']")
		
	NoOfChange = NoOfChange + 1
	print("[*] {} Left Out of {}\n".format((Chance - NoOfChange),Chance))

print("\t\t\tGame Over!\n")

if UserPoint == ComputerPoint:
	print("\t\t\tMatch Draw!\n")

elif ComputerPoint > UserPoint:
	print("\t\tComputer Won the Match!\n")

else:
	print("\t\tUser({}) Won the Match!\n".format(UserName))
	
print("Match Tied: {}\nError's ->  {}\nUsername: {} \n[*] User Total Point: {} \n[*] Computer Total Point {}".format(Tie,Error,UserName,UserPoint,ComputerPoint))
