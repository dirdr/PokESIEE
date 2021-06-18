import text_box
import selection_box
import config


class BattleEventQueue:

    def __init__(self) -> None:
        self.event_queue = []

    def get_current_event(self):
        if not len(self.event_queue) == 0:
            return self.event_queue[len(self.event_queue) - 1]

    def pop_current_event(self) -> None:
        self.event_queue.pop()

    def have_event(self) -> bool:
        return not len(self.event_queue) == 0

    def add_event(self, animation) -> None:
        self.event_queue.insert(0, animation)

class Event:

    def __init__(self):
        self.user_input = ''
        self.isFinished = False


class BattleEventOptionBoxAndTextBox(Event):

    def __init__(self, player):
        super(BattleEventOptionBoxAndTextBox, self).__init__()
        self.current_text_box = text_box.TextBox(["Que va va faire ", player.get_current_pokemon().get_name()])
        self.current_option_box = selection_box.SelectionBox(int(config.SCREEN_WIDTH / 2) + 30,
                                                             int(config.SCREEN_WIDTH / 2) - 30,
                                                             ["Attaque", "Pokémon", "Capture", "Fuite"], 4)

    def update(self):
        if self.current_option_box.user_have_choose:
            self.isFinished = True
        self.current_option_box.update()

    def get_user_input(self) -> str:
        return self.current_option_box.find_user_input()

    def draw(self, surface):
        self.current_text_box.draw(surface)
        self.current_option_box.draw(surface)


class ChooseAttack(Event):

    def __init__(self, pokemon):
        super(ChooseAttack, self).__init__()
        self.current_option_box = selection_box.SelectionBox(int(config.SCREEN_WIDTH / 2) + 30,
                                                             int(config.SCREEN_WIDTH / 2) - 30, pokemon.moves, len(pokemon.moves))
