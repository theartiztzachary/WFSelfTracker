from Objects import wfability, modslot, arcane


class Warframe:

    name: str
    note_name = ''
    #icon
    base_stats: dict

    first_ability: wfability
    second_ability: wfability
    third_ability: wfability
    fourth_ability: wfability
    has_helminth: bool
    helminth_ability: wfability
    helminth_slot: int

    arcane_one: arcane
    arcane_two: arcane

    mod_capacity: int
    used_capacity: int
    has_potato: bool
    aura_slot: modslot
    exilus_slot: modslot
    mod_slot_1: modslot
    mod_slot_2: modslot
    mod_slot_3: modslot
    mod_slot_4: modslot
    mod_slot_5: modslot
    mod_slot_6: modslot
    mod_slot_7: modslot
    mod_slot_8: modslot

    blueprint_location: str
    neuroptics_location: str
    chassis_location: str
    systems_location: str

    def __init__(self, name: str):
        self.name = name

        self.setBaseStats(name)
        self.setAbilities(name)

        self.has_potato = False
        self.has_helminth = False

    def __int__(self):
        pass

    def setBaseStats(self, name: str):
        # API call using the Warframe's name (and whatever else I need) to pull base stats
        hit_points: int
        shield_max: int
        base_armor: int
        energy_max: int

        self.base_stats = {
            "Health" : hit_points,
            "Shields" : shield_max,
            "Armor": base_armor,
            "Energy" : energy_max,
            "Ability Strength" : 100,
            "Ability Duration" : 100,
            "Ability Range" : 100,
            "Ability Efficiency" : 100
        }

        if name == 'Harrow':
            overshields = self.base_stats["Shields"] + (1200 * 2)
            self.base_stats.update({"Overshield Cap" : overshields})
        else:
            overshields = self.base_stats["Shields"] + 1200
            self.base_stats.update({"Overshield Cap" : overshields})
            pass

        self.mod_capacity = 30
        self.used_capacity = 0

    def setAbilities(self, name: str):
        # API call using the Warframe's name to pull abilities
        pass

    def setHelminthAbility(self, name: str, position: int):
        # API call using the ability's name to pull information for that ability
        match position:
            case 1: #first ability
                self.helminth_slot = 1
                pass
            case 2: #second ability
                self.helminth_slot = 2
                pass
            case 3: #third ability
                self.helminth_slot = 3
                pass
            case 4: #fourth ability
                self.helminth_slot = 4
                pass

        self.has_helminth = True

    def removeHelminthAbility(self, position: int):
        # API call using the Warframe's name + ability position to reset the ability back to a regular ability
        pass

    def setArcane(self, name: str, position: int):
        # API call using the arcane's name to pull information for that arcane
        match position:
            case 1: # upper arcane
                pass
            case 2: # lower arcane
                pass

    def setMod(self, name: str, position: str, mod_type: str):
        # API call using the mod's name to pull information for that mod
        # build a mod object and then build a modslot object
        match position:
            case "Aura":
                # set to aura, mod_capacity += modslot.drain
                pass
            case "Exilus":
                # set to exilus, used_capacity += modslot.drain
                pass
            case "One":
                # set to position one, used_capacity += modslot.drain
                pass
            case "Two":
                # set position two, used_capacity += modslot.drain
                pass
            case "Three":
                # set position three, used_capacity += modslot.drain
                pass
            case "Four":
                # set position four, used_capacity += modslot.drain
                pass
            case "Five":
                # set position five, used_capacity += modslot.drain
                pass
            case "Six":
                # set position six, used_capacity += modslot.drain
                pass
            case "Seven":
                # set position seven, used_capacity += modslot.drain
                pass
            case "Eight":
                # set position eight, used_capacity += modslot.drain
                pass
        pass

    def applyPotato(self):
        self.has_potato = True
        self.mod_capacity += 30

    def __str__(self):
        return self.name