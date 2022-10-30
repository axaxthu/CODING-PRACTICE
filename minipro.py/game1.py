#play a game of rock paper scissors with the computer
import random

user_input=input("ENTER A CHOICE[ROCK,PAPER,SCISSORS]: ") 
possible_actions=["ROCK","PAPER","SCISSORS"]
computer_action= random.choice(possible_actions)
print("COMPUTERS'S CHOICE:",computer_action)

if user_input==computer_action:
    print("IT'S A TIE")

elif user_input=="ROCK":
    if computer_action=="PAPER":
        print("WINNER IS COMPUTER")
    else:
        print("YOU ARE THE WINNER")

elif user_input=="PAPER":
    if computer_action=="ROCK":
        print("YOU ARE THE WINNER")
    else:
        print("COMPUTER IS THE WINNER")
else:
    if computer_action=="ROCK":
        print("WINNER IS COMPUTER")
    else:
        print("YOU ARE THE WINNER")    


      
      