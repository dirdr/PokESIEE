def find_opposite(direction):
    if direction == 'South':
        return 'North'
    if direction == 'North':
        return 'South'
    if direction == 'East':
        return 'West'
    if direction == 'West':
        return 'East'


class Warp:

    def __init__(self, coordinate: (int, int)):
        self.coordinate = coordinate
