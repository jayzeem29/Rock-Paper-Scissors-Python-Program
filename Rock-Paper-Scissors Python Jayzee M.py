# Published by Jayzee Monserate on May 25, 2025
import random 
import sys

choice_list = ('rock', 'paper', 'scissors') # Immutable (cannot be changed)
# choice_attr checks for which option beats another option
choice_attr = {'rock': 'scissors', # Rock beats scissors
'paper': 'rock', # Paper beats rock
'scissors': 'paper'} # Scissors beats paper

def game_interface():
    print ('\n ~~~~~ Rock - Paper - Scissors Python Program by Jayzee Monserate ~~~~~ ')
    print ("To reset both you and the bot's score, type 'clear' in the input prompt. ")
    print ("If you want to stop running this program at any time, type 'exit' in the input prompt. \n")
    print ("Otherwise, type 'rock', 'paper', or 'scissors' in the input prompt. \n")

def game_code():
    user_score = 0 
    bot_score = 0 
    # User and bot scores outside the loop prevents the variables from resetting in every iteration
    # (instead resetting ONLY if user inputs "clear")
    game_interface() # Prints the four lines in the game_interface() function
    while True: # Indefinite loop
        user_input = input("Enter your input here: ").strip().lower() 
        if user_input == 'clear': # Resets the user and the bot's points to 0
            user_score = 0 
            bot_score = 0 
            print ("Your points and the bot's point have been reset to 0.")
        elif user_input == 'exit':
            sys.exit() # Stops running the program
        elif user_input not in choice_list: # Occurs if user input is not "rock", "paper", or "scissors"
            print ("Invalid input: Please type a valid input!")
        else:
            bot_input = random.choice(choice_list)
            if user_input == bot_input:
                print (f"Both you and the bot have chosen {user_input}!")
                continue # Goes back to the user input
            else:
                print (f"You have chosen {user_input}, while the bot chose {bot_input}.")
            # Line below checks for the user's input and returns which value the input beats
            if bot_input == choice_attr.get(user_input):
                # .get(user_input) returns the value in the choice_attr dictionary based on the key (the user input)
                print("You win!")
                user_score += 1 # Increases user score by 1
            else:
                print("The bot wins!")
                bot_score += 1 # Increases bot score by 1
            print (f"You have {user_score} points, while the bot has {bot_score} points.") 
            # Goes back to the user input

while True: # If an exception is raised, the program still runs
    try:
        game_code() # Loads the game_code() function from above
    except Exception as e:
        print (f"Exception occured: {e}") # In case an Exception is raised unexpectedly
    except KeyboardInterrupt:
        print ("Exception occured: KeyboardInterrupt") # If KeyboardInterrupt occurs