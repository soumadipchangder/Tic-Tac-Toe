class Board:
    def __init__(self):
        self.cells = [" " for _ in range(9)]

    def make_move(self, position, player):
        if self.cells[position] == " ":
            self.cells[position] = player
            return True
        return False

    def is_full(self):
        return " " not in self.cells

    def get_empty_positions(self):
        return [i for i, cell in enumerate(self.cells) if cell == " "]

    def check_winner(self):
        # Check rows
        for i in range(0, 9, 3):
            if self.cells[i] == self.cells[i+1] == self.cells[i+2] != " ":
                return self.cells[i]

        # Check columns
        for i in range(3):
            if self.cells[i] == self.cells[i+3] == self.cells[i+6] != " ":
                return self.cells[i]

        # Check diagonals
        if self.cells[0] == self.cells[4] == self.cells[8] != " ":
            return self.cells[0]
        if self.cells[2] == self.cells[4] == self.cells[6] != " ":
            return self.cells[2]

        return None

    def display(self):
        print("\n=== TIC TAC TOE ===\n")
        for i in range(0, 9, 3):
            print(f" {self.cells[i]} | {self.cells[i+1]} | {self.cells[i+2]} ")
            if i < 6:
                print("-----------")
        print()