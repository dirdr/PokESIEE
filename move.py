class Move:

    def __init__(self, move_type: str, category: str, pp: int, power: int, accuracy: int) -> None:
        self.move_type = move_type
        self.category = category
        self.pp = pp
        self.power = power
        self.accuracy = accuracy

