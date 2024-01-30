#
class Shape:
    def __init__(self, color):
        self.color = color

    def show_color(self):
        print(f"The color of the shape is {self.color}")


class Rectangle(Shape):
    def __init__(self, color, width, height):
        super().__init__(color)
        self.width = width
        self.height = height

    def display_color(self):
        super().show_color()
        print(f"Width {self.width}, Height {self.height}")

rectangle = Rectangle(color="Red", width=20, height=5)
rectangle.display_color()