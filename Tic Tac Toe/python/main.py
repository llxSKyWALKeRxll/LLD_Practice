from game_host import GameHost
from player import Player
from shape_o import Shape_O
from shape_x import Shape_X

player1 = Player("sky", Shape_X())
player2 = Player("kaos", Shape_O())

players = [player1, player2]

gameHost = GameHost(players, 3)

gameHost.start_game()
