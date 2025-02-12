from tkinter import *
from tkinter import ttk
import asyncio
from Objects import tenno
from commonattributes import Commonattributes
from commonmethods import Commonmethods

mainframe: Frame
user: tenno.Tenno
user_loaded: tenno.Tenno

class Startpage:
    def __init__(self, parent, common_attributes_object: Commonattributes):
        self.common_methods_object = Commonmethods(common_attributes_object)
        self.common_attributes_object = common_attributes_object
        self.mainframe = ttk.Frame(parent, padding = "3 3 12 12")
        self.mainframe.grid(column = 0, row = 0, sticky = (N, E, S, W))
        self.user = None
        self.user_loaded = None
        self.user_name = StringVar()
        self.user_mr = StringVar()

        self.pageSetUp()


    def pageSetUp(self):
        ttk.Label(self.mainframe, text = "Start Page!").grid(column = 2, row = 1, sticky = N)

        from Pages.pageone import Pageone
        from Pages.pagetwo import Pagetwo
        from Pages.homepage import Homepage

        ttk.Button(self.mainframe, text = "Go to Page One", command = lambda: self.common_methods_object.changePage(
            self.common_attributes_object.pages[Pageone])).grid(column = 1, row = 2, sticky = W)
        ttk.Button(self.mainframe, text = "Go to Home Page", command = lambda: self.common_methods_object.changePage(
            self.common_attributes_object.pages[Homepage])).grid(column = 2, row = 2, sticky = S)
        ttk.Button(self.mainframe, text = "Go to Page Two", command = lambda: self.common_methods_object.changePage(
            self.common_attributes_object.pages[Pagetwo])).grid(column = 3, row = 2, sticky = E)

        ttk.Label(self.mainframe, text = "Create a Warframe").grid(column = 2, row = 3, sticky = N)

        warframe_name = StringVar()
        warframe_entry = ttk.Entry(self.mainframe, width = 10, textvariable = warframe_name)
        warframe_entry.grid(column = 1, row = 4, sticky = W)
        warframe_name_label = ttk.Label(self.mainframe)
        warframe_name_label.grid(column = 3, row = 4, sticky = E)

        ttk.Button(self.mainframe, text = "Set Warframe Name", command = lambda: self.updateLabel(warframe_name,
            warframe_name_label)).grid(column = 2, row = 4, sticky = N)

        warframe_abilities_label = ttk.Label(self.mainframe)
        warframe_abilities_label.grid(column = 2, row = 5, sticky = W)

        ttk.Button(self.mainframe, text = 'Test Find', command = lambda: asyncio.run(
            self.common_methods_object.parseTest())).grid(column = 1, row = 6, sticky = W)

        ttk.Button(self.mainframe, text = 'Create User', command = lambda: self.createTenno()).grid(
            column = 1, row = 7, sticky = W)

        mr_value = StringVar()
        mr_entry = ttk.Entry(self.mainframe, width = 10, textvariable = mr_value)
        mr_entry.grid(column = 3, row = 7, sticky = E)

        ttk.Button(self.mainframe, text = 'Update MR', command = lambda: self.updateMR(mr_value, self.user)).grid(
            column = 2, row = 7, sticky = N)

        ttk.Button(self.mainframe, text = 'Create File', command = lambda: self.common_methods_object.writeFile(
            self.user)).grid(column = 1, row = 8, sticky = W)

        ttk.Button(self.mainframe, text = 'Read File', command = lambda: self.openUserFile()).grid(
            column = 2, row = 8, sticky = N)

        ttk.Button(self.mainframe, text= 'Delete File', command =
        lambda: self.common_methods_object.deleteFile()).grid(column = 3, row = 8, sticky = E)

        user_name_label = ttk.Label(self.mainframe, textvariable = self.user_name)
        user_name_label.grid(column = 1, row = 9, sticky = W)
        user_mr_label = ttk.Label(self.mainframe, textvariable = self.user_mr)
        user_mr_label.grid(column = 2, row = 9, sticky = N)

        for child in self.mainframe.winfo_children():
            child.grid_configure(padx = 5, pady = 5)

    def updateLabel(self, stringvar: StringVar, label: Label):
        label.config(text = stringvar.get())

    def getAbilities(self, stringvar: StringVar, label: Label):
        pass

    def createTenno(self):
        self.user = tenno.Tenno('Zachie')

    def updateMR(self, mr: StringVar, user: tenno.Tenno):
        user.setMR(int(mr.get()))

    def openUserFile(self):
        self.user_loaded = self.common_methods_object.loadFile()
        self.user_name.set(self.user_loaded.name)
        self.user_mr.set(self.user_loaded.mastery_rank)