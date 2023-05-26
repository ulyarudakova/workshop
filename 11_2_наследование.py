class Figure:
    def __init__(self):
        self.color = "white"

    def change_color(self, new_color):
        self.color = new_color

    def print_parameters(self):
        pass


class Oval(Figure):
    def __init__(self, width, height):
        super().__init__()
        self.width = width
        self.height = height

    def print_parameters(self):
        print("Это овал с шириной {} и высотой {}. Цвет: {}".format(self.width, self.height, self.color))


class Square(Figure):
    def __init__(self, side_length):
        super().__init__()
        self.side_length = side_length

    def print_parameters(self):
        print("Это квадрат с длиной стороны {}. Цвет: {}".format(self.side_length, self.color))


oval1 = Oval(5, 3)
oval1.change_color("blue")
oval1.print_parameters()

square1 = Square(4)
square1.print_parameters()
