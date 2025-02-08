from tkinter import *
from tkinter import ttk

# for tkinter files, methods need to go towards the top (or otherwise defined before they're actually used
def calculate(*args):
    try:
        value = float(feet.get())
        meters.set(int(0.3048 * value * 10000.0  + 0.5)/10000.0)
    except ValueError:
        pass

root = Tk() # creates a Tk object (a window)
root.title("Feet to Meters") # gives that window a name

mainframe = ttk.Frame(root, padding="3 3 12 12") # creates a frame widget - not strictly "needed" but helps things look
# nice
mainframe.grid(column = 0, row = 0, sticky = (N, W, E, S)) # puts the frame in the window
# yes N/W/E/S is compass directions, tells where something should be anchored to

# tells the frame to expand to fill any extra space if the window is resized
root.columnconfigure(0, weight = 1)
root.rowconfigure(0, weight = 1)

feet = StringVar()
feet_entry = ttk.Entry(mainframe, width = 7, textvariable = feet) # the first parameter sets the parent of the widget
# textvariable parameter points to the variable and will automatically update it if it gets updated!
# only caveat is that these variables MUST be StringVar
feet_entry.grid(column = 2, row = 1, sticky = (W, E)) # actually places it in the "grid" of the window

meters = StringVar()
ttk.Label(mainframe, textvariable = meters).grid(column = 2, row = 2, sticky = (W, E))

ttk.Button(mainframe, text = "Calculate", command = calculate).grid(column = 3, row = 3, sticky = W)

ttk.Label(mainframe, text = "feet").grid(column = 3, row = 1, sticky = W)
ttk.Label(mainframe, text = "is equivalent to").grid(column = 1, row = 2, sticky = E)
ttk.Label(mainframe, text = "meters").grid(column = 3, row = 2, sticky = W)

for child in mainframe.winfo_children(): # goes through all the children of mainframe and adds some padding
    child.grid_configure(padx = 5, pady = 5)

feet_entry.focus() # tells Tk to start with this field in focus (ie already clicked when opened)
root.bind("<Return>", calculate) # allows the user to hit Enter on the keyboard to also get it to work!
root.mainloop() #enter the "event loop"

''' an example of the above code encapsulated into a class and then executed, since it is in a class the calculate
method can go wherever 
from tkinter import *
from tkinter import ttk

class FeetToMeters:

    def __init__(self, root):

        root.title("Feet to Meters")

        mainframe = ttk.Frame(root, padding="3 3 12 12")
        mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
        root.columnconfigure(0, weight=1)
        root.rowconfigure(0, weight=1)
       
        self.feet = StringVar()
        feet_entry = ttk.Entry(mainframe, width=7, textvariable=self.feet)
        feet_entry.grid(column=2, row=1, sticky=(W, E))
        self.meters = StringVar()

        ttk.Label(mainframe, textvariable=self.meters).grid(column=2, row=2, sticky=(W, E))
        ttk.Button(mainframe, text="Calculate", command=self.calculate).grid(column=3, row=3, sticky=W)

        ttk.Label(mainframe, text="feet").grid(column=3, row=1, sticky=W)
        ttk.Label(mainframe, text="is equivalent to").grid(column=1, row=2, sticky=E)
        ttk.Label(mainframe, text="meters").grid(column=3, row=2, sticky=W)

        for child in mainframe.winfo_children(): 
            child.grid_configure(padx=5, pady=5)

        feet_entry.focus()
        root.bind("<Return>", self.calculate)
        
    def calculate(self, *args):
        try:
            value = float(self.feet.get())
            self.meters.set(int(0.3048 * value * 10000.0 + 0.5)/10000.0)
        except ValueError:
            pass

root = Tk()
FeetToMeters(root)
root.mainloop()
'''

