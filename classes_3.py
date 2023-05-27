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
        
    def print_contents(self):
        for shape in self.shapes:
            if isinstance(shape, Circle):
                print(f"Circle - Color: {shape.color}, Size: {shape.size}, Radius: {shape.radius}")
            elif isinstance(shape, Square):
                print(f"Square - Color: {shape.color}, Size: {shape.size}, Side Length: {shape.side_length}")


circle1 = Circle("red", "small", 5)
square1 = Square("blue", "medium", 4)
circle2 = Circle("green", "large", 10)

box = Box()
box.add_shape(circle1)
box.add_shape(square1)
box.add_shape(circle2)


box.print_contents()
