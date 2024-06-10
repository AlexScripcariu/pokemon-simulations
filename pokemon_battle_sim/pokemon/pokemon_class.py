from type_content.type_class import *
from type_content.type_lib import *
from natures.nature_class import *
from math import floor
from random import randint
from moves.move_lib import Move

tags = ["HP", "Atk", "Def", "SpA", "SpD", "Spe"]

class Pokemon:
    def __init__(self, name, type, ability, gender_ratio, height, weight, iv=[0,0,0,0,0,0], ev=[0,0,0,0,0,0], bst=[0,0,0,0,0,0], level=50, nature=Hardy, held_item=None, status="Healthy", moveset=[None, None, None, None]) -> None:
        self.name = name
        self.types = type
        self.type1 = type[0]
        self.type2 = type[1]
        self.ability = ability
        self.gender_ratio = gender_ratio # chance to be a male
        self.height = height
        self.weight = weight
        self.level = level
        self.held_item = held_item
        self.bst = bst
        self.bst_hp = bst[0]
        self.bst_attack = bst[1]
        self.bst_defense = bst[2]
        self.bst_special_attack = bst[3]
        self.bst_special_defense = bst[4]
        self.bst_speed = bst[5]
        self.iv = iv
        self.iv_hp = iv[0]
        self.iv_attack = iv[1]
        self.iv_defense = iv[2]
        self.iv_special_attack = iv[3]
        self.iv_special_defense = iv[4]
        self.iv_speed = iv[5]
        self.ev = ev
        self.ev_hp = ev[0]
        self.ev_attack = ev[1]
        self.ev_defense = ev[2]
        self.ev_special_attack = ev[3]
        self.ev_special_defense = ev[4]
        self.ev_speed = ev[5]
        self.nature = nature
        self.hidden_accuracy = 3/3
        self.hidden_evasion = 3/3
        self.attack_stage = 2/2
        self.defense_stage = 2/2
        self.special_attack_stage = 2/2
        self.special_defense_stage = 2/2
        self.speed_stage = 2/2  
        self.hp = self.calculate_hp()
        self.max_hp = self.calculate_hp()
        self.attack = self.calculate_stat("attack") 
        self.defense = self.calculate_stat("defense") 
        self.special_attack = self.calculate_stat("special_attack")
        self.special_defense = self.calculate_stat("special_defense")
        self.speed = self.calculate_stat("speed")
        self.status = status
        self.poison_counter = 0
        self.moveset = moveset
        self.move1 = moveset[0]
        self.move2 = moveset[1]
        self.move3 = moveset[2]
        self.move4 = moveset[3]
        
    
    def calculate_hp(self):
        return floor(0.01 * (2 * self.bst_hp + self.iv_hp + floor(0.25 * self.ev_hp)) * self.level) + self.level + 10


    def calculate_stat(self, stat):
        curr_bst = 0
        curr_iv = 0
        curr_ev = 0
        match stat:
            case "attack":
                curr_bst, curr_iv, curr_ev = self.bst_attack, self.iv_attack, self.ev_attack
            case "defense":
                curr_bst, curr_iv, curr_ev = self.bst_defense, self.iv_defense, self.ev_defense
            case "special_attack":
                curr_bst, curr_iv, curr_ev = self.bst_special_attack, self.iv_special_attack, self.ev_special_attack
            case "special_defense":
                curr_bst, curr_iv, curr_ev = self.bst_special_defense, self.iv_special_defense, self.ev_special_defense
            case "speed":
                curr_bst, curr_iv, curr_ev = self.bst_speed, self.iv_speed, self.ev_speed
        
        result = floor(0.01 * (2 * curr_bst + curr_iv + floor(0.25 * curr_ev)) * self.level) + 5

        if self.nature.boosted_stat == stat:
            return floor(result * 1.1)
        elif self.nature.reduced_stat == stat:
            return floor(result * 0.9)
        else:
            return result
        

    def __str__(self) -> str:
        evs = ""
            
        for i in range(len(self.ev)):
            if self.ev[i] == 0:
                continue
            else:
                evs += f" {self.ev[i]} {tags[i]} /"

        evs = evs[:-2]

        return f"{self.name} @ {self.held_item}\nAbility: {self.ability.name}\nLevel: {self.level}\nEVs:{evs}\n{self.nature.name} Nature\n- {self.move1.name}\n- {self.move2.name}\n- {self.move3.name}\n- {self.move4.name}"

    def calculate_crit(self, move, target):
        crit = 1

        crit_rng = randint(1, 24)

        if move.crit_stage == 0 and crit_rng == 1:
            crit = 1.5
        elif move.crit_stage == 1 and crit_rng <= 3:
            crit = 1.5
        elif move.crit_stage == 2 and crit_rng <= 12:
            crit = 1.5
        elif move.crit_stage >= 3:
            crit = 1.5

        if target.ability.name == "Battle Armor" or target.ability.name == "Shell Armor":
            crit = 1
        
        if (target.status == "Poisoned" or target.status == "Badly Poisoned") and self.ability.name == "Merciless":
            crit = 1.5 
        
        return crit

    def calculate_stab(self, move, target):
        stab = 1
        for typ in self.types: 
            if typ is None:
                continue
            elif typ.name == move.type.name:
                stab = 1.5
                if self.ability.name == "Adaptability":
                    stab = 2
        
        return stab

    def calculate_type_effectiveness(self, move, target):
        type_effectiveness = 1
        for typ in target.types:
            if typ is None:
                continue
            if type(move.type) in typ.weaknesses:
                type_effectiveness *= 2
            elif type(move.type) in typ.resistances:
                if move.name == "Freeze-Dry" and typ.name == "Water":
                    type_effectiveness *= 2
                else:
                    type_effectiveness *= 0.5
            elif move.type in typ.immunities:
                if target.typ.name == "Flying" and target.held_item.name == "Iron Ball":
                    type_effectiveness *= 1
                elif target.held_item.name == "Ring Target":
                    type_effectiveness *= 1
                if self.ability.name == "Scrappy" and (move.type.name == "Normal" or move.type.name == "Fighting"):
                    type_effectiveness *= 1
                else:
                    type_effectiveness *= 0
                #TODO implement thousand arrows, foresight, odor sleuth, miracle eye, add flying press, strong winds, tar shot

        return type_effectiveness


    def calculate_burn(self, move):
        burn = 1
        if self.status == "Burned" and move.move_category == "Physical":
            burn = 0.5
        return burn

    def calculate_damage(self, move,target):
        if move.move_category == "Status":
            return
        
        attack_stat = 0
        defense_stat = 0

        if move.move_category == "Physical":
            attack_stat = self.attack * self.attack_stage
            defense_stat = target.defense * target.defense_stage
        elif move.move_category == "Special":
            attack_stat = self.special_attack * self.special_attack_stage
            defense_stat = target.special_defense * target.special_defense_stage
        
        parental_bond = 1
        weather = 1
        glaive_rush = 1
        crit = self.calculate_crit(move, target)
        rng_multiplier = randint(85, 100) / 100
        stab_bonus = self.calculate_stab(move, target)
        type_effectiveness = self.calculate_type_effectiveness(move, target)
        burn = self.calculate_burn(move)
        other_effect = 1    # TODO add the effects in

        

        # calculate_damage = ((2 * self.level / 5 + 2) * move.power * (attack_stat / defense_stat)/ 50 + 2) * parental_bond * weather * glaive_rush * crit * rng_multiplier * stab_bonus * type_effectiveness * burn * other_effect
        
        return int(floor(floor(((2 * self.level / 5 + 2) * move.power * (attack_stat / defense_stat) / 50 + 2) * parental_bond * weather * glaive_rush * crit) * rng_multiplier) * stab_bonus * type_effectiveness * burn * other_effect)

    def use_status_move(self, move: Move):
        move.secondary_effect(self)

    def clone(self):
        return Pokemon(self.name,
                       self.types,
                       self.ability,
                       self.gender_ratio,
                       self.height,
                       self.weight,
                       self.iv,
                       self.ev,
                       self.bst,
                       self.level,
                       self.nature,
                       self.held_item,
                       self.status,
                       self.moveset)
    
    def stage_change(self, stat, stages):
        stage_dict_base = {
            '-6': 2/8,
            '-5': 2/7,
            '-4': 2/6,
            '-3': 2/5,
            '-2': 2/4,
            '-1': 2/3,
            '0': 2/2,
            '1': 3/2,
            '2': 4/2,
            '3': 5/2,
            '4': 6/2,
            '5': 7/2,
            '6': 8/2
            }
        
        stage = 0
        stat_value = 0


        match stat:
            case 'attack':
                stat_value = self.attack_stage
            case 'defense':
                stat_value = self.defense_stage
            case 'special_attack':
                stat_value = self.special_attack_stage
            case 'special_defense':
                stat_value = self.special_defense_stage
            case 'speed':
                stat_value = self.speed_stage
        
        for key, value in stage_dict_base.items():
            if value == stat_value:
                stage = int(key)
        
        new_stage = stage + stages

        if new_stage < -6:
            new_stage = -6
        elif new_stage > 6:
            new_stage = 6

        match stat:
            case 'attack':
                self.attack_stage = stage_dict_base[str(new_stage)]
            case 'defense':
                self.defense_stage = stage_dict_base[str(new_stage)]
            case 'special_attack':
                self.special_attack_stage = stage_dict_base[str(new_stage)]
            case 'special_defense':
                self.special_defense_stage = stage_dict_base[str(new_stage)]
            case 'speed':
                self.speed_stage = stage_dict_base[str(new_stage)]

    def use_move(self, move: Move, target=None):
        rng_accuracy = randint(1, 100)
    
        if not (rng_accuracy > move.accuracy or move.accuracy != -1) or move.pp == 0: 
            # the move has missed if this is true so just return && same with if the pp is 0
            return

        if move.move_category == "Status":
            self.use_status_move(move)
        else:
            damage = self.calculate_damage(move, target)
            target.hp -= damage

        
        move.pp -= 1
        

    
    