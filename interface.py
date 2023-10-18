import chess
from player import Player

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
        return self.board.fen

    def __str__(self):
        return str(self.board)    
    
    def choose_move(self,move: chess.Move):
        """Checks the given move for validity and pushes it to the board. 
        Accepts a Move object or a str in UCI.
        Returns True if the move was successful, and False otherwise. 
        """
        if type(move) == str:
            try:
                move = chess.Move.from_uci(move)
            except chess.IllegalMoveError:
                print("Error: Str must be a valid move in UCI format.")
                return False
            
        try:
            if self.board.gives_check(move):
                self.in_check[not self.turn] = True #  Declares the opposing Player to be in check
            self.board.push(move)
        except chess.IllegalMoveError:
            print("Error: Not a legal move.")
            return False
        
        self.can_castle[self.turn] = self.board.has_castling_rights(self.turn)
        self.turn = self.board.turn #  Run this AFTER any attribute updates

        if self.board.is_checkmate():
            self.game_over()
        return True

    def game_over(self):
        """Declares a victor for the Game and updates the Players' scores.
        Assumes Game has been concluded.
        """
        self.victor = self.board.outcome().winner
        if self.victor == chess.WHITE:
            self.player_white.score["Wins"] += 1
            self.player_black.score["Losses"] += 1
        elif self.victor == chess.BLACK:
            self.player_black.score["Wins"] += 1
            self.player_white.score["Losses"] += 1
        else:
            self.player_white.score["Draws"] += 1
            self.player_black.score["Draws"] += 1

class Scoreboard:
    """This class represents a history of played games"""
    def __init__(self):
        self.scoreboard = {chess.WHITE: 0, chess.BLACK: 0, None: 0}
        self.record = [] # A list of past Games, which can be reviewed later

    def update(self, game: Game):
        """Increments the scoreboard and updates the record.
           Assumes Game has been concluded."""
        self.scoreboard[game.victor] += 1
        self.record.append(game)