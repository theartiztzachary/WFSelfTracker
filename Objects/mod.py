class Mod:

    name: str
    #icon
    polarity: str
    capacity: int
    half_capacity: int
    increased_capacity: int
    is_aura: bool
    is_riven: bool
    is_exilus: bool
    is_augment: bool
    mr_required: int
    #what the mod *does* <- this will be the tricky part lol

    def __init__(self, name: str, polarity: str, capacity: int, is_aura: bool, is_riven: bool, is_exilus: bool,
                 is_augment: bool, mr_required: int):
        self.name = name
        self.polarity = polarity
        self.capacity = capacity

        if (capacity % 2) == 0:
            self.half_capacity = int(capacity / 2)
        elif (capacity % 2) == 1:
            self.half_capacity = int(capacity / 2) + 1

        quarter_capacity: float
        quarter_capacity = capacity / 4
        qcfstr = f'{quarter_capacity:.2f}'
        qcdecimal = int(qcfstr.split(".")[1])
        if qcdecimal == 5 or qcdecimal == 50:
            qcfinal = round(quarter_capacity)
            qcfinal += 1
            self.increased_capacity = self.capacity + qcfinal
        elif qcdecimal > 50:
            qcfinal = round(quarter_capacity)
            self.increased_capacity = self.capacity + qcfinal
        elif qcdecimal < 50:
            qcfinal = round(quarter_capacity)
            self.increased_capacity = self.capacity + qcfinal

        self.is_aura = is_aura
        self.is_riven = is_riven
        self.is_exilus = is_exilus
        self.is_augment = is_augment

        if is_riven:
            self.mr_required = mr_required
        else:
            self.mr_required = 0


        self.setModEffects(name)

    def __int__(self):
        pass

    def setModEffects(self, name):
        pass

    def applyModEffects(self):
        pass

    def __str__(self):
        return self.name