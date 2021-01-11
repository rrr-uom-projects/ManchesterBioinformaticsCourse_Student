# With this code you will be able to make a 2 player noughts and crosses game

import numpy as np

## These two lines are part of the dark arts. See the function called clearScreen() for why we need them
import colorama
colorama.init()


def displayBoard(state):
    """
    This function should display the board. The board is a 3x3 grid. We use a letter-number system to identify squares in the grid.
    """
    decodedState = ["X" if s == 1 else "O" if s == -1 else "-" for s in state]
    print("""|  #  |  A  |  B  |  C  |  #  |
|  1  |  {0}  |  {1}  |  {2}  |  1  |
|  2  |  {3}  |  {4}  |  {5}  |  2  |
|  3  |  {6}  |  {7}  |  {8}  |  3  |
|  #  |  A  |  B  |  C  |  #  |""".format(*decodedState))  ## Note the use of formatted multi-line strings!

## Also - the *decodedStrings is just a way to unpack the list without having to do decodedStrings[1], decodedStrigns[2]...

def clearScreen():
    """
    This is dark magic.
    When you have colorama imported, and have called colorama.init(), this sequence will clear the console output whenever you call the function.
    It makes the board display look pretty.
    """
    print("\033[2J\033[1;1f")


def userSelection(player, state):
    """
	This function takes input from the players in the form of a two character string. (e.g. A1).
	It needs to make sure a selected square isn't already taken, and it should update the game state when an allowed square is selected.
	The function should also check the user hasn't entered something stupid (like two numbers, all letters, letters that make no sense etc...)
	From here we return a modified state, and the selected index (so recursion will work)
	"""
    selected = raw_input("Player {0}, select a square (eg A1):  ".format(player + 1))
    if selected[0].upper() == "A":
        pass
    #1. Delete pass above and select the column here.
    #2. You should also provide code for each of the columns and to select the row.

    #3.Set the index based on the selected column and row
    #4.Check if the selected row and column have already been taken and print a message and call user selection again.

    ## use 0 to represent an unfilled square, 1 for player 1, -1 for player 2
    if player == 0:
        state[index] = 1
    #5. add code for the second player
    return index, state


def checkGameStatus(state):
    """
	This function checks to see if anyone has won yet. To do this, it tests the 8 possible winning combinations.
	To make it a bit easier, I hardcoded the possible win scenarios. It would be good to generate them based on the size of the grid.
	We must also check to see if there are any moves left.
	This function returns a boolean which will be true whenever the game can continue
	"""
    # Hard code this bit
    winningIndices = [(0, 1, 2),
                      (3, 4, 5),
                      (6, 7, 8)
                      #6. add the rest of the winning conditions
                      ]

    gameContinues = True
    for wI in winningIndices:
        if np.all(np.take(state, wI) == 1):
            gameContinues = False
            print("Player 1 wins!")
        #7. Add a win condition for player 2.
    #8. Check if all of the moves have been taken.
        gameContinues = False
        print("Out of Moves!")
    return gameContinues


def main():
    player = 0  ## Use zero based player numbering - add 1 to make it human friendly
    state = np.zeros(9)  ## the state of the game - will be updated after every turn
    clearScreen()  ## get the screen ready...
    while True:  ## This is an infinite loop - make sure we escape it somewhere!
        displayBoard(state)  ## Show the current game status
        index, state = userSelection(player, state)  ## User selects square, update state...
        if not checkGameStatus(state):
            displayBoard(state)  ## Show the current game status
            break  ## If the game is won, or out of moves, escape from the infinite loop
        player = 1# 9. complete this code ## Add 1 to player number. Modulo division by 2 means we will always be either 0 or 1

        clearScreen()  ## Clear screen ready for next update


if __name__ == "__main__":
    main()
