import chess
import chess.pgn
import datetime
from player import Player


class Game:
    """This class represents an arbitrary chess game"""
    def __init__(self, player_white: Player, player_black: Player):
        self.player_white = player_white
        self.player_black = player_black

        self.board = chess.Board()
        self.moves = self.board.move_stack #  Only edit with board methods
        self.turn = self.board.turn

        self.has_en_passant = {chess.WHITE: False, chess.BLACK: False} 
        self.in_check = {chess.WHITE: False, chess.BLACK: False}
        self.can_castle = {
            chess.WHITE: {"kingside": True, "queenside": True}, 
            chess.BLACK: {"kingside": True, "queenside": True}
            }
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
                self.in_check[not self.turn] = True
            self.board.push(move)
        except chess.IllegalMoveError:
            print("Error: Not a legal move.")
            return False
        
        self.has_en_passant[self.turn] = self.board.has_legal_en_passant
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

    def play(self):
        """Begin and run the game. Currently only supports TUI."""
        print("Welcome to Blobfish chess!")
        print("UCI Format: {start square}{end square}{promotion if app.}")
        print("e.g.: e2e4, e7e8q")
        turn = 1
        while not self.board.is_game_over():
            print("Turn", turn)
            print("Board:")
            print(self)
            print("White's move")
            self.choose_move(self.player_white.MakeMove(self.board))
            if not self.board.is_game_over(): #  For when White checkmates
                print("Black's move")
                self.choose_move(self.player_black.MakeMove(self.board))
            turn += 1
        if self.victor == True:
           print("Game over! White wins!") 
        elif self.victor == False: 
            print("Game over! Black wins!")
        else:
            print("Game over! Draw!")
    
    def export_game(self, filename=None):
        """Export the Game to a .pgn file"""
        time_now = datetime.datetime.now().strftime('%Y-%m-%d-%H%M%S')
        date_now = datetime.date.isoformat(datetime.date.today())
        if filename is None:
            filename = "blobfish-" + time_now + ".pgn"
        match = chess.pgn.Game.from_board(self.board)
        
        match.headers["Event"] = "Blobfish Match " + time_now
        match.headers["Site"] = "Blobfish Engine"
        match.headers["Date"] = date_now
        match.headers["Round"] = 1 #  TODO
        match.headers["White"] = self.player_white.name
        match.headers["Black"] = self.player_black.name

        with open(filename, "w") as file:
            file.write(str(match))

class Scoreboard:
    """This class represents a history of played games"""
    def __init__(self):
        self.scoreboard = {chess.WHITE: 0, chess.BLACK: 0, None: 0}
        self.record = [] # A list of past Games, which can be reviewed later

    def update(self, game: Game):
        """Increments the scoreboard and updates the record.
        Assumes Game has been concluded.
        """
        self.scoreboard[game.victor] += 1
        self.record.append(game)