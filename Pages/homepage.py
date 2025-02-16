from tkinter import *
from tkinter import ttk
from Objects import tenno
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
        self.error_message = None
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

        ttk.Label(self.mainframe, textvariable = self.error_message).grid(column = 4, row = 5, sticky = W)

        for child in self.mainframe.winfo_children():
            child.grid_configure(padx = 5, pady = 5)

    def returningUserPage(self):
        # put the glyph somewhere
        ttk.Label(self.mainframe, text = "Welcome back " + loaded_tenno.name + "!").grid(column = 2, row = 1,
            sticky = N)

        ttk.Button(self.mainframe, text = "Create New Project", command = lambda: self.loaded_tenno.createNewProject()
                   ).grid(column = 1, row = 3, sticky = W)
        ttk.Button(self.mainframe, text = "Create New Item", command = lambda: self.loaded_tenno.createNewItem()
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

        self.loaded_tenno = tenno.Tenno(t_name)
        self.loaded_tenno.setMR(t_rank)
        self.error_present = False
        self.error_message = None

        self.common_methods_object.cleanPage(self.mainframe)
        self.returningUserPage()