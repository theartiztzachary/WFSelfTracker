from tkinter import *
from tkinter import ttk
from commonattributes import Commonattributes
from commonmethods import Commonmethods

mainfraime: Frame

class Homepage:
    def __init__(self, parent, common_attributes_object):
        self.common_methods_object = Commonmethods(common_attributes_object)
        self.common_attributes_object = common_attributes_object
        self.mainframe = ttk.Frame(parent, padding = "3 3 12 12")
        self.mainframe.grid(column = 0, row = 0, sticky = (N, E, S, W))

        self.pageSetUp()

    def pageSetUp(self):
        ttk.Label(self.mainframe, text = "Home Page").grid(column = 2, row = 1, sticky = N)
        pass

    def __init__(self):
        pass