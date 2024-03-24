from typing import List

from shape import Shape


class Board:
    """
    Represents the Tic Tac Toe game board.
    """

    def __init__(self, size: int):
        self.size = size
        self.board = []
        for _ in range(self.size):
            self.board.append([None] * self.size)

    def get_size(self) -> int:
        return self.size

    def get_board(self) -> List[List[Shape]]:
        return self.board

    def put_shape(self, row: int, col: int, shape: Shape) -> bool:
        if self.board[row][col] is not None:
            return False
        self.board[row][col] = shape
        return True

    def is_space_left(self) -> bool:
        for c_row in self.board:
            for c_space in c_row:
                if c_space is None:
                    return True
        return False

    def print_board(self) -> None:
        for r in range(self.size):
            for c in range(self.size):
                if self.board[r][c] is not None:
                    print(self.board[r][c].get_shape_name(), end="")
                else:
                    print(" ", end="")
                print(" | ", end="")
            print()
