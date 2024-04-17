# -*- coding: utf-8 -*-
"""
Created on Sat Apr  6 12:32:35 2024

@author: gus_a
"""



"""
Python Web Development Techdegree
Project 1 - Number Guessing Game
"""



import random # importing random library


def start_game(): # start_game function
    print("Welcome player! ")
    
    #high_score = 0
    
    #if high_score != 0:
    #    print(f"The High score is {high_score} ")
    
    random_number = random.randint(0,10)    # generating random number
    user_response = int()                    # user_response variable, set to None so we can run the while loop
    responses = []                          # responses variable, to store all attempts
    
    
    while True: # the while loop will continue until we stop it with a "break" keyword
        
        
        
        try:
            user_response = int(input("Guess what number it is, between 0 and 10 "))
            if user_response < 0 or user_response > 10:
                print("You entered a number out of range ")
            
        except ValueError:
            print(" Please only enter a valid number between 0 and 10")
            continue
        
        
        
                
        
        
        responses.append(user_response) # we store each user_response in responses 
        
        # wether the user_response value is greater or lower than the random_number, we 
        # make the user aware of it
        if user_response < random_number: 
            print("It's higher")
            
            
        elif user_response > random_number:
            print("It's lower")
            
        
        
        elif user_response == random_number:
            attempts = len(responses) # we count how many attempts it took our player to get
                                      # to the right answer
            
            
            # when the user guesses correctly the random_number, we let him/her know and finish the game
            print(f"""\nGot it in {attempts} attempts! """)
            
            play_again = input(" Would you like to play again? (y)es / (n)o ")
            if play_again.lower() == "n":
                
                print("the game is over, see ya next time! ")
                
                break
            else:
                
                responses.clear()                       # clearing the previous responses
                
                random_number = random.randint(0,10)    # generating random number
                
                #if attempts < high_score or high_score == 0:
                #    high_score = attempts
                
                continue
            
       
    

# Kick off the program by calling the start_game function.
start_game()


"""
Provide Out-Of-Range Feedback
As a player, my guess should be within the number range. 
If my guess is outside the guessing range, I should be told to try again. 
For example, if the range is 1-10 and the player enters 12, 
they should be informed that this number is outside the range.
/
not sure if i am correct




Option to Play Again Prompt
As a player, after I guess correctly and win, 
I should be prompted if I would like to play again.
/


Display a High Score
As a player, at the start of each game, 
I should be shown the current high score (least amount of guess attempts) 
so that I know what I am supposed to beat.
-------


Generate a New Winning Number
Every time a player decides to play again, 
the random number to guess is updated so that players 
are guessing something new each time.
/


"""





