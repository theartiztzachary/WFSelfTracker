from tkinter import *
from tkinter import ttk
from commonattributes import Commonattributes

class Commonmethods:

    common_attributes_object: Commonattributes

    def __init__(self, common_attributes_object: Commonattributes):
        self.common_attributes_object = common_attributes_object
        pass

    def readyPages(self, parent):
        from Pages.startpage import Startpage
        from Pages.pageone import Pageone
        from Pages.pagetwo import Pagetwo
        for P in (Startpage, Pageone, Pagetwo):
            page = P(parent, self.common_attributes_object)
            self.common_attributes_object.pages.update({P : page})

    def changePage(self, page):
        page.mainframe.tkraise()