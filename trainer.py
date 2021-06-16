import pokemon


# this class represent a pokemon trainer
class Trainer:

    def __init__(self, poke: pokemon.Pokemon) -> None:
        self.pokemon_list = []
        self.pokemon_list.append(poke)

    def add_pokemon(self, poke: pokemon.Pokemon) -> bool:
        if len(self.pokemon_list) >= 6:
            return False
        else:
            self.pokemon_list.append(poke)
            return True

    def get_current_pokemon(self) -> pokemon.Pokemon:
        return self.pokemon_list[0]

    def get_pokemon_list_size(self) -> int:
        return len(self.pokemon_list)
