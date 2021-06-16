from battle import Battle


class GameStateManager:

    def __init__(self, init) -> None:
        self.current_state = init
        self.next_state = init
        self.current_battle = Battle

    def change_state(self, state) -> None:
        self.next_state = state

    def update_state(self) -> None:
        self.current_state = self.next_state

    def get_current_state(self) -> int:
        return self.current_state

    def new_battle(self, battle: Battle) -> None:
        self.current_battle = battle
