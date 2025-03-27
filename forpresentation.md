

**this is the minimax algorithm used in the 5x5 tictactoe**

previous_hashed_states = {}

def minimax(bd, depth, alpha, beta, isMaximizing):
    board_tuple = tuple(tuple(row) for row in bd)  # Convert board state to hashable type
    if board_tuple in previous_hashed_states:       #see if a state has been computed already
        return previous_hashed_states[board_tuple]

    if winner(bd, 'O'):
        return 1
    if winner(bd, 'X'):
        return -1
    if isfull(bd) or depth == 0:
        return 0
    
    if isMaximizing:
        maxEval = -float('inf')
        for i in range(5):
            for j in range(5):
                if bd[i][j] == ' ':
                    bd[i][j] = 'O'
                    eval = minimax(bd, depth - 1, alpha, beta, False)
                    bd[i][j] = ' '  # Undo move
                    maxEval = max(maxEval, eval)
                    alpha = max(alpha, eval)
                    if beta <= alpha:
                        break
        previous_hashed_states[board_tuple] = maxEval  # Store result
        return maxEval
    else:
        minEval = float('inf')
        for i in range(5):
            for j in range(5):
                if bd[i][j] == ' ':
                    bd[i][j] = 'X'
                    eval = minimax(bd, depth - 1, alpha, beta, True)
                    bd[i][j] = ' '  # Undo move
                    minEval = min(minEval, eval)
                    beta = min(beta, eval)
                    if beta <= alpha:
                        break
        previous_hashed_states[board_tuple] = minEval  # Store result
        return minEval