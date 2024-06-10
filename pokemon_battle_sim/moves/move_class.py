
class Move:
    def __init__(self, name: str, type, pp: int, power: int, accuracy: int, move_category: str, secondary_effect=None, crit_stage=0, priority=0) -> None:
        self.name = name
        self.type = type
        self.pp = pp
        self.accuracy = accuracy
        self.power = power
        self.move_category = move_category
        self.secondary_effect = secondary_effect
        self.crit_stage = crit_stage

    