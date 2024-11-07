def minimax(board, depth, is_maximizing):
    scores = {"X": -1, "O": 1, "Tie": 0}
    
    winner = board.check_winner()
    if winner:
        return scores[winner]
    if board.is_full():
        return scores["Tie"]
        
    if is_maximizing:
        best_score = float('-inf')
        for pos in board.get_empty_positions():
            board.cells[pos] = "O"
            score = minimax(board, depth + 1, False)
            board.cells[pos] = " "
            best_score = max(score, best_score)
        return best_score
    else:
        best_score = float('inf')
        for pos in board.get_empty_positions():
            board.cells[pos] = "X"
            score = minimax(board, depth + 1, True)
            board.cells[pos] = " "
            best_score = min(score, best_score)
        return best_score

def get_best_move(board):
    best_score = float('-inf')
    best_move = None
    
    for pos in board.get_empty_positions():
        board.cells[pos] = "O"
        score = minimax(board, 0, False)
        board.cells[pos] = " "
        if score > best_score:
            best_score = score
            best_move = pos
                
    return best_move