class State :
    # Represents the available spaces on the tic-tac-toe board (starts empty)
    # " " means the space is empty
    # "X" means the space is filled with an X
    # "O" means the space is filled with an O
    # By default it generates an empty board
    def __init__(self, board = [" ", " ", " ",
                                " ", " ", " ",
                                " ", " ", " "]) :
        self.board = board

    # Use the board list to build and show a tic-tac-toe board to the player
    def show_board(self) :
        print(" " + self.board[0] + " " + "|" + " " + self.board[1] + " " + "|" + " " + self.board[2] + " \n" +
              "---+---+---\n" +
              " " + self.board[3] + " " + "|" + " " + self.board[4] + " " + "|" + " " + self.board[5] + " \n" +
              "---+---+---\n" +
              " " + self.board[6] + " " + "|" + " " + self.board[7] + " " + "|" + " " + self.board[8] + " ")
        
    # Get the value of a specific cell
    def get_cell(self, cell) :
        return self.board[cell]
    
    # Return a copy of the board list 
    # Essentially passes the board list by value instead of by reference, which is important in the min_value and max_value functions
    def get_board(self) :
        return (self.board).copy()

    # List all of the available actions as a list (1-9 instead of 0-8)
    def actions(self) :
        actions = []
        for x in range(len(self.board)) :
            if self.board[x] == " " :
                actions.append(x+1)
        return actions
    
    # Perform an action and update the board accordingly
    def result(self, player, action) :
        self.board[action] = player
    
    # Is the game in a terminal state (true/false)?
    # Uses python list comprehension
    def is_terminal(self) :
        return any(player == self.board[a] == self.board[b] == self.board[c]
                   for player in ["X", "O"]
                   for a, b, c in
                   [(0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6)]) \
               or not (" " in self.board)
    
    # Determine the utility of a board state for a given player
    # Uses list comprehension similarly to is_terminal()
    def utility(self, player) :
        if player == "X" :
            enemy = "O"
        else :
            enemy = "X"

        if any( player == self.board[a] == self.board[b] == self.board[c]
                for a,b,c in [(0,1,2),(3,4,5),(6,7,8),(0,3,6),(1,4,7),(2,5,8),(0,4,8),(2,4,6)] ) :
            return 2
        elif any( enemy == self.board[a] == self.board[b] == self.board[c]
                for a,b,c in [(0,1,2),(3,4,5),(6,7,8),(0,3,6),(1,4,7),(2,5,8),(0,4,8),(2,4,6)] ) :
            return -2
        elif not (" " in self.board) :
            return 0
        else :
            return -1
                    