import pokemon


class Trainer:

    def __init__(self, poke: pokemon.Pokemon):
        self.pokemon_list = []
        self.pokemon_list.append(poke)

    def add_pokemon(self, poke: pokemon.Pokemon) -> bool:
        if len(self.pokemon_list) >= 6:
            return False
        else:
            self.pokemon_list.append(poke)
            return True

    def get_pokemon_list_size(self):
        return len(self.pokemon_list)



