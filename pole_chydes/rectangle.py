class Rectangle:
    def __init__(self, width, heigth):
        self.width = width
        self.heigth = heigth

    def calculate_area(self):
        return self.width * self.heigth

    def calculate_perimeter(self):
        return 2 * (self.width + self.heigth)

rectangle_object = Rectangle(width=5, heigth=4)

area = rectangle_object.calculate_area()
perimeter = rectangle_object.calculate_perimeter()

print(f"Area of the rectangle: {area}")
print(f"Perimetr ot the rectangle:{perimeter}")
