class Player:
  def __init__(self, color, board):
      self.color = color
      self.check = False
      self.en_passant = False
      self.check = False
      self.en_passant = False
      self.castling = {'kingside': True, 'queenside': True}
      self.board = board
      self.move_sequence = []

  def MakeMove(self):
      legal_moves = list(self.board.legal_moves)
      import random
      player_move = random.choice(legal_moves)
      current_castling = self.castling.copy()
      self.board.push(player_move)
      self.update_castling_rights(current_castling)
      if self.board.is_check():
          self.check = True
      else:
          self.check = False
      self.move_sequence.append(str(player_move))
      return str(player_move)

  def update_castling_rights(self, previous_castling):
      for square in previous_castling:
          if previous_castling[square]:
              self.castling[square] = False
