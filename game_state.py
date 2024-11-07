class GameState:
    def __init__(self):
        self.scores = {"X": 0, "O": 0, "Tie": 0}
        self.game_history = []
        self.vs_ai = False
        
    def update_score(self, winner):
        if winner:
            self.scores[winner] += 1
        else:
            self.scores["Tie"] += 1
            
    def save_game(self, moves):
        self.game_history.append(moves)
        
    def display_scores(self):
        print("\n=== SCORES ===")
        print(f"Player X: {self.scores['X']}")
        print(f"Player O: {self.scores['O']}")
        print(f"Ties: {self.scores['Tie']}")
        print("=============")