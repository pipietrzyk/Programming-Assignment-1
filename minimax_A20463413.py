from state_A20463413 import State

# Tells the function that brd is of type State
# Utility is not needed by the actual game in main() so it is not returned
# brd = the game board, plyr = what player is taking their turn (X/O)
def minimax(brd : State, plyr) :
    utility, cell, nodes = max_value(brd, plyr, 1) # Pass in the first root node here as well
    return cell, nodes


# Tells the function that brd is of type State
# brd = the game board, plyr = what player is taking their turn (X/O), nodes = how many nodes are generated
def max_value(brd : State, plyr, nodes) :
    nodes = nodes + 1

    # Since there is no mechanism to automatically detect whose turn it is based on board state, it is done here instead
    if plyr == "X" :
        enemy = "O"
    else :
        enemy = "X"

    # Follows the pseudocode pretty closely
    if brd.is_terminal() :
        return (brd.utility(plyr), 0, nodes)
    u = -10
    # For each possible action, create a new board object and simulate playing that action and then call min_value()
    for a in brd.actions() :
        newBrd = State(brd.get_board())
        newBrd.result(plyr, a-1)
        u2, a2, nodes = min_value(newBrd, enemy, nodes)
        if u2 > u :
            u, move = u2, a-1
    return u, move, nodes


# Tells the function that brd is of type State
# brd = the game board, plyr = what player is taking their turn (X/O), nodes = how many nodes are generated
def min_value(brd : State, plyr, nodes) :
    nodes = nodes + 1

    # Since there is no mechanism to automatically detect whose turn it is based on board state, it is done here instead
    if plyr == "X" :
        enemy = "O"
    else :
        enemy = "X"

    # Follows the pseudocode pretty closely
    if brd.is_terminal() :
        return (brd.utility(enemy), 0, nodes)
    u = 10
    # For each possible action, create a new board object and simulate playing that action and then call max_value()
    for a in brd.actions() :
        newBrd = State(brd.get_board())
        newBrd.result(plyr, a-1)
        u2, a2, nodes = max_value(newBrd, enemy, nodes)
        if u2 < u :
            u, move = u2, a-1
    return u, move, nodes


# Tells the function that brd is of type State
# Utility is not needed by the actual game in main() so it is not returned
# brd = the game board, plyr = what player is taking their turn (X/O)
def minimax_ab(brd : State, plyr) :
    utility, cell, nodes = max_value_ab(brd, plyr, -10, 10, 1) # Pass in alpha, beta as -10, 10 instead of infinities, pass in the first root node here as well
    return cell, nodes


# Tells the function that brd is of type State
# brd = the game board, plyr = what player is taking their turn (X/O), 
# alpha and beta = alpha and beta values for ab pruning, nodes = how many nodes are generated
def max_value_ab(brd : State, plyr, alpha, beta, nodes) :
    nodes = nodes + 1

    # Since there is no mechanism to automatically detect whose turn it is based on board state, it is done here instead
    if plyr == "X" :
        enemy = "O"
    else :
        enemy = "X"

    # Follows the pseudocode pretty closely
    if brd.is_terminal() :
        return (brd.utility(plyr), 0, nodes)
    u = -10
    # For each possible action, create a new board object and simulate playing that action and then call max_value()
    for a in brd.actions() :
        newBrd = State(brd.get_board())
        newBrd.result(plyr, a-1)
        u2, a2, nodes = min_value_ab(newBrd, enemy, alpha, beta, nodes)
        if u2 > u :
            u, move = u2, a-1
            alpha = max(alpha, u)
        if u >= beta :
            return u, move, nodes
    return u, move, nodes


# Tells the function that brd is of type State
# brd = the game board, plyr = what player is taking their turn (X/O), 
# alpha and beta = alpha and beta values for ab pruning, nodes = how many nodes are generated
def min_value_ab(brd : State, plyr, alpha, beta, nodes) :
    nodes = nodes + 1

    # Since there is no mechanism to automatically detect whose turn it is based on board state, it is done here instead
    if plyr == "X" :
        enemy = "O"
    else :
        enemy = "X"

    # Follows the pseudocode pretty closely
    if brd.is_terminal() :
        return (brd.utility(enemy), 0, nodes)
    u = 10
    # For each possible action, create a new board object and simulate playing that action and then call max_value()
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

