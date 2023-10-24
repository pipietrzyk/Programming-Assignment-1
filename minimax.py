from state import State

# Tells the function that brd is of type State
#TODO: Try passing in board as a list instead of an object
def minimax(brd : State, plyr) :
    utility, cell = max_value(brd, plyr)
    return utility, cell

# TODO: player might need to be opposite from MIN
# Tells the function that brd is of type State
def max_value(brd : State, plyr) :
    if plyr == "X" :
        enemy = "O"
    else :
        enemy = "X"

    if brd.is_terminal() :
        return (brd.utility(plyr), 0)
    u = -10
    for a in brd.actions() :
        newBrd = State(brd.get_board())
        newBrd.result(plyr, a-1)
        u2, a2 = min_value(newBrd, plyr)
        if u2 > u :
            u, move = u2, a-1
    return (u, move)

    # if game.IS-TERMINAL(board) then return (game.UTILITY(board, player), null)
    # v = -10 (v = value aka utility)
    # for each a in game.ACTIONS(board) do
    #   v2, a2 = MIN-VALUE(game, game.RESULT(state, a))
    #   if v2 > v then
    #     v, move = v2, a
    # return v, move

# TODO: player might need to be opposite from MAX
# Tells the function that brd is of type State
def min_value(brd : State, plyr) :
    if plyr == "X" :
        enemy = "O"
    else :
        enemy = "X"

    if brd.is_terminal() :
        return (brd.utility(plyr), 0)
    u = 10
    for a in brd.actions() :
        newBrd = State(brd.get_board())
        newBrd.result(plyr, a-1)
        u2, a2 = max_value(newBrd, plyr)
        if u2 < u :
            u, move = u2, a-1
    return (u, move)

    # if game.IS-TERMINAL(board) then return (game.UTILITY(board, player), null)
    # v = 10
    # for each a in game.ACTIONS(board) do
    #   v2, a2 = MAX-VALUE(game, game.RESULT(state, a))
    # if v2 < v then
    #   v, move = v2, a
    # return v, move



def minimax_ab(brd, plyr) :
    cell, nodes = 0
    return (cell, nodes)

def max_value_ab(brd) :
    pass

def min_value_ab(brd) :
    pass

