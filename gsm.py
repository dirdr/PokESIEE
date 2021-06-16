from battle import Battle


class GameStateManager:

    def __init__(self, init):
        self.current_state = init
        self.next_state = init
        self.current_battle = Battle

    def change_state(self, state):
        self.next_state = state

    def update_state(self):
        self.current_state = self.next_state

    def get_current_state(self):
        return self.current_state

    def new_battle(self, battle: Battle):
        self.current_battle = battle
