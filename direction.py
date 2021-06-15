

class Direction:

    def __init__(self, dx: int, dy: int):
        self.dx = dx
        self.dy = dy

    def get_opposite(self):
        direction = Directions
        if self == direction.NORTH:
            return direction.SOUTH
        if self == direction.SOUTH:
            return direction.NORTH
        if self == direction.EAST:
            return direction.WEST
        if self == direction.WEST:
            return direction.EAST

class Directions:

    # create all four direction with the correct dx and dy in each case
    NORTH = Direction(0, -1)
    SOUTH = Direction(0, 1)
    EAST = Direction(1, 0)
    WEST = Direction(-1, 0)



