# Karol Kraus, Piotr Mastalerz - Connect 4

BOARD_COLS = 7
BOARD_ROWS = 6

class Board():
    def __init__(self):
        self.board = [[' ' for _ in range(BOARD_COLS)] for _ in range(BOARD_ROWS)]
        self.turns = 0
        self.last_move = [-1, -1] # row, col

    def print_board(self):
        # Number the columns
        print("\n")
        for c in range(BOARD_COLS):
            print(f" ({c + 1}) ", end="")
        print("\n")

        # Print the slots
        for r in range(BOARD_ROWS):
            print('|', end="")
            for c in range(BOARD_COLS):
                print(f"  {self.board[r][c]} |", end="")
            print("\n")

        print(f"{'-' * 35}\n")

    def which_turn(self):
        players = ['X', 'O']

def play():
    game = Board()

    game.print_board()

if __name__ == '__main__':
    play()