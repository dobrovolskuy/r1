class Shape:
    def __init__(self, color):
        self.color = color

    def display_color(self):
        print(f"The color of the shape is{self.color}")

class Rectangle(Shape):
    def __init__(self, color, width, height):

        super(). __init__(color)

        self.width = width
        self.height = height

    def display_size(self):
        print(f"The size of the rectangle is {self.width} x {self.height}")

my_rectangle = Rectangle(color="blue", width=20, height=15)

my_rectangle.display_color()

my_rectangle.display_size()

