# import random
from random import choice, randint
#Make Greeting
print("Hey There! Welcome to Rock Paper Scissors. You will be Demolished by the Chat Bot you are playing against...Failure is inevitable.")

def get_bot_response(user_response):
    #make an array for computer.
    computer = ["Rock", "Paper", "Scissors"]
    #make an array for losing the game.
    player_lost = ["You lose Mate!", "Ouch! You put the LOSE in LOSER! Thats gotta hurt!", "You Lost! Time for you to go to bed!"]
    #make an array for winning a game.
    player_wins = ["Way to go bro! I cant believe you won", "Winner! You're on a roll!", "WOW! Winning Streak? You are unstopable!"]

    player = False
    #compare the computer and user_response role
    while player == False:
        player = user_response
        # test user input
        print(player)
        computer_choice = computer[randint(0,2)]
        # test computer input 
        print(computer_choice)
        if computer_choice == player:
            print("Draw!")
        
        elif computer_choice == "Paper":
            if player == "Rock":
                print(choice(player_lost))
            else: #computer is Rock, player is Paper
                print(choice(player_wins))
        elif computer_choice == "Scissors":
            if player == "Rock":
                print(choice(player_wins))
            else: #computer is Scissors, player is Paper
                print(choice(player_lost))
        elif computer == "Rock":
            if player == "Scissors":
                print(choice(player_lost))
            else:
                print(choice(player_wins))
        # else:
        #     play_again = input("Would you like to play again? (yes/no) > ")
        #     if play_again == 'yes':
        #         player = False
        #         computer_choice = computer[randint(0,2)]
        else:
            break




user_response = False
while user_response == False:
    user_response = input("Choose Rock, Paper, or Scissors: ")


run_game = get_bot_response(user_response)

