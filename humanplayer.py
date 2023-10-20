import chess
from game import Game
from player import Player

class HumanPlayer(Player):
    """Represents a human or other sapient player."""
    def MakeMove(self, board):
        print("UCI Format: {starting square}{x if capturing}{ending square}{piece symbol if promoting}")
        print("e.g.: e2e4, e7e8q")
        move = input("Please type a move in UCI format")
        while move not in list(board.legal_moves):
            print("Move is not legal!")
            move = input("Please type a move in UCI format")
        return move