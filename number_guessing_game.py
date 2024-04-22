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
from sys import exit # import exit so we may use it later


high_score = 0

def start_game(): # start_game function
    print("Welcome player! ")
    
    global high_score
    
    if high_score != 0:
        print(f"The High score is {high_score} ") # print high score if we have one
    
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
                exit(0) # function to terminate the program
            
            else:
                
                responses.clear()                       # clearing the previous responses
                
                random_number = random.randint(0,10)    # generating random number
                
                if attempts < high_score or high_score == 0: # update the high score, if it hits a new one
                    high_score = attempts
                
                start_game()
            
       
    

# Kick off the program by calling the start_game function.
start_game()


"""
Code from websites:

https://www.freecodecamp.org/news/python-exit-how-to-use-an-exit-function-in-python-to-stop-a-program/
https://stackoverflow.com/questions/45066518/nameerror-name-exit-is-not-defined

"""


