from Objects import mod

class Modslot:

    position: str
    polarity: str
    drain: int
    current_mod: mod

    def __init__(self, position: str, polarity: str):
        self.position = position
        self.polarity = polarity
        self.drain = 0
        self.mod = None

    def __int__(self):
        pass

    def setMod(self, mod_inserted: mod):
        self.current_mod = mod_inserted

        if mod_inserted.is_aura:
            if self.polarity == self.current_mod.polarity or self.current_mod.polarity == 'Omni':
                self.drain = self.current_mod.capacity * 2
            elif self.polarity is None:
                self.drain = self.current_mod.capacity
            elif self.polarity != self.current_mod.polarity:
                fifth_capacity: float
                fifth_capacity = self.current_mod.capacity / 4
                fcfstr = f'{fifth_capacity:.2f}'
                fcdecimal = int(fcfstr.split(".")[1])
                if fcdecimal == 5 or fcdecimal == 50:
                    fcfinal = round(fifth_capacity)
                    fcfinal += 1
                    self.drain = self.current_mod.capacity + fcfinal
                elif fcdecimal > 50:
                    fcfinal = round(fifth_capacity)
                    self.drain = self.current_mod.capacity + fcfinal
                elif fcdecimal < 50:
                    fcfinal = round(fifth_capacity)
                    self.drain = self.current_mod.capacity + fcfinal

        else:
            if self.polarity == self.current_mod.polarity or self.current_mod.polarity == 'Omni':
                self.drain = self.current_mod.half_capacity
            elif self.polarity is None:
                self.drain = self.current_mod.capacity
            elif self.polarity != self.current_mod.polarity:
                self.drain = self.current_mod.increased_capacity

    def __str__(self):
        return self.position