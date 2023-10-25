import sys
from minimax_A20463413 import *
from state_A20463413 import State

# tic-tac-toe board representation
#
#  1 | 2 | 3
# ---+---+---
#  4 | 5 | 6
# ---+---+---
#  7 | 8 | 9

# Check for errors in initial command line inputs
if len(sys.argv) != 4 :
    sys.exit("ERROR: Not enough/too many/illegal input arguments.")

algo = int(sys.argv[1]) #Convert to int for convenience
first = sys.argv[2].upper() #Convert to uppercase for convenience
mode = int(sys.argv[3]) #Convert to int for convenience

# Used later to display the intro prompt to the player
algoText = ""
modeText = ""


if first != "O" and first != "X" :
    sys.exit("ERROR: Not enough/too many/illegal input arguments.")

if algo == 1 :
    algoText = "MiniMax"
elif algo == 2 :
    algoText = "MiniMax with alpha-beta pruning"
else :
    sys.exit("ERROR: Not enough/too many/illegal input arguments.")

if mode == 1 :
    modeText = "Human (X) vs. Computer (O)"
elif mode == 2 :
    modeText = "Computer vs. Computer"
else :
    sys.exit("ERROR: Not enough/too many/illegal input arguments.")


def main() :
    
    # Uses the Board class to make an empty board object
    board = State()

    # Print intro display
    print("Pietrzyk, Piotr, A20463413 solution:\nAlgorithm: " + algoText + "\nFirst: " + first + "\nMode: " + modeText)

    # The player variable will be used to determine which player's turn it is
    player = first

    # First show the empty board
    board.show_board()

    # Play the game
    while True :

        if mode == 1 and player == "X" : #It is the human's turn

            # The next while loop will deal with misinputs and re-prompting the player
            misinput = True
            cell = -1
            # Handles re-prompting user in case of misinput
            # First assume that a misinput is True and try to disprove from there
            while misinput :
                cellString = input(show_player_prompt(board))

                # First handle the case where the input value is a non-number
                if not cellString.isnumeric() :
                    continue
                else :
                    cell = int(cellString)

                # Then handle the cases where the input value is a number
                if cell == 0:
                    exit()
                elif cell < 1 or cell > 9 :
                    continue
                elif board.get_cell(cell - 1) != " " :
                    continue
                else :
                    misinput = False
                    
            # Player's turn is actually taken here
            board.result(player, cell-1)
        else :
            take_turn(board, player, algo) # It is the computer's turn
            
        # Show the board after a turn is taken
        board.show_board()

        checkWin = board.utility(player)
        # Check for winner
        if checkWin == 2 :
            print(player + " WON")
            break
        # Check for tie
        if checkWin == 0 :
            print("TIE")
            break

        # Switch to next player
        if player == "X" :
            player = "O"
        else :
            player = "X"


# Use the board array to build the prompt that will display to the human player a list of possible moves
# Tells the function that brd (the board object) is of type State
def show_player_prompt(brd : State) :
    prompt = "X's move. What is your move (possible moves at the moment are: <"
    
    for x in brd.actions() :
        prompt = prompt + str(x) + ", "

    # Remove the trailing ', ' that would otherwise appear
    prompt = prompt[0:len(prompt)-2]

    prompt = prompt + "> | enter 0 to exit the game)? "
    return prompt


# take_turn() first checks which algorithm to use then calls the appropriate minimax function, passing it the board state and the player whose turn it is
# Tells the function that brd (the board object) is of type State
def take_turn(brd : State, plyr, alg) :

    if alg == 1 :
        cell, nodes = minimax(brd, plyr)
    elif alg == 2 :
        cell, nodes = minimax_ab(brd, plyr)

    # Display the resulting move the player played and display how many nodes were generated
    brd.result(plyr, cell)
    print(plyr + "'s selected move: " + str(cell+1) + ". Number of search tree nodes generated: " + str(nodes))
    return brd


if __name__ == "__main__" :
    main()