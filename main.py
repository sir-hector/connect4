# Karol Kraus, Piotr Mastalerz - Connect 4
from easyAI import TwoPlayerGame

BOARD_COLS = 7
BOARD_ROWS = 6

class Board(TwoPlayerGame):
    def __init__(self):
        self.board = [[' ' for _ in range(BOARD_COLS)] for _ in range(BOARD_ROWS)]
        self.turns = 0
        self.last_move = [-1, -1] # row, col

    def possible_moves(self):
        return [i+1 for i in range(BOARD_COLS) if (self.board[0][i] == " ")]

    def is_over(self):
        return []

    def make_move(self, move):
        return []

    def print_board(self):
        print(self.possible_moves())
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
        return players[self.turns % 2]

    def turn(self, column):
        # Search from the bottom up
        for r in range(BOARD_ROWS-1, -1, -1):
            if self.board[r][column] == ' ':
                self.board[r][column] = self.which_turn()
                self.last_move = [r, column]

                self.turns += 1
                return True
        return False

    def in_bounds(self, r, c):
        return r >= 0 and r < BOARD_ROWS and c >= 0 and c < BOARD_COLS

    def game_winner(self):
        last_row = self.last_move[0]
        last_col = self.last_move[1]
        last_letter = self.board[last_row][last_col]

        # [r.c] direction, matching letter count, locked bool
        directions = [
            [[-1, 0], 0, True],
            [[1, 0], 0, True],
            [[0, -1], 0, True],
            [[0, 1], 0, True],
            [[-1, -1], 0, True],
            [[1, 1], 0, True],
            [[-1, 1], 0, True],
            [[1, -1], 0, True],
        ]

        # Search outwards looking for matching letters
        for a in range(4):
            for d in directions:
                r = last_row + (d[0][0] * (a+1))
                c = last_col + (d[0][1] * (a+1))
                if d[2] and self.in_bounds(r,c) and self.board[r][c] == last_letter:
                    d[1] += 1
                else:
                    # STOP searching in this direction
                    d[2] = False

        #Check possible direction pairs for '4 pieces in a row'
        for i in range(0,7,2):
            if(directions[i][1] + directions[i+1][1] >= 3):
                self.print_board()
                print(f"{last_letter} is the Winner")
                return last_letter

        # did not find a winner
            return False


def play():
    game = Board()

    game_over = False
    while not game_over:
        #continue playing

        game.print_board()
        valid_move = False
        while not valid_move:
            user_move = input(f"{game.which_turn()}'s turn - please pick a column 1-7 ")
            try:
                valid_move = game.turn(int(user_move) - 1)
            except:
                print(f"Please choose a number betwwen 1 and {BOARD_COLS}")

        game_over = game.game_winner()

if __name__ == '__main__':
    play()