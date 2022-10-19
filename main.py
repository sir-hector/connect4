# Authors:
# Karol Kraus s20687
# Piotr Mastalerz s21911

# game instructions https://en.wikipedia.org/wiki/Connect_Four
# environmental instructions
# create venv
#   python3 -m venv venv

import numpy as np
from easyAI import TwoPlayerGame, Human_Player, AI_Player, Negamax

class GameController(TwoPlayerGame):
    def __init__(self, players, board = None):

        # Define the players
        self.players = players

        # Define who starts the game
        self.current_player = 1

        # Define the playing board
        self.board = board if (board != None) else (np.array([[0 for i in range(7)] for j in range(6)]))

        # Define who starts the game
        self.current_player = 1

        # Define the positions
        self.pos_dir = np.array ([[[i, 0], [0, 1]] for i in range(6)] +
                                [[[0, i], [1, 0]] for i in range(7)] +
                                [[[i, 0], [1, 1]] for i in range(1, 3)] +
                                [[[0, i], [1, 1]] for i in range(4)] +
                                [[[i, 6], [ 1, -1]] for i in range(1, 3)] +
                                [[[0, i], [1, -1]] for i in range(3, 7)])

     # Define possible moves
    def possible_moves(self):
        """
        Return list of possible moves in each iteration

        Returns:
            list: list of possible moves(column numbers [0-6])
        """
        return [i for i in range(7) if (self.board[:, i].min() == 0)]

    # Define how to make the move
    def make_move(self, column):
        """
        Save move of current player into the board, each move take always the lowest place(row) in column

        Parameters:
        column (int) : number of chosen column by player

        Returns:
            None
        """
        line = np.argmin(self.board[:, column] != 0)
        self.board[line, column] = self.current_player

    # Show current status
    def show(self):
        """
        printing the board to the console

        Returns:
            None
        """
        print("\n" + "\n".join(["0 1 2 3 4 5 6", 13 * "-"] +
                                    [" ".join([[".", "O", "X"] [self.board[5 - j] [i]]
                                    for i in range(7)]) for j in range(6)]))

    # Define loss condition
    def loss_condition(self):
        """
        Checking if the board have winning sequence

        Returns:
            boolean: true if board has winning sequence, false if not
        """
        for pos, direction in self.pos_dir:
            streak = 0
            while (0 <= pos[0] <= 5) and (0 <= pos[1] <= 6):
                if self.board[pos[0], pos[1]] == self.opponent_index:
                    streak += 1
                    if streak == 4:
                        return True
                else:
                    streak = 0
                pos = pos + direction
        return False

    # Check if game is over
    def is_over(self):
        """
        checking if are any possible moves on the board or if the board has winning sequence

        Returns:
            boolean: true if game is over, false if not
        """
        return(self.board.min() > 0) or self.loss_condition()

    # Compute the score
    def scoring(self):
        """
        gives a score to the current game (for the AI)

        Returns:
            int: score(-100 or 0)
        """
        return -100 if self.loss_condition() else 0


if __name__ == "__main__":
    # Define the algorithm that will be used
    algo_neg = Negamax(5)

    # Start the game
    game = GameController([AI_Player(algo_neg), Human_Player()])
    game.play()

    # Print the result
    if game.loss_condition():
        print("\nPlayer", game.opponent_index, "wins. ")
    else:
        print("\nIt's a draw.")