from getpass import getpass as input
#import random
import emoji
print(emoji.emojize("This is a game of :rock: and :paper: and :scissors:"))
print(emoji.emojize("R stands for Rock :rock:"))
print("P stands for Paper")
print(emoji.emojize("S stands for Scissors :scissors:"))

player1_action = input("Enter a choice(R,P,S): ")
possible_actions = ["R","P","S"]
#player2_action = random.choice(possible_actions)
player2_action = input("Enter a choice(R,P,S): ")
print("Player 1 selected", player1_action, "Player 2 selected", player2_action)
if player1_action == player2_action:
  print("Both players selected", player1_action, "It's a tie!")
elif player1_action == "R":
  if player2_action == "S":
    print("R smashes S, Player 1 wins!")
  else:
    print("P covers R, Player 2 wins!")
elif player1_action == "P":
  if player2_action == "R":
    print("Paper covers rock, Player 2 wins!")
  else:
    print("Scissors can cut paper! Player 1 wins!")
elif player1_action == "S":
  if player2_action == "P":
    print("Scissors can cut paper! Player 1 wins!")
  else:
    print("Rock will smash scissors! Player 2 wins!")