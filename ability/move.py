from type import TYPES, Type

SPECIAL = "SPECIAL"
STATUS = "STATUS"
PHYSICAL = "PHYSICAL"

CATEGORYS: list[str] = [SPECIAL, STATUS, PHYSICAL]


class MoveError(Exception):
    def __init__(self, *args):
        if args:
            self.message = args[0]
        else:
            self.message = None

    def __str__(self) -> str:
        if self.message:
            return f"MoveError : {self.message}"
        else:
            return "Error in class Move has been raised"


class AbstractMove:

    def __init__(self, name: str, move_type: str, category: str, pp: int, power: int, accuracy: int,
                 self_dmg: int) -> None:
        self.name: str = name
        self.move_type: Type = TYPES[move_type]
        if category not in CATEGORYS:
            raise MoveError(f"Invalid category {category}, not in CATEGORYS list")
        self.category: str = category
        self.pp: int = pp
        self.pp_max: int = pp
        self.power: int = power
        self.accuracy: int = accuracy
        self.self_dmg: int = self_dmg

    def use(self):
        pass
