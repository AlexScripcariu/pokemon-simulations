
class NormalType:
    def __init__(self) -> None:
        self.name = "Normal"
        self.weaknesses = [FightingType]
        self.resistances = []
        self.immunities = [GhostType]


class FireType:
    def __init__(self) -> None:
        self.name = "Fire"
        self.weaknesses = [WaterType, GroundType, RockType]
        self.resistances = [FireType, GrassType, IceType, BugType, SteelType, FairyType]
        self.immunities = []


class WaterType:
    def __init__(self) -> None:
        self.name = "Water"
        self.weaknesses = [GrassType, ElectricType]
        self.resistances = [FireType, WaterType, IceType, SteelType]
        self.immunities = []


class GrassType:
    def __init__(self) -> None:
        self.name = "Grass"
        self.weaknesses = [FireType, IceType, PoisonType, FlyingType, BugType]
        self.resistances = [WaterType, GrassType, ElectricType, GroundType]
        self.immunities = []


class ElectricType:
    def __init__(self) -> None:
        self.name = "Electric"
        self.weaknesses = [GroundType]
        self.resistances = [ElectricType, FlyingType, SteelType]
        self.immunities = []


class IceType:
    def __init__(self) -> None:
        self.name = "Ice"
        self.weaknesses = [FireType, FightingType, RockType, SteelType]
        self.resistances = [IceType]
        self.immunities = []


class FightingType:
    def __init__(self) -> None:
        self.name = "Fighting"
        self.weaknesses = [FlyingType, PsychicType, FairyType]
        self.resistances = [BugType, RockType, DarkType]
        self.immunities = []


class PoisonType:
    def __init__(self) -> None:
        self.name = "Poison"
        self.weaknesses = [GroundType, PsychicType]
        self.resistances = [GrassType, FightingType, PoisonType, BugType, FairyType]
        self.immunities = []


class GroundType:
    def __init__(self) -> None:
        self.name = "Ground"
        self.weaknesses = [WaterType, GrassType, IceType]
        self.resistances = [PoisonType, RockType]
        self.immunities = [ElectricType]


class FlyingType:
    def __init__(self) -> None:
        self.name = "Flying"
        self.weaknesses = [ElectricType, IceType, RockType]
        self.resistances = [GrassType, FightingType, BugType]
        self.immunities = [GroundType]


class PsychicType:
    def __init__(self) -> None:
        self.name = "Psychic"
        self.weaknesses = [BugType, GhostType, DarkType]
        self.resistances = [FightingType, PsychicType]
        self.immunities = []

class BugType:
    def __init__(self) -> None:
        self.name = "Bug"
        self.weaknesses = [FireType, FlyingType, RockType]
        self.resistances = [GrassType, FightingType, GroundType]
        self.immunities = []


class RockType:
    def __init__(self) -> None:
        self.name = "Rock"
        self.weaknesses = [WaterType, GrassType, FightingType, GroundType, SteelType]
        self.resistances = [NormalType, FireType, PoisonType, FlyingType]
        self.immunities = []


class GhostType:
    def __init__(self) -> None:
        self.name = "Ghost"
        self.weaknesses = [GhostType, DarkType]
        self.resistances = [PoisonType, BugType]
        self.immunities = [NormalType, FightingType]


class DragonType:
    def __init__(self) -> None:
        self.name = "Dragon"
        self.weaknesses = [IceType, DragonType, FairyType]
        self.resistances = [FireType, WaterType, GrassType, ElectricType]
        self.immunities = []


class DarkType:
    def __init__(self) -> None:
        self.name = "Dark"
        self.weaknesses = [FightingType, BugType, FairyType]
        self.resistances = [GhostType, DarkType]
        self.immunities = [PsychicType]


class SteelType:
    def __init__(self) -> None:
        self.name = "Steel"
        self.weaknesses = [FireType, FightingType, GroundType]
        self.resistances = [NormalType, GrassType, IceType, FlyingType, PsychicType, BugType, RockType, DragonType, SteelType, FairyType]
        self.immunities = [PoisonType]


class FairyType:
    def __init__(self) -> None:
        self.name = "Fairy"
        self.weaknesses = [PoisonType, SteelType]
        self.resistances = [FightingType, BugType, DarkType]
        self.immunities = [DragonType]