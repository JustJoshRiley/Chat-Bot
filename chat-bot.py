#import random
from random import choice, randint
#Make Greeting
print("Hey There! Welcome to Rock, Paper, Knife. You will be Demolished by the Chat Bot you are playing against...Failure is inevitable.")

def get_bot_response(user_response):
    #make an array for computer.
    computer = ["Rock", "Paper", "Knife"]
    #make an array for losing the game.
    player_lost = ["You lose Mate!", "Ouch! You put the LOSE in LOSER! Thats gotta hurt!", "You Lost! Time for you to go to bed!"]
    #make an array for winning a game.
    player_wins = ["Way to go bro! I cant believe you won", "Winner! You're on a roll!", "WOW! Winning Streak? You are unstopable!"]

    player = False
    #compare the computer and user_response role
    while player == False:
        player = user_response
        # test user input
        # print(player)
        computer_choice = computer[randint(0,2)]
        # test computer input 
        # print(computer_choice)
        if computer_choice == player:
            print("Draw!")

        # Paper versus Rock
        elif computer_choice == "Paper" and player == "Rock":
            # if player == "Rock":
            print(choice(player_lost))

        #Paper Versus Knife
        elif computer_choice == "Paper" and player == "Knife":
            # if player == "Knife":
            print(choice(player_wins))

        # Rock versus Paper
        elif computer_choice == "Rock" and player == "Paper":
            # if player == "Paper":
            print(choice(player_wins))

        ######Rock Versus Knife not working
        elif computer_choice == "Rock" and player == "Knife":
            # if player == "Knife":
            print(choice(player_lost))
        
        #Knife versus Rock
        elif computer_choice == "Knife" and player == "Rock":
            # if player == "Rock":
            print(choice(player_wins))

        ####Knife versus Paper
        elif computer_choice == "Knife" and player == "Paper":
            # if player == "Paper":
            print(choice(player_lost))

user_response = " "
cont = True
while cont:
    user_response = input("Choose Rock, Paper, or Knife: ")
    get_bot_response(user_response)
    play_again = input("Would you like to play again? (yes/no) > ")
    if play_again.lower() == "no" or play_again.lower() == "done":
        cont = False
    else: 
            pass
