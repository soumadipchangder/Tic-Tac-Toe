class TicTacToe:
    def __init__(self):
        self.reset()

    def reset(self):
        self.board = [" " for _ in range(9)]
        self.current_player = "X"

    def make_move(self, position):
        if 0 <= position < 9 and self.board[position] == " ":
            self.board[position] = self.current_player
            self.current_player = "O" if self.current_player == "X" else "X"
            return True
        return False

    def check_winner(self):
        # Check rows
        for i in range(0, 9, 3):
            if self.board[i] == self.board[i+1] == self.board[i+2] != " ":
                return self.board[i]

        # Check columns
        for i in range(3):
            if self.board[i] == self.board[i+3] == self.board[i+6] != " ":
                return self.board[i]

        # Check diagonals
        if self.board[0] == self.board[4] == self.board[8] != " ":
            return self.board[0]
        if self.board[2] == self.board[4] == self.board[6] != " ":
            return self.board[2]

        return None

    def is_board_full(self):
        return " " not in self.board

def get_best_move(board, player):
    empty_cells = [i for i, cell in enumerate(board) if cell == " "]
    
    def minimax(board, depth, is_maximizing):
        scores = {"X": -1, "O": 1, "Tie": 0}
        
        winner = check_winner(board)
        if winner:
            return scores[winner]
        if " " not in board:
            return scores["Tie"]
            
        if is_maximizing:
            best_score = float('-inf')
            for pos in [i for i, cell in enumerate(board) if cell == " "]:
                board[pos] = "O"
                score = minimax(board, depth + 1, False)
                board[pos] = " "
                best_score = max(score, best_score)
            return best_score
        else:
            best_score = float('inf')
            for pos in [i for i, cell in enumerate(board) if cell == " "]:
                board[pos] = "X"
                score = minimax(board, depth + 1, True)
                board[pos] = " "
                best_score = min(score, best_score)
            return best_score

    def check_winner(board):
        # Check rows
        for i in range(0, 9, 3):
            if board[i] == board[i+1] == board[i+2] != " ":
                return board[i]
        # Check columns
        for i in range(3):
            if board[i] == board[i+3] == board[i+6] != " ":
                return board[i]
        # Check diagonals
        if board[0] == board[4] == board[8] != " ":
            return board[0]
        if board[2] == board[4] == board[6] != " ":
            return board[2]
        return None

    best_score = float('-inf')
    best_move = empty_cells[0]
    
    for pos in empty_cells:
        board[pos] = "O"
        score = minimax(board, 0, False)
        board[pos] = " "
        if score > best_score:
            best_score = score
            best_move = pos
                
    return best_move