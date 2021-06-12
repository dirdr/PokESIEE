from entity import Entity


class Tile(Entity):

    # For all the collisions and interaction side, all the cardinal pole are describe as the following
    # NORTH SOUTH EAST WEST
    def __init__(self, name: str, width: int, height: int, collision: [],  image_path: str) -> None:
        super().__init__(width, height, image_path)
        self.name = name
        self.collision = collision


class TileGRASS(Tile):

    def __init__(self) -> None:
        super(TileGRASS, self).__init__('Grass', 32, 32, [False, False, False, False], "unknown")


class TileTREE(Tile):

    def __init__(self) -> None:
        super(TileTREE, self).__init__('Tree', 32, 32, [True, True, True, True], "unknown")


class TileNONE(Tile):

    def __init__(self) -> None:
        super(TileNONE, self).__init__('None', 32, 32, [False, False, False, False], "unknown")


class TileSIGN(Tile):

    def __init__(self, message: str) -> None:
        super(TileSIGN, self).__init__('Sign', 32, 32, [True, True, True, True], "unknown")
        self.interactionSide = []
        self.message = message

    def load(self) -> None:
        self.interactionSide = [False, True, False, False]


class TileROCK(Tile):

    def __init__(self) -> None:
        super(TileROCK, self).__init__('Rock', 32, 32, [True, True, True, True], "unknown")


class TileFENCE(Tile):

    def __init__(self) -> None:
        super(TileFENCE, self).__init__('Fence', 32, 32, [True, True, True, True], "unknown")


class TileSAND(Tile):

    def __init__(self):
        super(TileSAND, self).__init__('Sand', 32, 32, [False, False, False, False], "unknown")

class TileFLOWER(Tile):

    def __init__(self) -> None:
        super(TileFLOWER, self).__init__('Flower', 32, 32, [False, False, False, False], "unknown")
        self.animation = "A IMPLEMENTER"

    def update(self) -> None:
        pass

    def load_sprite(self) -> None:
        pass

class TileOneWayFENCE:

    def __init__(self):
        super(TileOneWayFENCE, self).__init__('OneWayFence', 32, 32, [True, False, False, False], "unknown")


class TileBLOCKED(Tile):

    def __init__(self):
        super(TileBLOCKED, self).__init__("Blocked", 32, 32, [True, True, True, True], "unknown")













