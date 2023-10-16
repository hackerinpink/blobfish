import chess,random,colorama
colorama.just_fix_windows_console()

board = chess.Board()
print(board)

def makeMove(b):
    legal_moves = list(b.legal_moves)
    if len(legal_moves) > 0:
        random_move = random.choice(legal_moves)
        b.push(random_move)
    return b

while board.outcome() == None:
    start_square = input('Enter move starting square: ').lower()
    end_square = input('Enter move ending square: ').lower() 
    attempted_move = chess.Move.from_uci(start_square+end_square)
    while attempted_move not in board.legal_moves:
        print(colorama.Fore.RED + 'Move is illegal' + colorama.Style.RESET_ALL)
        start_square = input('Enter move starting square: ').lower()
        end_square = input('Enter move ending square: ').lower()
        attempted_move = chess.Move.from_uci(start_square+end_square)
    board.push(attempted_move)
    board = makeMove(board)
    print(board)

