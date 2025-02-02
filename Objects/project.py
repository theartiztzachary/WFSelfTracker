import warframe, operator, weapon, mod

class Project:

    id_number: int
    project_item: object

    def __init__(self, id_number: int, project_item: object):
        self.id_number = id_number
        self.project_item = project_item

    def __int__(self):
        pass

    def __str__(self):
        return self.project_item.name