import random

def get_choices():
  player_choice = input("Enter a choice (rock, paper, scissors, lizard, spock): ")
  options = ["rock", "paper", "scissors", "lizard", "spock"]
  computer_choice = random.choice(options)
  choices = {"player": player_choice, "computer": computer_choice}
  return choices

def check_win(player, computer):
  print(f"You chose {player}, computer chose {computer}")
  if player == computer:
    return "It's a tie!"
  elif player == "scissors":
    if computer == "spock":
      return "Spock smashes Scissors! You lose."
    else:
      return "Paper covers rock! You win!"
  elif player == "rock":
    if computer == "paper":
      return "Paper covers rock! You lose."
    else:
      return "Scissors cuts paper! You win!"
  elif player == "paper":
    if computer == "scissors":
      return "Scissors cuts paper! You lose."
    else:
      return "Rock crushes Lizard! You win!"
  elif player == "lizard":
    if computer == "rock":
      return "Rock crushes Lizard! You lose."
    else:
      return "Lizard poisons Spock! You win!"
  elif player == "spock":
    if computer == "lizard":
      return "Lizard poisons Spock! You lose."
    else:
      return "(and as it always has) Rock crushes Scissors! You lose."
  elif player == "rock":
    if player == "scissors":
      return "(and as it always has) Rock crushes Scissors! You win!"
    else:
      return "Scissors decapitates Lizard! You lose."
  elif player == "scissors":
    if computer == "lizard":
      return "Scissors decapitates Lizard! You win!"
    else:
      return "Lizard eats Paper! You lose."
  elif player == "lizard":
    if computer == "paper":
      return "Lizard eats Paper! You win!"
    else:
      return "Paper disproves Spock! You lose."
  elif player == "paper":
    if computer == "spock":
      return "Paper disproves Spock! You win!"
    else:
      return "Spock VAPORIZES Rock!!!!! You lose."
  elif player == "spock":
    if computer == "rock":
      return "Spock VAPORIZES Rock!!!!! You win!"
    else:
      return "Spock smashes Scissors! You win!"


choices = get_choices()
result = check_win(choices["player"], choices["computer"])
print(result)

