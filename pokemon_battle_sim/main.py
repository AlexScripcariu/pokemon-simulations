from moves.move_lib import moves
from natures.nature_class import *
from abilities.ability_class import *
from type_content.type_class import *
from type_content.type_lib import *
from abilities.ability_lib import *
from pokemon.pokemon_class import Pokemon

haxorus = Pokemon("Haxorus", [dragon_type, None], neutral_ability, 
                  50, 1.8, 105.5, [31, 31, 31, 0, 31, 31], [0, 252, 4, 0, 0, 252],
                  [76, 147, 90, 60, 70, 97], 50, Adamant, 
                  moveset=[moves["Swords Dance"], moves["Outrage"], moves["Dragon Claw"], moves["Dragon Tail"]])

articuno = Pokemon("Articuno", [ice_type, flying_type], neutral_ability, None, 1.7,
                   55.4, [31, 31, 31, 31, 31, 31], [0, 0, 252, 0, 252, 4],
                   [90, 85, 100, 95, 125, 85], 50, Bold, 
                   moveset=[moves["Blizzard"], moves["Hurricane"], moves["Ice Beam"], moves["Freeze-Dry"]])

def tailwind_check(user: Pokemon, isTailwindUser):
    if isTailwindUser["active"] and isTailwindUser["Turns Left"] != 0 and not isTailwindUser['doubled']:
        user.speed *= 2
        if isTailwindUser["active"] and isTailwindUser["Turns Left"] == 0:
            user.speed /= 2
            isTailwindUser["active"] = False
            isTailwindUser["doubled"] = False

        isTailwindUser["Turns Left"] -= 1

def trick_room_speed(user: Pokemon):
    resultant_speed = (10000 - user.speed) % 8192
    user.speed = resultant_speed

def trick_room_check(user: Pokemon, target: Pokemon, isTrickRoom: dict):
    if isTrickRoom['active'] and isTrickRoom['Turns left'] != 0 and not isTrickRoom['isModified']:
        trick_room_speed(user)
        trick_room_speed(target)


def calculate_speed_pre_round(user: Pokemon, target: Pokemon, isTrickRoom, isTailwindUser, isTailwindTarget):
    tailwind_check(user, isTailwindUser)
    tailwind_check(target, isTailwindTarget)

    
    if user.held_item.name == "Choice Scarf":
        user.speed *= 1.5
    elif target.held_item.name == "Choice Scarf":
        target.speed *= 1.5
    
    if user.speed >= target.speed:
        return [user, target, "Same"]
    elif target.speed > user.speed:
        return [target, user]
    
def turn(user: Pokemon, target: Pokemon, speed_queue: list):
    user_move = None
    target_move = None

    if user_move != None and user.held_item.name != "Choice Scarf": #  TODO rename speed stat by creating a 'modded speed' stat instead to use for speed calcs
        pass

def game(user, target):
    turns = 0
    terrain = []
    weather = []
    isTrickRoom = {'active': False, 'Turns Left': 0, 'isModified': False}
    isGravity = {'active': False, 'Turns Left': 0}
    isTailwindUser = {'active': False, 'Turns Left': 0, 'doubled': False}
    isTailwindTarget = {'active': False, 'Turns Left': 0, 'doubled': False}
    in_proccess_moves_user = {} # format -> 'Solar Beam': 1    <- 1 = amount of turns until used aka. 0 = using on this turn
    in_proccess_moves_target = {}

    speed_queue = calculate_speed_pre_round(user, target, isTrickRoom, isTailwindUser, isTailwindTarget)



