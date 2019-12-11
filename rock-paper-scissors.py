# 5-4 Automobile Costs
# Shaun Hayworth
# CIS 2
# 12-10-2019
# Source code and revision history are available at
# https://github.com/SCHayworth/Rock-Paper-Scissors

# This program plays a game of Rock, Paper, Scissors (RPS) against the computer,
# and announces the winner.

# Import modules.
import random

# Create a constant dictionary with each option as a key to an RPS move.
MOVE_OPTIONS = { 1 : 'Rock',
                 2 : 'Paper',
                 3 : 'Scissors'}

# Initialize constant tuple of valid move choices.
VALID_MOVES = (1, 2, 3)


# Define the functions used in the program
def main():
    '''This is the mainline program logic loop.'''
    # Choose a random move option for the CPU.
    cpu_choice = random.randint(1,3)

    # Print the move options and get a valid selection from the user.
    # If the selection is not valid, ask again until it is.
    print('1 = Rock; 2 = Paper; 3 = Scissors')
    user_choice = input('Input the integer for your choice: ')
    while user_choice not in VALID_MOVES:
        user_choice = input('Please enter 1 for Rock, 2 for Paper, or 3 for Scissors: ')
    else:
        # Retrieve RPS move values from the MOVE_OPTIONS dictionary and print them.
        user_move = MOVE_OPTIONS[user_choice]
        cpu_move = MOVE_OPTIONS[cpu_choice]
        print(f'User: {user_move}')
        print(f'CPU: {cpu_move}')

        # Call the is_winner function to see if the player wins and print the
        # result of the game.
        if user_choice == cpu_choice:
            print('Tie game!')
        else:
            player_wins = is_winner(user_choice, cpu_choice)
            if player_wins == True:
                print('You win!')
            else:
                print('CPU wins!')


def is_winner(move_a, move_b):
    '''This function determines if the player wins at Rock, Paper, Scissors'''
    # Compare move_a and move_b, and print whether the user or the CPU wins the
    # game.
    if move_a == 1:
        if move_b == 2:
            return False
        else:
            return True
    elif move_a == 2:
        if move_b == 1:
            return True
        else:
            return False
    else:
        if move_b == 1:
            return False
        else:
            return True


def play_again(prompt, reminder='Please answer y/n.'):
    '''Asks the user if they would like to run the program again, and returns
       False if they do not.'''
    while True:
        ok = input(prompt)
        if ok in ('Y', 'y'):
            return True
        if ok in ('n', 'N'):
            return False
        print(reminder)


# Loop the main() function as long as the run_program condition is True.
run_program = True
while run_program == True:
    main()
    run_program = play_again()
