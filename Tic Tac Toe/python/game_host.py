from collections import deque
from typing import List

from board import Board
from player import Player
from shape import Shape


class GameHost:
    """
    Helper/Host for the game.
    """

    def __init__(self, players: List[Player], board_size: int):

        if len(players) > 2:
            raise TypeError("There is a size limit of 2 players!")
        self.players = deque()
        for player in players:
            self.players.append(player)
        self.board = Board(board_size)

    def start_game(self) -> None:

        print(f"Game between {self.players[0].get_name()} & {self.players[1].get_name()} has started!")

        ongoing_game = True

        while ongoing_game:

            self.board.print_board()
            is_space_left = self.board.is_space_left()
            if not is_space_left:
                print("It is a tie!")
                break
            curr_player = self.players.popleft()
            print(f"It is {curr_player.get_name()}'s turn.")
            i_row = int(input("Enter the desired row (0-indexed) => "))
            if i_row >= self.board.get_size() or i_row < 0:
                print("Invalid row input, please try again")
                self.players.appendleft(curr_player)
                continue
            i_col = int(input("Enter the desired column (0-indexed) => "))
            if i_col >= self.board.get_size() or i_col < 0:
                print("Invalid column input, please try again")
                self.players.appendleft(curr_player)
                continue
            is_valid_move = self.board.put_shape(i_row, i_col, curr_player.get_shape())
            if not is_valid_move:
                print("Invalid move, please try again")
                continue
            self.players.append(curr_player)
            has_player_won = self.check_for_winner(i_row, i_col, curr_player.get_shape())
            if has_player_won:
                print(f"Congratulations {curr_player.get_name()}, you have won the game!")
                self.board.print_board()
                return

    def check_for_winner(self, row: int, col: int, shape: Shape) -> bool:

        row_match, col_match, diagonal_match, anti_diagonal_match = True, True, True, True

        for c in range(self.board.get_size()):
            if self.board.board[row][c] is None or self.board.board[row][c] != shape:
                row_match = False
                break

        for r in range(self.board.get_size()):
            if self.board.board[r][col] is None or self.board.board[r][col] != shape:
                col_match = False
                break

        for i in range(self.board.get_size()):
            if self.board.board[i][i] is None or self.board.board[i][i] != shape:
                diagonal_match = False
                break

        for i in range(self.board.get_size()):
            j = self.board.get_size() - 1 - i
            if self.board.board[i][j] is None or self.board.board[i][j] != shape:
                anti_diagonal_match = False
                break

        return row_match or col_match or diagonal_match or anti_diagonal_match
