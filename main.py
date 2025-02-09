from tkinter import *
from tkinter import ttk
from commonattributes import Commonattributes
from commonmethods import Commonmethods
from Pages.startpage import Startpage
from Pages.pageone import Pageone
from Pages.pagetwo import Pagetwo



def main():
    common_attributes_object = Commonattributes()
    common_methods_object = Commonmethods(common_attributes_object)
    window = Tk()
    window.title('Warframe Project Manager')
    window.columnconfigure(0, weight = 1)
    window.rowconfigure(0, weight = 1)

    common_methods_object.readyPages(window)
    common_methods_object.changePage(common_attributes_object.pages[Startpage])

    window.mainloop()

if __name__ == '__main__':
    main()