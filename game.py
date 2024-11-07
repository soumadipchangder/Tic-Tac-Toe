from board import Board
from game_state import GameState
from ai_player import get_best_move

def get_valid_input(prompt, valid_range=None):
    while True:
        try:
            user_input = input(prompt)
            if user_input.lower() in ['q', 'quit', 'exit']:
                return None
            value = int(user_input)
            if valid_range is None or value in valid_range:
                return value
            print(f"Please enter a number within the valid range!")
        except ValueError:
            print("Please enter a valid number!")
        except (EOFError, KeyboardInterrupt):
            print("\nGame terminated by user.")
            return None

def replay_game(moves):
    print("\n=== GAME REPLAY ===\n")
    replay_board = Board()
    
    for position, player in moves:
        replay_board.cells[position] = player
        replay_board.display()
        print("\n" + "="*20 + "\n")

def play_game(game_state):
    board = Board()
    current_player = "X"
    moves = []
    
    print("\nPosition reference:")
    print("0 | 1 | 2")
    print("---------")
    print("3 | 4 | 5")
    print("---------")
    print("6 | 7 | 8")
    
    while True:
        board.display()
        
        if game_state.vs_ai and current_player == "O":
            print("\nAI is thinking...")
            position = get_best_move(board)
        else:
            position = get_valid_input(f"\nPlayer {current_player}'s turn (0-8): ", range(9))
            if position is None:
                return False

        if not board.make_move(position, current_player):
            print("That position is already taken!")
            continue

        moves.append((position, current_player))
        
        winner = board.check_winner()
        if winner:
            board.display()
            print(f"\nPlayer {winner} wins!")
            game_state.update_score(winner)
            game_state.save_game(moves)
            return True

        if board.is_full():
            board.display()
            print("\nIt's a tie!")
            game_state.update_score(None)
            game_state.save_game(moves)
            return True
            
        current_player = "O" if current_player == "X" else "X"

def main():
    game_state = GameState()
    
    while True:
        print("\n=== TIC TAC TOE ===")
        print("1. Play vs Human")
        print("2. Play vs AI")
        print("3. View Scores")
        print("4. Watch Last Game Replay")
        print("5. Exit")
        
        choice = get_valid_input("\nEnter your choice (1-5): ", range(1, 6))
        if choice is None or choice == 5:
            print("\nThanks for playing!")
            break
        
        if choice == 1:
            game_state.vs_ai = False
            if not play_game(game_state):
                break
        elif choice == 2:
            game_state.vs_ai = True
            if not play_game(game_state):
                break
        elif choice == 3:
            game_state.display_scores()
        elif choice == 4:
            if game_state.game_history:
                replay_game(game_state.game_history[-1])
            else:
                print("\nNo games to replay!")
        
        input("\nPress Enter to continue...")

if __name__ == "__main__":
    try:
        main()
    except (KeyboardInterrupt, EOFError):
        print("\nGame terminated by user.")
    except Exception as e:
        print(f"\nAn error occurred: {e}")
        print("Game terminated.")