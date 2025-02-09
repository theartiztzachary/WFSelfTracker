from tkinter import *
from tkinter import ttk
from commonattributes import Commonattributes
from commonmethods import Commonmethods

mainframe: Frame

class Startpage:
    def __init__(self, parent, common_attributes_object: Commonattributes):
        common_methods_object = Commonmethods(common_attributes_object)
        self.mainframe = ttk.Frame(parent, padding = "3 3 12 12")
        self.mainframe.grid(column = 0, row = 0, sticky = (N, E, S, W))
        ttk.Label(self.mainframe, text = "Start Page!").grid(column = 2, row = 1, sticky = N)

        from Pages.pageone import Pageone
        from Pages.pagetwo import Pagetwo

        ttk.Button(self.mainframe, text = "Go to Page One", command = lambda: common_methods_object.changePage(
            common_attributes_object.pages[Pageone])).grid(column = 1, row = 2, sticky = W)
        ttk.Button(self.mainframe, text = "Go to Page Two", command = lambda: common_methods_object.changePage(
            common_attributes_object.pages[Pagetwo])).grid(column = 3, row = 2, sticky = W)

        for child in self.mainframe.winfo_children():
            child.grid_configure(padx = 5, pady = 5)