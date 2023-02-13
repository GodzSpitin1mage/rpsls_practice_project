#Rock-paper-scissors-lizard-spock

import random

def name_to_number(name):
  if(name == 'rock'):
      return 0;
  elif(name == 'spock'):
      return 1;
  elif(name == 'paper'):
      return 2;
  elif(name == 'lizard'):
      return 3;
  elif(name == 'scissors'):
      return 4;
  else:
    print("ERROR Name")

def number_to_name(number):
  if(number == 0):
      return 'rock';
  elif(number == 1):
      return 'spock';
  elif(number == 2):
      return 'paper';
  elif(number == 3):
      return 'lizzard';
  elif(number == 4):
      return 'scissors';
  else:
      print("ERROR Number")
def rpsls(player_choice):


  print("\n")

  print("Player chooses " + player_choice)

  player_number = name_to_number(player_choice)

  comp_number = random.randrange(0, 5)

  comp_choice = number_to_name(comp_number);

  print("Computer chooses " + comp_choice)

  difference = (comp_number - player_number) % 5

  if(difference == 1 or difference == 2):
    print("Computer wins.")
  elif(difference == 4 or difference == 3):
    print("Player wins!")
  elif(difference == 0):
    print("Player and computer tie!")

rpsls("rock")
rpsls("spock")
rpsls("paper")
rpsls("lizard")
rpsls("scissors")

