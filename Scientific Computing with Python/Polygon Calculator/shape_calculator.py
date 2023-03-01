class Shape:
    def __str__(self):
        return f"{type(self).__name__}({', '.join([f'{k}={v}' for k, v in self.__dict__.items() if k[0] != '_'])})"

class Rectangle(Shape):
    def __init__(self, width, height=None):
        super().__init__()
        self.width = width
        self.height = height if height is not None else width

    def set_width(self, new_width):
        self.width = new_width

    def set_height(self, new_height):
        self.height = new_height

    def get_area(self):
        return self.height * self.width

    def get_perimeter(self):
        return (2 * self.height) + (2 * self.width)

    def get_diagonal(self):
        return ((self.width ** 2 + self.height ** 2) ** 0.5)

    def get_picture(self):
        if self.width > 50 or self.height > 50:
            return "Too big for picture."
        else:
            return "\n".join(["*" * self.width for _ in range(self.height)])

    def get_amount_inside(self, shape):
        return int((self.width * self.height) / (shape.width * shape.height))


class Square(Rectangle):
    def __init__(self, side):
        super().__init__(side, side)

    def set_side(self, side):
        self.width = self.height = side
