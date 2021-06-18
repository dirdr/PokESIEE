import os
import config
import localisation
import pokemon
import warp
from entity import Entity
import random
import animation
import battle


class GameMap(Entity):

    # game_map constructor
    def __init__(self, width: int, height: int, image_path: str, collision_path: str,
                 pokemon_list: list[pokemon.Pokemon], name: str, game):
        self.game = game
        super(GameMap, self).__init__(width, height, image_path)
        self.pokemon_list = pokemon_list
        self.animation_manager = self.game.animation_manager
        self.player_trainer = self.game.player_trainer
        self.tile_size = config.TILE_SIZE_SCALED
        self.number_of_tiles_width = int(2 * self.width / self.tile_size)
        self.number_of_tiles_height = int(2 * self.height / self.tile_size)
        self.map_objects = []
        self.map_grid = []
        self.pokemon_found_list = []
        self.collision_path = collision_path
        self.name = name
        self.warp = warp

    # draw the game_map
    def draw(self, screen, draw_area) -> None:
        screen.blit(self.scaled, (0, 0), area=draw_area.update_rect())

    # Load the map file into the field map_grid
    def load_map_array(self) -> None:
        with open(os.path.join(config.map_collision, self.collision_path)) as f:
            line_array = f.read().splitlines()
            f.close()
        for line in line_array:
            line_array = []
            for char in line:
                line_array.append(char)
            self.map_grid.append(line_array)

    def handle_grass_event(self):
        random_number = random.random()
        if random_number < config.FIND_POKEMON_CHANCE_BOUND:
            # when we face a wild pokemon, play the animation
            self.animation_manager.add_animation(animation.BattleAnimation())
            # then create a battle
            new_battle = battle.WildBattle(self.animation_manager, self.player_trainer, self.pick_random_pokemon())
            # add it to the game_state_manager
            self.game.new_battle(new_battle)
            # then change the game_state
            self.game.request_state_change(config.GAME_STATE_BATTLE)
            # start the battle

    # pick a random pokemon from the pokemon list associated with
    def pick_random_pokemon(self) -> pokemon.Pokemon:
        returnable = random.choice(self.pokemon_list)
        print("vous venez de rencontrer un pokemon sauvage")
        print("le pokemon que vous venez de rencontrer est " + returnable.get_name())
        return returnable


