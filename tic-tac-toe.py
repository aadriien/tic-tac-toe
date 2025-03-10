def get_board():
    board = [[" " for _ in range(3)] for _ in range(3)]
    return board


def print_board(board):
    print("\n")
    for i in range(3):
        print(" " + board[i][0] + " | " + board[i][1] + " | " + board[i][2] + " ")
        if i < 2:
            print("---+---+---")
    print("\n")


def get_move(curr_player, board):
    curr_move = input(f"Player {curr_player}, choose your move (1-9): ")
    
    # Confirm valid choice & return array position
    if not (curr_move.isdigit() and int(curr_move) - 1 in range(9)):
        print(f"Position {curr_move} is not valid. Try again.\n")
        return get_move(curr_player, board)

    row = (int(curr_move) - 1) // 3
    col = (int(curr_move) - 1) % 3

    if board[row][col] != " ":
        print(f"Position {curr_move} is taken. Try again.\n")
        return get_move(curr_player, board)
    
    board[row][col] = curr_player


def check_for_winner(board):
    for i in range(3):
        # Check rows
        if board[i][0] == board[i][1] == board[i][2] != " ":
            return board[i][0]

        # Check columns
        if board[0][i] == board[1][i] == board[2][i] != " ":
            return board[i][0]

    # Check diagonals
    if board[0][0] == board[1][1] == board[2][2] != " ":
        return board[0][0]
    
    if board[0][2] == board[1][1] == board[2][0] != " ":
        return board[0][2]

    return ""


def check_full_board(board):
    for i in range(3):
        for j in range(3):
            if board[i][j] == " ":
                return False
    return True


def run_game():
    new_board = get_board()
    curr_player = "X"
    game_over = False

    while not game_over:
        print_board(new_board)

        get_move(curr_player, new_board)

        winner = check_for_winner(new_board)
        if winner != "":
            print(f"\nCongrats, player {winner}! You win!\n")
            game_over = True

        elif check_full_board(new_board):
            print(f"\nGame over, you ran out of spaces!\n")
            game_over = True

        curr_player = "O" if curr_player == "X" else "X"

    return new_board



def main():
    final_board = run_game()

    print(f"Here's your board!\n")
    print_board(final_board)


if __name__ == "__main__":
    main()     

    

