from project.divers.base_diver import BaseDiver


class FreeDiver(BaseDiver):
    INITIAL_OXYGEN_LEVEL = 120

    def __init__(self, name: str):
        super().__init__(name, FreeDiver.INITIAL_OXYGEN_LEVEL)


    def miss(self, time_to_catch: int) -> None:  #TODO check time_to_catch

        oxygen_to_remove = int(0.60 * time_to_catch)
        if  (self.oxygen_level - oxygen_to_remove) < 0:
            self.oxygen_level = 0
        else:
            self.oxygen_level -= oxygen_to_remove

    def renew_oxy(self) -> None:
        self.oxygen_level = self.INITIAL_OXYGEN_LEVEL