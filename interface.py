#!/usr/bin/env python3
import chess

class Player:
    """This class acts as the interface between the chess bots themselves and the game simulation."""
    def __init__(self, bot, color: chess.Color):
        self.color = color

        self.wins = 0
        self.losses = 0
        self.draws = 0

        """Fill in once bot functionality is determined"""
        pass

    def find_move(self, board: chess.Board):
        """
        This method accepts a chess.BaseBoard object and tells the chess bot to calculate an ideal move given its state.
        It returns a chess.Move object.
        """
        state = board.board_fen()
        TestBoard = board.copy() # Creates a copy of the current board for the bot to analyze

        move = None

        TestBoard.push(move)

        # if bot.Magic(move, TestBoard) = True:
        #   ideal_move = move

        ideal_move = None
        return ideal_move

class Game:
    """This class represents an arbitrary chess game"""
    def __init__(self, player_white: Player, player_black: Player):
        self.board = chess.Board()
        # self.scoreboard = {chess.WHITE: 0, chess.BLACK: 0, None: 0} # None represents draws
        self.victor = None

        self.player_white = player_white
        self.player_black = player_black


    def game_over(self):
        self.victor = self.board.outcome().winner
        if self.victor == chess.WHITE:
            self.player_white.wins += 1
            self.player_black.losses += 1
        elif self.victor == chess.BLACK:
            self.player_black.wins += 1
            self.player_white.losses += 1
        else:
            self.player_white.draws += 1
            self.player_black.draws += 1


# Preserved for potential future development paths
# class Board:
#     """This class represents a chessboard. """
#     def __init__(self):
#         self.board = [] # The current state of the board, represented by a nested list
#         self.moves = [] # A list of all moves in the game
#
#     def move_piece(self, move, player):
#         """
#         This function updates the Board object with the desired move. move should be a string in chess notation,
#         and player should be either 0 for white, or 1 for black.
#         """
#
