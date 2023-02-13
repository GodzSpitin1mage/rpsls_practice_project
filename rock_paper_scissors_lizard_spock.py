import random
options = ['Rock', 'Paper', 'Scissor', 'Lizard', 'Spock']
name = input("Enter your name : ")
ComputerScore = 0
PlayerScore = 0
NumberOfRounds = 0
gameOn = True
print(f"Welcome {name.title()}")
while NumberOfRounds < 5:
  ComputerOption=random.choice(options)
  PlayerOption=input("Enter Rock/ Paper/ Scissor/ Lizard/ Spock :").title()
  print(f"Computer option :{ComputerOption}")
  print(f"{name.title()} option :{PlayerOption}")
  NumberOfRounds += 1
  if ComputerOption == PlayerOption:
    print('Tie')                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      #you might have to change the last PlayerOption to ComputerOption?
  elif (ComputerOption == 'Rock' and PlayerOption == 'Scissor') or (ComputerOption == 'Scissor' and PlayerOption == 'Paper') or (ComputerOption == 'Paper' and PlayerOption == 'Rock') or (ComputerOption == 'Rock' and PlayerOption == 'Lizard') or (ComputerOption == 'Lizard' and PlayerOption == 'Spock') or (ComputerOption == 'Spock' and PlayerOption == 'Scissor') or (ComputerOption == 'Scissor' and PlayerOption == 'Lizard') or (ComputerOption == 'Lizard' and PlayerOption == 'Paper') or (ComputerOption == 'Paper' and PlayerOption == 'Spock') or (ComputerOption == 'Spock' and PlayerOption == 'Rock'):
    print("Computer wins")
    ComputerScore += 1
  elif (PlayerOption == 'Rock' and ComputerOption == 'Scissor') or (PlayerOption == 'Scissor' and ComputerOption == 'Paper') or (PlayerOption == 'Paper' and ComputerOption == 'Rock') or (PlayerOption == 'Rock' and ComputerOption == 'Lizard') or (PlayerOption == 'Lizard' and ComputerOption == 'Spock') or (PlayerOption == 'Spock' and ComputerOption == 'Scissor') or (PlayerOption == 'Scissor' and ComputerOption == 'Lizard') or (PlayerOption == 'Lizard' and ComputerOption == 'Paper') or (PlayerOption == 'Paper' and ComputerOption == 'Spock') or (PlayerOption == 'Spock' and ComputerOption == 'Rock'):
    print(f"{name.title()} wins")
    PlayerScore += 1
  else:
    print("Choose a valid option to play this game.")
  print("-------------------------")
  print("")
  print(f"Round No: {NumberOfRounds}")
  print("------ Score Board ------")
  print(f"{name.title()}: {PlayerScore} | Computer: {ComputerScore}")
  print("===============================")
  print("")
  if NumberOfRounds == 5:
    gameOn = False
    break
if PlayerScore == ComputerScore:
  print("Draw!!")
elif PlayerScore > ComputerScore:
  print(f"Congrats {name.title()}, You won the game!!")
else:
  print(f"Oops Computer won the game!! Better luck next time {name.title()}!")
