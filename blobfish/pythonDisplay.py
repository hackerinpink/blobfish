import pygame #Importing pygame
import chess
import game,player
pygame.init() #Using pygame

board = chess.Board()
WINDOW_SIZE = (650, 650) #Size of the pop up window
WHITE = (255, 255, 255) #Setting white color
BLACK = (0, 0, 0) #Setting black color

GREEN = (0,127,0)
YELLOW = (255,255,200)

DISPLAY_SCREEN = pygame.display.set_mode(WINDOW_SIZE) #Creates a pop up window to display screen

the_game = game.Game(player.RandomPlayer(chess.WHITE,'WHITE'),player.RandomPlayer(chess.BLACK,"BLACK"))

pygame.display.set_caption("Chess Game Board") #The title of the DISPLAY_SCREEN

PIECES = {
    "K":"♔",
    "Q":"♕",
    "N":"♘",
    "B":"♗",
    "R":"♖",
    "P":"♙",
    "k":"♚",
    "q":"♛",
    "n":"♞",
    "b":"♝",
    "r":"♜",
    "p":"♟︎",

}
# font = pygame.font.Font("blobfish\CASEFONT.ttf",32)
font = pygame.font.SysFont("segoeuisymbol",80)
def setUp_board(): #Defining a function set up board
    
    
    for col in range(8): #Looping through the columns of the chess board
        for row in range(8): #Looping through the rows of the chess board
            each_square = pygame.Rect(col * 81.25, row * 81.25, 81.25, 81.25) #Going to the location of where each square needs to be drawn
            if (row + col) % 2 == 1: #If we are at an odd position then a black square is drawn
                pygame.draw.rect(DISPLAY_SCREEN, GREEN, each_square)
            else: #If we are at an even position then a white square is drawn
                pygame.draw.rect(DISPLAY_SCREEN, YELLOW, each_square)
    
    pygame.display.flip()

def update_pieces(b):
    for col in range(8):
        for row in range(8):
            piece = b.piece_at(chess.square(col,7-row))
            if piece is not None:
                pieceStr  = font.render(PIECES[piece.symbol()],True,BLACK)
                pieceRect = pieceStr.get_rect()
                pieceRect.center = ((81.25)*(col+0.5),(81.25)*(row+0.5))
                DISPLAY_SCREEN.blit(pieceStr,pieceRect)
    pygame.display.flip()
game = True #Setting a boolean variable game as true

setUp_board() #Setting up the game board
update_pieces(board)
while game: #While we are playing the game, we are getting the user input until the user input's quit. Then we set game = false and exit out of the while loop

    for event in pygame.event.get():

        if event.type == pygame.QUIT:

            game = False
    
    the_game.step()
    update_pieces(the_game.board)
    pygame.time.wait(10)
    if the_game.board.is_game_over():
        pass 
    else:
        setUp_board()
pygame.display.update() #Displays the upda

pygame.quit() #Quits pygame