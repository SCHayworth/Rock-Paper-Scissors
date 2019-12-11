# Rock-Paper-Scissors
 A Rock, Paper, Scissors game

## Scope and Instructions
 Write a program that allows you to play rock, paper, scissors against the computer. Import the random module to select the computer's choice.

 *Hint:* Use if, elif, else for this program.

### Sample Run
    1 = Rock; 2 = Paper; 3 = Scissors
    Input the integer for your choice:  1

    User: Rock
    CPU: Scissors
    User wins!

## Pseudocode
### Program Logic
    START
      IMPORT random module
      INITALIZE dictionary of moves
        1 : rock
        2 : paper
        3 : scissors
      SET play game flag to True
      WHILE play game is True
        CALL main function
    END

### Function: main
    START
      SET cpu choice to a random number between 1 and 3
      PRINT "1 = Rock; 2 = Paper; 3 = Scissors"
      PRINT "Input the integer for your choice:"
      INPUT integer between 1 and 3
      INPUT user choice
      WHILE user choice is not a key in the dictionary of options
        PRINT "Please enter 1 for Rock, 2 for Paper, or 3 for Scissors: "
        INPUT user choice
      ELSE
        SET user move to the dictionary value of user choice
        PRINT user move
        SET cpu move to the dictionary value of cpu choice
        PRINT cpu choice
        CALL is_winner (args: user choice, cpu choice)
      ENDWHILE
      CALL play_again
      SET play game to return value of Play_again
    END

### Function: is_winner
    START
      PASS IN: move a, move b
      IF move a is the same as move b
        PRINT "Tie Game!"
      ELSE IF move a = 1
        IF move b = 2
          PRINT "CPU wins!"
        ELSE
          PRINT "You win!"
        ENDIF
      ELSE IF move a = 2
        IF move b = 1
          PRINT "You win!"
        ELSE
          PRINT "CPU wins!"
        ENDIF
      ELSE
        IF move b = 1
          PRINT "CPU wins!"
        ELSE
          PRINT "You win!"
        ENDIF
      ENDIF
    END

### Function: play_again
    START
      PASS IN: nothing
      PRINT "Would you like to play again (y/n)?"
      INPUT answer
      WHILE answer is not Y, y, N, or n
        PRINT "Please answer Y or N."
        INPUT answer
      ENDWHILE
      IF answer is Y or y
        return True
      ELSE
        return False
      ENDIF
    ENDI
