from shape import Shape


class Player:
    """
    Represents a player.
    """

    def __init__(self, name: str, shape: Shape):
        self.name = name
        self.shape = shape

    def get_name(self) -> str:
        return self.name

    def get_shape(self) -> Shape:
        return self.shape
