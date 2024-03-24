from shape_type import Shape_Type


class Shape:
    """
    Represents a Shape on the board.
    """

    def __init__(self, shape: Shape_Type):
        self.shape = shape

    def get_shape(self) -> Shape_Type:
        return self.shape

    def get_shape_name(self):
        return self.shape.value
