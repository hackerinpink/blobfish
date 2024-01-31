import chess

import player
import game

scoreboard = game.Scoreboard()

print("Blobfish Chess Engine, version 0.1")
ready = False

# TODO: Possibly move some of this into other modules to minimize __main__ 
white_name = input("Enter White's name (LastName, Firstname): ")
black_name = input("Enter Black's name (LastName, Firstname): ")

player_white = None
player_black = None

match_type = input(
    """ Please choose one of the following:
    [1] Human v. Human
    [2] Human v. Random
    [3] Random v. Random
    """)
match_type = int(match_type)

match match_type:
    case 1:
        player_white = player.HumanPlayer(chess.WHITE, white_name)
        player_black = player.HumanPlayer(chess.BLACK, black_name)
    case 2:
        player_white = player.HumanPlayer(chess.WHITE, white_name)
        player_black = player.RandomPlayer(chess.BLACK, black_name)
    case 3:
        player_white = player.RandomPlayer(chess.WHITE, white_name)
        player_black = player.RandomPlayer(chess.BLACK, black_name)

ready = True
while ready:
    the_game = game.Game(player_white, player_black)
    print("Open the game!")
    the_game.play()
    scoreboard.update(the_game)
    match input("Go again? [y/n]"):
        case "y":
            ready = True
        case "n":
            ready = False
            print("Thanks for playing!")
            print("Score:")
            print(scoreboard.scoreboard)
            if (input("Save record? [y/n] ") == "y"):
                scoreboard.export_scoreboard()