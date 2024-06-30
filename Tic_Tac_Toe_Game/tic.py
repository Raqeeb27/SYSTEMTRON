import random

def print_board(board):
    print("---------")
    for row in board:
        print("|".join(row))
        print("---------")

def check_winner(board, player):
    # Check rows
    for row in board:
        if all(s == player for s in row):
            return True
    
    # Check columns
    for col in range(3):
        if all(board[row][col] == player for row in range(3)):
            return True
    
    # Check diagonals
    if all(board[i][i] == player for i in range(3)) or all(board[i][2-i] == player for i in range(3)):
        return True
    
    return False

def is_full(board):
    return all(all(cell != " " for cell in row) for row in board)

def get_available_moves(board):
    return [(r, c) for r in range(3) for c in range(3) if board[r][c] == " "]

def computer_move(board):
    available_moves = get_available_moves(board)
    return random.choice(available_moves)

def two_player_mode():
    board = [[" " for _ in range(3)] for _ in range(3)]
    current_player = "X"
    
    while True:
        print_board(board)
        row = int(input(f"Player {current_player}, enter the row (0, 1, or 2): "))
        col = int(input(f"Player {current_player}, enter the column (0, 1, or 2): "))
        
        if board[row][col] != " ":
            print("Cell already taken, try again.")
            continue
        
        board[row][col] = current_player
        
        if check_winner(board, current_player):
            print_board(board)
            print(f"Player {current_player} wins!")
            break
        
        if is_full(board):
            print_board(board)
            print("It's a tie!")
            break
        
        current_player = "O" if current_player == "X" else "X"

def single_player_mode():
    board = [[" " for _ in range(3)] for _ in range(3)]
    human_player = "X"
    computer_player = "O"
    
    current_player = human_player
    
    while True:
        print_board(board)
        
        if current_player == human_player:
            row = int(input(f"Player {current_player}, enter the row (0, 1, or 2): "))
            col = int(input(f"Player {current_player}, enter the column (0, 1, or 2): "))
        else:
            row, col = computer_move(board)
            print(f"Computer chose: ({row}, {col})")
        
        if board[row][col] != " ":
            print("Cell already taken, try again.")
            continue
        
        board[row][col] = current_player
        
        if check_winner(board, current_player):
            print_board(board)
            print(f"Player {current_player} wins!")
            break
        
        if is_full(board):
            print_board(board)
            print("It's a tie!")
            break
        
        current_player = computer_player if current_player == human_player else human_player

def main():
    print("Welcome to Tic Tac Toe!")
    print("1. Two Player Mode")
    print("2. Single Player Mode")
    choice = input("Choose the game mode (1 or 2): ")
    
    if choice == "1":
        two_player_mode()
    elif choice == "2":
        single_player_mode()
    else:
        print("Invalid choice, please restart the game.")

if __name__ == "__main__":
    main()