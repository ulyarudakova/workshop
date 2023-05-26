class Circle:
    def __init__(self, color, size, radius):
        self.color = color
        self.size = size
        self.radius = radius


class Square:
    def __init__(self, color, size, side_length):
        self.color = color
        self.size = size
        self.side_length = side_length


class Box:
    def __init__(self):
        self.shapes = []

    def add_shape(self, shape):
        self.shapes.append(shape)
