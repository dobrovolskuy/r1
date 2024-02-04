class Sguare(Rectangle):
    def __init(self, color, side_length):
        super().__init(color, side_length, side_length)
        self.side_length = side_length


    def display_side(self):
        print(f"Side Length: {self.side_length}")


    def display_color(self):
        super().display_color()
        print(f"Side Length: {self.side_length}")

sguare = Sguare(color = "Red", side_length = 8)
sguare.display_color()
sguare.display_side()