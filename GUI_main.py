"""
    GUI Script
"""
# # Module Declaration
# import tkinter as tk
#
# # Function Declaration
# def write_slogan():
#     print("Tkinter is easy to use!")
#


import tkinter as tk                # python 3
from tkinter import font  as tkfont # python 3

class SampleApp(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        self.title("Expert PGM")
        self.title_font = tkfont.Font(family='Helvetica', size=18, weight="bold", slant="italic")

        # the container is where we'll stack a bunch of frames
        # on top of each other, then the one we want visible
        # will be raised above the others
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}
        # Perlu diganti
        for F in (StartPage, PageOne, PageTwo, EndPage):
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[page_name] = frame

            # put all of the pages in the same location;
            # the one on the top of the stacking order
            # will be the one that is visible.
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("StartPage")

    def show_frame(self, page_name):
        '''Show a frame for the given page name'''
        frame = self.frames[page_name]
        frame.tkraise()


class StartPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="Welcome to Expert PGM", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)

        button1 = tk.Button(self, text="Start!",
                            command=lambda: controller.show_frame("PageOne"))
        button1.pack()


# Nama kelas ganti
class PageOne(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        v = tk.IntVar()
        v.set(1)  # initializing the choice, i.e. Python

        options = [
            "Mining",
            "Geotechnical and Environmental",
            "Geothermal",
            "Oil and Gas",
            "Unconventional"
        ]

        def ShowChoice():
            print(v.get())

        # Perlu Ganti
        def Next(a):
            if (a.get() == 1):
                controller.show_frame("PageTwo")
            else:
                controller.show_frame("StartPage")

        tk.Label(self,
                 text="""What do you looking for?:""",
                 justify = tk.LEFT,
                 padx = 20).pack()

        for val, option in enumerate(options):
            tk.Radiobutton(self,
                          text=option,
                          padx = 20,
                          variable=v,
                          command=ShowChoice,
                          value=val+1).pack(anchor=tk.W)
        button = tk.Button(self, text="Next",
                           command=lambda: Next(v))
        button.pack()


class PageTwo(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        v = tk.IntVar()
        v.set(1)  # initializing the choice, i.e. Python

        options = [
            "VMS Deposit",
            "Uranium Deposit",
            "Porphyry Copper Deposit",
            "Diamond",
            "Lode Gold",
            "Coal"
        ]

        def ShowChoice():
            print(v.get())

        def Next(a):
            controller.show_frame("EndPage")

        tk.Label(self,
                 text="""More Choice:""",
                 justify = tk.LEFT,
                 padx = 20).pack()

        for val, option in enumerate(options):
            tk.Radiobutton(self,
                          text=option,
                          padx = 20,
                          variable=v,
                          command=ShowChoice,
                          value=val+1).pack(anchor=tk.W)
        button = tk.Button(self, text="Next",
                           command=lambda: Next(v))
        button.pack()


class EndPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text=
                         """Thank You!
 Your Answer is :
 X""", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)

if __name__ == "__main__":
    app = SampleApp()
    app.mainloop()
