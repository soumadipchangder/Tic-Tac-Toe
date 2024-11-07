from flask import Flask, render_template, jsonify, request

app = Flask(__name__)

class TicTacToe:
    def __init__(self):
        self.board = [" " for _ in range(9)]
        self.current_player = "X"
        
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

game = TicTacToe()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/move', methods=['POST'])
def make_move():
    data = request.get_json()
    position = data.get('position')
    
    if not game.make_move(position):
        return jsonify({'error': 'Invalid move'}), 400
    
    return jsonify({
        'board': game.board,
        'currentPlayer': game.current_player,
        'winner': game.check_winner(),
        'isDraw': game.is_board_full(),
        'gameOver': game.check_winner() is not None or game.is_board_full()
    })

@app.route('/api/reset', methods=['POST'])
def reset_game():
    game.reset()
    return jsonify({
        'board': game.board,
        'currentPlayer': game.current_player
    })

if __name__ == '__main__':
    app.run(debug=True)