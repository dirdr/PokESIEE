from typing import Optional, Dict, List, Any
import spritesheet
from entity import Entity
from type import TYPES, Type
from move import Move
from utils import get_args
import json


def to_3_digit(num: int) -> str:
    if num < 10:
        return "00" + str(num)
    if num < 100:
        return "0" + str(num)
    return str(num)


poke_dos = Entity(2976, 2016, 'poke_dos.png')
poke_face = Entity(2976, 2016, 'poke_face.png')

ID_LIST: List[int] = [4, 5, 6, 252, 253, 254, 393, 394, 395, 16, 17, 18, 25, 26, 19, 20, 261, 262, 143, 29, 30, 31, 32,
                      33, 34, 58, 59, 43, 44, 45,
                      231, 232, 403, 404, 405, 276, 277, 532, 533, 534, 92, 93, 94, 200, 429, 406, 315, 407, 543, 544,
                      545, 355, 356, 477, 198,
                      430, 451, 452, 228, 229, 246, 247, 248, 442, 607, 608, 609, 396, 397, 398, 309, 310, 624, 625,
                      626, 287, 288, 289, 179,
                      180, 181, 27, 28, 111, 112, 464, 304, 305, 306, 529, 530, 551, 552, 553, 322, 323, 449, 450, 115,
                      344, 350, 437, 589, 617,
                      614, 473, 362, 76, 472
                      ]
NB_POKEMON: int = 651
POKEMONS: List[Optional['Pokemon']] = [None for i in range(NB_POKEMON + 1)]


class Pokemon(Entity):

    def __init__(self, id: int, data: Dict[str, Any], ):
        super(Pokemon, self).__init__(96, 96, 'empty.png')
        self.name: str = get_args(data, "name", id)
        self.id: int = id
        self.level: int = get_args(data, "level", id)
        self.exp: int = 0
        self.exp_max: int = self.level ** 3
        self.base_health: int = get_args(data, "base_health", id)
        self.health: int = int((2 * self.base_health * self.level) / 100 + self.level + 10)
        self.health_max: int = self.health
        self.types: List[Type] = [TYPES[t] for t in get_args(data, "type", id)]
        self.attack: int = get_args(data, "stats", id)["attack"]
        self.defense: int = get_args(data, "stats", id)["defense"]
        self.attack_spe: int = get_args(data, "stats", id)["attack_spe"]
        self.defense_spe: int = get_args(data, "stats", id)["defense_spe"]
        self.speed: int = get_args(data, "stats", id)["speed"]
        self.all_moves: List[Move] = get_args(data, "ability", id)
        self.exp_points: int = get_args(data, "exp_points", id)
        self.front_image = spritesheet.pick_image(poke_face.image, id % 31 * 96, int(id / 31) * 96, self.width,
                                                  self.height)
        self.back_image = spritesheet.pick_image(poke_dos.image, id % 31 * 96, int(id / 31) * 96, self.width,
                                                 self.height)
        self.evolution: List[Optional[int]] = get_args(data, "evolution", id)

    def calc_exp_max(self) -> None:
        self.exp_max = self.level ** 3

    def calc_health_max(self) -> None:
        self.health_max = (2 * self.base_health * self.level) / 100 + self.level + 10
        self.health = self.health_max

    def get_name(self) -> str:
        return self.name

    @staticmethod
    def load_pokemons():
        global POKEMONS, NB_POKEMON
        for i in range(0, len(ID_LIST)):
            poke_id: int = ID_LIST[i]
            id_str = to_3_digit(poke_id)
            try:
                with open("data/pokemon/{}.json".format(id_str), "r", encoding='utf-8') as file:
                    data = json.load(file)
                    POKEMONS[poke_id] = Pokemon(poke_id, data)
            except FileNotFoundError:
                print(f'pokemon id : {poke_id}, not found')
                break
        # while POKEMONS[-1] is None:
        # del POKEMONS[-1]
        NB_POKEMON = len(POKEMONS) - 1


def get_poke(num_id: int):
    return POKEMONS[num_id].get_name()



