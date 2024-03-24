from shape import Shape
from shape_type import Shape_Type


class Shape_X(Shape):
    """
    Represents the shape X.
    """

    def __init__(self):
        super().__init__(Shape_Type.shape_x)
