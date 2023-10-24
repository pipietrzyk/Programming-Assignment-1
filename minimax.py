from state import State

# Tells the function that brd is of type State
#TODO: Try passing in board as a list instead of an object
def minimax(brd : State, plyr) :
    utility, cell, nodes = max_value(brd, plyr, 1)
    return cell, nodes

# TODO: player might need to be opposite from MIN
# Tells the function that brd is of type State
def max_value(brd : State, plyr, nodes) :
    nodes = nodes + 1

    if plyr == "X" :
        enemy = "O"
    else :
        enemy = "X"

    if brd.is_terminal() :
        return (brd.utility(plyr), 0, nodes)
    u = -10
    for a in brd.actions() :
        newBrd = State(brd.get_board())
        newBrd.result(plyr, a-1)
        u2, a2, nodes = min_value(newBrd, enemy, nodes)
        if u2 > u :
            u, move = u2, a-1
    return u, move, nodes

    # if game.IS-TERMINAL(board) then return (game.UTILITY(board, player), null)
    # v = -10 (v = value aka utility)
    # for each a in game.ACTIONS(board) do
    #   v2, a2 = MIN-VALUE(game, game.RESULT(state, a))
    #   if v2 > v then
    #     v, move = v2, a
    # return v, move

# TODO: player might need to be opposite from MAX
# Tells the function that brd is of type State
def min_value(brd : State, plyr, nodes) :
    nodes = nodes + 1

    if plyr == "X" :
        enemy = "O"
    else :
        enemy = "X"

    if brd.is_terminal() :
        return (brd.utility(enemy), 0, nodes)
    u = 10
    for a in brd.actions() :
        newBrd = State(brd.get_board())
        newBrd.result(plyr, a-1)
        u2, a2, nodes = max_value(newBrd, enemy, nodes)
        if u2 < u :
            u, move = u2, a-1
    return u, move, nodes

    # if game.IS-TERMINAL(board) then return (game.UTILITY(board, player), null)
    # v = 10
    # for each a in game.ACTIONS(board) do
    #   v2, a2 = MAX-VALUE(game, game.RESULT(state, a))
    # if v2 < v then
    #   v, move = v2, a
    # return v, move



def minimax_ab(brd : State, plyr) :
    utility, cell, nodes = max_value_ab(brd, plyr, -10, 10, 1)
    return cell, nodes

def max_value_ab(brd : State, plyr, alpha, beta, nodes) :
    nodes = nodes + 1

    if plyr == "X" :
        enemy = "O"
    else :
        enemy = "X"

    if brd.is_terminal() :
        return (brd.utility(plyr), 0, nodes)
    u = -10
    for a in brd.actions() :
        newBrd = State(brd.get_board())
        newBrd.result(plyr, a-1)
        u2, a2, nodes = min_value_ab(newBrd, enemy, alpha, beta, nodes)
        if u2 > u :
            u, move = u2, a-1
            alpha = max(a, u)
        if u >= beta :
            return u, move, nodes
    return u, move, nodes


def min_value_ab(brd : State, plyr, alpha, beta, nodes) :
    nodes = nodes + 1

    if plyr == "X" :
        enemy = "O"
    else :
        enemy = "X"

    if brd.is_terminal() :
        return (brd.utility(enemy), 0, nodes)
    u = 10
    for a in brd.actions() :
        newBrd = State(brd.get_board())
        newBrd.result(plyr, a-1)
        u2, a2, nodes = max_value_ab(newBrd, enemy, alpha, beta, nodes)
        if u2 < u :
            u, move = u2, a-1
            beta = min(beta, u)
        if u <= alpha :
            return u, move, nodes
    return u, move, nodes

