class Game :
    def __init__(self, player) :
        self.player = player
        self.board = [" ", " ", " ",
                      " ", " ", " ",
                      " ", " ", " "]

    # Determines whose turn it is to move
    def ToMove(self, board) :
        countX = 0
        countO = 0

        for x in board :
            if x == "X" :
                countX = countX + 1
            else :
                countO = countO + 1

        if countX > countO :
            self.player = "O"
            return self.player
        else :
            self.player = "X"
            return self.player

    # Determines whether the game is in a terminal state (win/tie) using python list comprehension
    def IsTerminal(self, board) :
        return any(plyr == board[a] == board[b] == board[c]
                   for plyr in ["X", "O"]
                   for a, b, c in
                   [(0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6)]) \
               or not (" " in board)


    # Determine utility (1, 0, -1) for a win/loss/tie
    # Assumes the board passed through is in a terminal state
    def Utility(self, board, player) :
        void

    # Returns a list of possible moves (1-9)
    def Actions(self, board) :
        actions = []

        for x in range(len(board)) :
            if board[x] == " " :
                actions.append(x+1)

        return actions

    def Result(self, board, action) :
        void

