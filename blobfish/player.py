import chess


class Player:
  """An arbitrary player capable of choosing a move and storing state"""
  def __init__(self, color: chess.Color, name: str):
      # Name should be in LastName, FirstName format
      self.name = name
      
      self.color = color
      self.score = {"Wins": 0, "Losses": 0, "Draws": 0}
      self.check = False
      self.en_passant = False
      self.castling = {'kingside': True, 'queenside': True}
      self.move_sequence = []

  def MakeMove(self, board: chess.Board):
      # TODO: Update with NN functionality
      pass

  def update_castling_rights(self, previous_castling):
      for square in previous_castling:
          if previous_castling[square]:
              self.castling[square] = False

  def read_board(self, game):
      """Reads the state of the Game.board, and updates Player attributes.
      Note: This overwrites all existing Player attributes with the Game
      version. This function should be called if these have somehow been
      desynchronized.
      """
      self.castling = game.can_castle[self.color]
      self.check = game.in_check[self.color]
      move_sequence = []
      self.en_passant = game.has_en_passant[self.color]
      for i in range(len(game.moves)):
          # Update move_sequence based on every other move in move_stack.
          # Since int(chess.WHITE) = int(True) = 1, this will pick even-
          # numbered moves for white, and odd for black
          move_sequence.append((game.moves[2*i + (not int(self.color))]))
      self.move_sequence = move_sequence

class RandomPlayer(Player):
    """A Player that moves entirely randomly."""
    def MakeMove(self, board: chess.Board):
      legal_moves = list(board.legal_moves)
      import random
      if len(legal_moves) > 0:
        player_move = random.choice(legal_moves)
      current_castling = self.castling.copy()
      self.update_castling_rights(current_castling)
      if board.is_check():
          self.check = True
      else:
          self.check = False
      self.move_sequence.append(str(player_move))
      return str(player_move)
    
class HumanPlayer(Player):
    """A Player whose actions are chosen by a human."""
    def MakeMove(self, board: chess.Board):
        move = input("Please type a move in UCI format: ")
        while chess.Move.from_uci(move) not in list(board.legal_moves):
            print("Move is not legal!")
            move = input("Please type a move in UCI format: ")
        return move