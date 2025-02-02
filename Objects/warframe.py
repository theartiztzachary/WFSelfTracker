import wfability, mod, modslot, arcane, commonattributes

class Warframe:

    max_level = 30

    name: str
    #icon
    is_prime: bool
    base_stats: dict
    secondary_stats: dict
    first_ability: wfability
    second_ability: wfability
    third_ability: wfability
    fourth_ability: wfability
    has_helminth: bool
    helminth_ability: wfability
    helminth_slot: int
    arcane_one: arcane
    arcane_two: arcane
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

    def __init__(self, name: str, is_prime: bool):
        self.name = name
        self.is_prime = is_prime

    def __int__(self):
        pass

    def __str__(self):
        return self.name