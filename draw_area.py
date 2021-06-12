class DrawArea:

    def __init__(self, x: int, y: int, width: int, height: int) -> None:
        self.x = x
        self.y = y
        self.width = width
        self.height = height

    def update_rect(self):
        rect = (self.x, self.y, self.width, self.height)
        return rect

