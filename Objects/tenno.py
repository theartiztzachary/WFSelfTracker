from Objects import warframe, weapon

class Tenno:

    name: str
    #profile_icon
    mastery_rank: int
    built_items: dict #since you can have multiple of the same item, each item will have a unique ID
    projects: dict #techincally same as items, so they can be cleanly moved there
    id_number: int

    def __init__(self, name):
        self.name = name
        self.id_number = 0

    def __int__(self):
        pass

    def setMR(self, mastery_rank: int):
        self.mastery_rank = mastery_rank

    def createNewItem(self, item: str):
        self.id_number += 1
        item_object: object
        if item == "Warframe":
            item_object = warframe.Warframe()
        elif item == "Weapon":
            item_object = weapon.Weapon()
        self.built_items.update({self.id_number, item_object})

    def createNewProject(self, project_item: str):
        self.id_number += 1
        project_object: object
        if project_item == "Warframe":
            project_object = warframe.Warframe()
        elif project_item == "Weapon":
            project_object = weapon.Weapon()
        self.projects.update({self.id_number, project_object})


    def moveProjectToItems(self, project_id_number: int):
        self.built_items.update({project_id_number: self.projects[project_id_number]})
        self.projects.pop(project_id_number)

    def deleteItem(self, item_id_number: int):
        self.built_items.pop(item_id_number)

    def deleteProject(self, project_id_number: int):
        self.projects.pop(project_id_number)

    def __str__(self):
        return self.name