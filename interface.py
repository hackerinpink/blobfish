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
        self.player_white = player_white
        self.player_black = player_black

        self.board = chess.Board()
        self.moves = self.board.move_stack # Should not be modified directly; use Board methods
        self.turn = self.board.turn

        self.in_check = {chess.WHITE: False, chess.BLACK: False}
        self.can_castle = {chess.WHITE: True, chess.BLACK: True}
        self.victor = None


    def __repr__(self):
        return self.board.fen()

    def __str__(self):
        board_list = [[],[],[],[],[],[],[],[]]
        board_string = ""

        # Initialize the list
        for rank in range(0, 7):
            for file in range(0, 7):
                board_list[rank].append(None)

        for rank in range(0,7):
            for file in range(0,7):
                if self.board.piece_at(chess.square(file,rank)) is not None:
                    board_list[rank][file] = self.board.piece_at(chess.square(file,rank)).symbol()
        for rank in board_list:
            board_string = str(board_list) + "\n"
        return board_string

    def choose_move(self,move: chess.Move):
        if move in self.board.legal_moves:
            if self.board.gives_check(move):
                self.in_check[not self.turn] = True
            self.board.push(move)
        else:
            raise chess.IllegalMoveError

        self.can_castle[self.turn] = self.board.has_castling_rights(self.turn)
        self.turn = self.board.turn # Run this AFTER any attribute updates

        if self.board.is_checkmate():
            self.game_over()

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

    def automate(self, turns=0):
        """Yield control of the board to the robots, for an optional number of turns (defaults until game over)"""
        turn = 1
        while (not self.board.is_game_over()):
            pass
        pass


class Scoreboard:
    """This class represents a history of played games"""
    def __init__(self):
        self.scoreboard = {chess.WHITE: 0, chess.BLACK: 0, None: 0}
        self.record = [] # A list of past Games, which can be reviewed later

    def update(self, game: Game):
        """Increments the scoreboard and updates the record. Assumes game has been concluded"""
        self.scoreboard[game.victor] += 1
        self.record.append(game)