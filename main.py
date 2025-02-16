import faulthandler, subprocess, os
from tkinter import *
from tkinter import ttk
from commonattributes import Commonattributes
from commonmethods import Commonmethods
from Pages.startpage import Startpage

def main():
    faulthandler.enable() # : ^ )

    # create a Commonattributes object, responsible for holding global variables THIS SPECIFIC ONE MUST BE PASSED
    # AROUND IF NEEDED
    common_attributes_object = Commonattributes()
    # create a Commonmethods object, responsible for holding common methods, this specific one doesn't need to be
    # passed around
    common_methods_object = Commonmethods(common_attributes_object)

    # creates the main window
    window = Tk()
    window.title('Warframe Project Manager')
    window.columnconfigure(0, weight = 1)
    window.rowconfigure(0, weight = 1)

    # initiates the pages and sets the starting page
    common_methods_object.readyPages(window)
    common_methods_object.changePage(common_attributes_object.pages[Startpage])

    # essentially "starts" the app
    window.mainloop()

# i forget what this does but it's important lmao
if __name__ == '__main__':
    main()