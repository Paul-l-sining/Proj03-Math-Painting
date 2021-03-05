
class Rectangle:
    def __init__(self, x, y, a, b, color):
        self.color = color
        self.b = b  # width
        self.a = a  # length
        self.y = y
        self.x = x

    def draw(self, canvas):
        # changing the pixels color to make the rectangle
        canvas.data[self.y:self.b + self.y, self.x:self.a + self.x] = self.color


class Square:
    def __init__(self, x, y, a, color):
        self.color = color
        self.a = a
        self.y = y
        self.x = x

    def draw(self, canvas):
        # changing the pixels color to make the square
        canvas.data[self.y:self.a + self.y, self.x:self.a + self.x] = self.color
