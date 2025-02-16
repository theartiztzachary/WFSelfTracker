from Objects import warframe, weapon
from tkinter import *
from tkinter import ttk, messagebox
from commonattributes import Commonattributes
from commonmethods import Commonmethods

class Tenno:

    name: str
    #profile_icon
    mastery_rank: int
    built_items: dict #since you can have multiple of the same item, each item will have a unique ID
    projects: dict #techincally same as items, so they can be cleanly moved there
    id_number: int

    def __init__(self, name, common_attributes_object: Commonattributes):
        self.name = name
        self.common_methods_object = Commonmethods(common_attributes_object)
        self.common_attributes_object = common_attributes_object
        self.id_number = 0

    def setMR(self, mastery_rank: int):
        self.mastery_rank = mastery_rank

    def createNewItem(self):
        self.id_number += 1
        item_object: object

        popup = Tk()
        popup.title("Create A New Item")

    def createNewProject(self):
        self.id_number += 1

        popup = Tk()
        popup.title("Create A New Project")
        popup_mainframe = ttk.Frame(popup, padding = "3 3 12 12")
        popup_mainframe.grid(column = 0, row = 0, sticky = (N, S, W, E))
        type_dropdown = ttk.Combobox(popup_mainframe, values = ['Select A Project Type', 'Warframe', 'Weapon',
            'Companion'], state = 'readonly')
        type_dropdown.grid(column = 1, row = 3, sticky = W)
        sub_type_dropdown = ttk.Combobox(popup_mainframe, values = ['Select One'], state = 'readonly')
        sub_type_dropdown.grid(column = 2, row = 3, sticky = N)
        type_dropdown.bind('<<ComboboxSelected>>', self.updateDropdown(sub_type_dropdown, type_dropdown))
        ttk.Button(popup, text = "Create Project")

    def addProject(self, type_dropdown: ttk.Combobox, sub_type_dropdown: ttk.Combobox):
        if type_dropdown.get() == 'Select A Project Type':
            return
        elif type_dropdown.get() == 'Warframe':
            selected_frame = sub_type_dropdown.get()
            if selected_frame == 'Select One':
                messagebox.showinfo(
                    title = "Alert",
                    message = "Please select a Warframe."
                )
                return

            new_warframe = warframe.Warframe(sub_type_dropdown.get())
            self.projects.update({self.id_number: new_warframe})
        else:
            messagebox.showinfo(
                title = 'Alert',
                message = 'That type of project has not been implemented yet.'
            )

    def moveProjectToItems(self, project_id_number: int):
        self.built_items.update({project_id_number: self.projects[project_id_number]})
        self.projects.pop(project_id_number)

    def deleteItem(self, item_id_number: int):
        self.built_items.pop(item_id_number)

    def deleteProject(self, project_id_number: int):
        self.projects.pop(project_id_number)

    def updateDropdown(self, changing_dropdown: ttk.Combobox, triggering_dropdown: ttk.Combobox):
        type_selection = triggering_dropdown.get()
        if type_selection == 'Select One':
            return
        elif type_selection == 'Warframe':
            changing_dropdown['values'] = self.common_attributes_object.warframe_list
        elif type_selection == 'Weapon':
            changing_dropdown['values'] = ['Not Implemented Yet']
        elif type_selection == 'Companion':
            changing_dropdown['values'] = ['Not Implemented Yet']

    def __str__(self):
        return self.name