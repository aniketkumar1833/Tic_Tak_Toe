import random
from colorama import init, Fore, Style

init(autoreset=True)

def show_board(board):
    print()

    def color_cell(cell):
        if cell == "X":
            return Fore.RED + cell + Style.RESET_ALL
        elif cell == "O":
            return Fore.BLUE + cell + Style.RESET_ALL
        return Fore.YELLOW + cell + Style.RESET_ALL

    print(f" {color_cell(board[0])} | {color_cell(board[1])} | {color_cell(board[2])}")
    print(Fore.CYAN + "---+---+---")
    print(f" {color_cell(board[3])} | {color_cell(board[4])} | {color_cell(board[5])}")
    print(Fore.CYAN + "---+---+---")
    print(f" {color_cell(board[6])} | {color_cell(board[7])} | {color_cell(board[8])}")
    print()

def choose_symbol():
    choice = ""

    while choice not in ["X", "O"]:
        choice = input(
            Fore.GREEN + "Choose your symbol (X/O): "
        ).upper()

    if choice == "X":
        return "X", "O"
    return "O", "X"

def user_turn(board, symbol):
    while True:
        try:
            position = int(input(Fore.YELLOW + "Pick a position (1-9): "))

            if position in range(1, 10) and board[position - 1].isdigit():
                board[position - 1] = symbol
                break
            else:
                print(Fore.RED + "⚠ Position unavailable. Try again.")

        except ValueError:
            print(Fore.RED + "⚠ Enter a valid number from 1 to 9.")

def computer_turn(board, computer_symbol, user_symbol):

    # Winning move
    for i in range(9):
        if board[i].isdigit():
            temp = board.copy()
            temp[i] = computer_symbol

            if check_winner(temp, computer_symbol):
                board[i] = computer_symbol
                return

    # Blocking move
    for i in range(9):
        if board[i].isdigit():
            temp = board.copy()
            temp[i] = user_symbol

            if check_winner(temp, user_symbol):
                board[i] = computer_symbol
                return

    available = [i for i in range(9) if board[i].isdigit()]
    board[random.choice(available)] = computer_symbol

def check_winner(board, symbol):

    patterns = [
        (0, 1, 2),
        (3, 4, 5),
        (6, 7, 8),
        (0, 3, 6),
        (1, 4, 7),
        (2, 5, 8),
        (0, 4, 8),
        (2, 4, 6)
    ]

    for a, b, c in patterns:
        if board[a] == board[b] == board[c] == symbol:
            return True

    return False

def board_full(board):
    return all(not item.isdigit() for item in board)

def start_game():

    print(Fore.CYAN + "🎮 Welcome to Smart Tic-Tac-Toe Arena!")

    player_name = input(
        Fore.GREEN + "👤 Enter your name: "
    )

    print(Fore.MAGENTA + f"\nHello {player_name}! Let's begin.\n")

    while True:

        board = [str(i) for i in range(1, 10)]

        player_symbol, computer_symbol = choose_symbol()

        current_turn = "Player"

        while True:

            show_board(board)

            if current_turn == "Player":

                user_turn(board, player_symbol)

                if check_winner(board, player_symbol):
                    show_board(board)
                    print(
                        Fore.GREEN
                        + f"🏆 Fantastic, {player_name}! You won the match!"
                    )
                    break

                if board_full(board):
                    show_board(board)
                    print(Fore.CYAN + "🤝 It's a draw!")
                    break

                current_turn = "Computer"

            else:

                print(Fore.MAGENTA + "🤖 Computer is making a move...")
                computer_turn(board, computer_symbol, player_symbol)

                if check_winner(board, computer_symbol):
                    show_board(board)
                    print(Fore.RED + "🤖 Computer wins this round!")
                    break

                if board_full(board):
                    show_board(board)
                    print(Fore.CYAN + "🤝 It's a draw!")
                    break

                current_turn = "Player"

        again = input(
            Fore.YELLOW + "\n🔄 Play another round? (yes/no): "
        ).lower()

        if again != "yes":
            print(
                Fore.CYAN
                + "\n👋 Thanks for playing Smart Tic-Tac-Toe Arena!"
            )
            break

if __name__ == "__main__":
    start_game()