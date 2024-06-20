import numpy as np

class TicTacToe:
    def __init__(self):
        self.board = np.zeros((3, 3), dtype=int)
        self.done = False
        self.winner = None

    def reset(self):
        self.board.fill(0)
        self.done = False
        self.winner = None
        return self.board

    def available_actions(self):
        return [(i, j) for i in range(3) for j in range(3) if self.board[i, j] == 0]

    def step(self, action, player):
        if self.done:
            raise Exception("Game is already over")
        if self.board[action] != 0:
            raise Exception("Invalid move")

        self.board[action] = player
        self.done, self.winner = self.check_winner()
        return self.board, self.done, self.winner

    def check_winner(self):
        for player in [1, -1]:
            for i in range(3):
                if np.all(self.board[i, :] == player) or np.all(self.board[:, i] == player):
                    return True, player
            if self.board[0, 0] == self.board[1, 1] == self.board[2, 2] == player or \
               self.board[0, 2] == self.board[1, 1] == self.board[2, 0] == player:
                return True, player
        if np.all(self.board != 0):
            return True, 0
        return False, None

    def render(self):
        print(self.board)

