class Tenno:

    name: str
    #profile_icon
    mastery_rank: int
    built_items: dict #since you can have multiple of the same item, each item will have a unique ID
    projects: dict #techincally same as items, so they can be cleanly moved there
    id_number: int

    def __init__(self, name, mastery_rank):
        self.name = name
        self.projects = {}
        self.build_items = {}
        self.id_number = 0

    def moveProjectToItems(self, project_id_number: int):
        self.built_items.update({project_id_number: self.projects[project_id_number]})
        self.projects.pop(project_id_number)

    def deleteItem(self, item_id_number: int):
        self.built_items.pop(item_id_number)

    def deleteProject(self, project_id_number: int):
        self.projects.pop(project_id_number)

    def __str__(self):
        return self.name