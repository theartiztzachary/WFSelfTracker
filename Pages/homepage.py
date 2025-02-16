from tkinter import *
from tkinter import ttk, messagebox
from Objects import tenno, warframe
from commonattributes import Commonattributes
from commonmethods import Commonmethods

mainfraime: Frame
parent: Tk
loaded_tenno: tenno.Tenno
error_present: bool
error_message: StringVar

class Homepage:
    def __init__(self, page_parent: Tk, common_attributes_object: Commonattributes):
        self.loaded_tenno = None
        self.error_present = False
        self.error_message = StringVar()
        self.parent = page_parent
        self.common_methods_object = Commonmethods(common_attributes_object)
        self.common_attributes_object = common_attributes_object
        self.mainframe = ttk.Frame(self.parent, padding = "3 3 12 12")
        self.mainframe.grid(column = 0, row = 0, sticky = (N, E, S, W))

        self.pageSetUp()

    def pageSetUp(self):
        self.parent.title('Warframe Project Manager - Homepage')
        self.loaded_tenno = self.common_methods_object.loadFile()
        if self.loaded_tenno is None:
            self.newUserPage()
        else:
            self.returningUserPage()

    def newUserPage(self):
        tenno_name = StringVar()
        name_label = ttk.Label(self.mainframe, text = "What is your name?")
        name_label.grid(column = 1, row = 2, sticky = W)
        name_entry = ttk.Entry(self.mainframe, width = 10, textvariable = tenno_name)
        name_entry.grid(column = 1, row = 3, sticky = W)

        # tenno_icon = image
        # label for select a glyph
        # glyph selection

        tenno_mr = StringVar()
        ttk.Label(self.mainframe, text = "What is your Mastery Rank? Please input a numerical value. "
            "LR1 is considered 31, LR2 is considered 32, etc.").grid(column = 3, row = 2, sticky = E)
        ttk.Entry(self.mainframe, width = 10, textvariable = tenno_mr).grid(column = 3, row = 3, sticky = E)

        ttk.Button(self.mainframe, text = "Create Profile", command = lambda: self.createTenno(
            tenno_name, tenno_mr)).grid(column = 2, row = 5, sticky = N)

        ttk.Label(self.mainframe, textvariable = self.error_message).grid(column = 3, row = 5, sticky = W)

        for child in self.mainframe.winfo_children():
            child.grid_configure(padx = 5, pady = 5)

    def returningUserPage(self):
        # put the glyph somewhere
        ttk.Label(self.mainframe, text = "Welcome back " + self.loaded_tenno.name + "!").grid(column = 2, row = 1,
            sticky = N)

        ttk.Button(self.mainframe, text = "Create New Project",
                   command = lambda: self.createNewProject(self.loaded_tenno)).grid(column = 1, row = 3, sticky = W)
        ttk.Button(self.mainframe, text = "Create New Item", command = lambda: self.createNewItem()
                   ).grid(column = 3, row = 3, sticky = E)

        sub_frame_projects = ttk.Frame(self.mainframe, padding = "3 3 12 12")
        sub_frame_projects.grid(column = 0, row = 4, sticky = (N, E, S, W))


        sub_frame_items = ttk.Frame(self.mainframe, padding = "3 3 12 12")
        sub_frame_items.grid(column = 2, row = 4, sticky = (N, E, S, W))

    def createTenno(self, tenno_name: StringVar, mastery_rank: StringVar):
        t_name = str(tenno_name.get())
        try:
            t_rank = int(mastery_rank.get())
        except ValueError:
            self.error_present = True
            self.error_message.set("Please enter a numerical value for your Mastery Rank.")
            return

        self.loaded_tenno = tenno.Tenno(t_name, t_rank)
        self.error_present = False
        self.error_message = None

        self.common_methods_object.cleanPage(self.mainframe)
        self.returningUserPage()

    def createNewProject(self, user_tenno: tenno.Tenno):
        user_tenno.id_number += 1

        popup = Tk()
        popup.title("Create A New Project")
        popup_mainframe = ttk.Frame(popup, padding = "3 3 12 12")
        popup_mainframe.grid(column = 0, row = 0, sticky = (N, S, W, E))
        type_dropdown = ttk.Combobox(popup_mainframe, values = ['Select A Project Type', 'Warframe', 'Weapon',
            'Companion'], state = 'readonly')
        type_dropdown.grid(column = 1, row = 3, sticky = W)
        sub_type_dropdown = ttk.Combobox(popup_mainframe, values = ['Select One'], state = 'readonly')
        sub_type_dropdown.grid(column = 2, row = 3, sticky = N)
        type_dropdown.bind('<<ComboboxSelected>>', lambda event: self.updateDropdown(triggering_dropdown = type_dropdown,
            changing_dropdown = sub_type_dropdown, event = event))
        ttk.Button(popup, text = "Create Project", command = lambda: self.addProject(type_dropdown, sub_type_dropdown,
            self.loaded_tenno)).grid(column = 3, row = 3, sticky = E)

    def addProject(self, type_dropdown: ttk.Combobox, sub_type_dropdown: ttk.Combobox, user_tenno: tenno.Tenno):
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

            user_tenno.id_number += 1
            new_warframe = warframe.Warframe(sub_type_dropdown.get())
            user_tenno.projects.update({user_tenno.id_number: new_warframe})

        else:
            messagebox.showinfo(
                title = 'Alert',
                message = 'That type of project has not been implemented yet.'
            )

    def createNewItem(self):
        self.id_number += 1
        item_object: object

        popup = Tk()
        popup.title("Create A New Item")

    def updateDropdown(self, event, changing_dropdown: ttk.Combobox, triggering_dropdown: ttk.Combobox):
        type_selection = triggering_dropdown.get()
        if type_selection == 'Select One':
            return
        elif type_selection == 'Warframe':
            changing_dropdown['values'] = self.common_attributes_object.warframe_list
        elif type_selection == 'Weapon':
            changing_dropdown['values'] = ['Not Implemented Yet']
        elif type_selection == 'Companion':
            changing_dropdown['values'] = ['Not Implemented Yet']

