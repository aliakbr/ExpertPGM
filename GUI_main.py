"""
    GUI Script
"""
# Expert System for Proper Geophysical Method
# Kelompok 21
# Cessa Mutiara Aziz - 12314056
# Rahman Fitra Perdana - 12314058
# Nuresi Rantri Wulan N. - 12314060
# Aditya Prabowo - 12314062
# Maharditio Chairul S. - 12314063

import tkinter as tk                #
from tkinter import font  as tkfont #

class SampleApp(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        self.title("Expert PGM")
        self.title_font = tkfont.Font(family='Helvetica', size=18, weight="bold", slant="italic")

        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}
        for F in (StartPage, MainPage, PageM, PageM1, PageM2, PageM3, PageM4, PageM5, PageM6, PageM11, PageM12, PageM111, PageM112, PageM121, PageM122, PageM21, PageM22, PageM211, PageM212, PageM221, PageM222, PageM31, PageM32, PageM311, PageM312, PageM321, PageM322, PageM41, PageM42, PageM411, PageM412, PageM421, PageM422, PageM51, PageM52, PageM511, PageM512, PageM521, PageM522, PageGTL, PageGTL1, PageGTL11,PageGTL12, PageGTL13, PageGTL2, PageGTL21, PageGTL22, PageGTL23, PageGTL24, PageGTL3, PageGTL31, PageGTL32, PageGTL33, PageGTL34, PageGTL35, PageGTL36, PageGTL37, PageGTL371, PageGTL3711, PageGTL3712, PageGTL372, PageGTL3721, PageGTL3722, PageG, PageG1, PageG11, PageG12, PageG2, PageG21, PageG22, PageO, PageO1, PageO2, PageO3, PageU, PageU1, PageU2):
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[page_name] = frame

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
        label = tk.Label(self, text="""Welcome to Expert PGM
Terratory
Kelompok 21 Kelas AI 2018""", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)

        button1 = tk.Button(self, text="Start!",
                            command=lambda: controller.show_frame("MainPage"))
        button1.pack()


class MainPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        v = tk.IntVar()
        v.set(1)  

        options = [
            "Mining",
            "Geotechnical and Environmental",
            "Geothermal",
            "Oil and Gas",
            "Unconventional"
        ]

        def Next(a):
            if (a.get() == 1):
                controller.show_frame("PageM")
            elif (a.get() == 2):
                controller.show_frame("PageGTL")
            elif (a.get() == 3):
                controller.show_frame("PageG")
            elif (a.get() == 4):
                controller.show_frame("PageO")
            elif (a.get() == 5):
                controller.show_frame("PageU")
            else:
                controller.show_frame("MainPage")

        tk.Label(self,
                 text="""What do you looking for?:""",
                 justify = tk.LEFT,
                 padx = 20).pack()

        for val, option in enumerate(options):
            tk.Radiobutton(self,
                          text=option,
                          padx = 20,
                          variable=v,

                          value=val+1).pack(anchor=tk.W)
        button = tk.Button(self, text="Next",
                           command=lambda: Next(v))
        button.pack()


class PageM(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        v = tk.IntVar()
        v.set(1)  

        options = [
            "VMS Deposit",
            "Uranium Deposit",
            "Porphyry Copper Deposit",
            "Diamond",
            "Lode Gold",
            "Coal"
        ]




        def Next(a):
            if (a.get() == 1):
                controller.show_frame("PageM1")
            elif (a.get() == 2):
                controller.show_frame("PageM2")
            elif (a.get() == 3):
                controller.show_frame("PageM3")
            elif (a.get() == 4):
                controller.show_frame("PageM4")
            elif (a.get() == 5):
                controller.show_frame("PageM5")
            elif (a.get() == 6):
                controller.show_frame("PageM6")


        tk.Label(self,
                 text="""More Choice : """,
                 justify = tk.LEFT,
                 padx = 20).pack()

        for val, option in enumerate(options):
            tk.Radiobutton(self,
                          text=option,
                          padx = 20,
                          variable=v,

                          value=val+1).pack(anchor=tk.W)
        button = tk.Button(self, text="Next",
                           command=lambda: Next(v))
        button.pack()


class PageM1(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        v = tk.IntVar()
        v.set(1)  

        options = [
            "Air",
            "Ground",
        ]




        def Next(a):
            if (a.get() == 1):
                controller.show_frame("PageM11")
            elif (a.get() == 2):
                controller.show_frame("PageM12")

        tk.Label(self,
                 text="""More Spesific Survey :""",
                 justify = tk.LEFT,
                 padx = 20).pack()

        for val, option in enumerate(options):
            tk.Radiobutton(self,
                          text=option,
                          padx = 20,
                          variable=v,

                          value=val+1).pack(anchor=tk.W)
        button = tk.Button(self, text="Next",
                           command=lambda: Next(v))
        button.pack()

class PageM2(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        v = tk.IntVar()
        v.set(1)  

        options = [
            "Air",
            "Ground",
        ]




        def Next(a):
            if (a.get() == 1):
                controller.show_frame("PageM21")
            elif (a.get() == 2):
                controller.show_frame("PageM22")

        tk.Label(self,
                 text="""More Spesific Survey :""",
                 justify = tk.LEFT,
                 padx = 20).pack()

        for val, option in enumerate(options):
            tk.Radiobutton(self,
                          text=option,
                          padx = 20,
                          variable=v,

                          value=val+1).pack(anchor=tk.W)
        button = tk.Button(self, text="Next",
                           command=lambda: Next(v))
        button.pack()


class PageM3(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        v = tk.IntVar()
        v.set(1)  

        options = [
            "Air",
            "Ground",
        ]




        def Next(a):
            if (a.get() == 1):
                controller.show_frame("PageM31")
            elif (a.get() == 2):
                controller.show_frame("PageM32")

        tk.Label(self,
                 text="""More Spesific Survey :""",
                 justify = tk.LEFT,
                 padx = 20).pack()

        for val, option in enumerate(options):
            tk.Radiobutton(self,
                          text=option,
                          padx = 20,
                          variable=v,

                          value=val+1).pack(anchor=tk.W)
        button = tk.Button(self, text="Next",
                           command=lambda: Next(v))
        button.pack()

class PageM4(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        v = tk.IntVar()
        v.set(1)  

        options = [
            "Air",
            "Ground",
        ]




        def Next(a):
            if (a.get() == 1):
                controller.show_frame("PageM41")
            elif (a.get() == 2):
                controller.show_frame("PageM42")

        tk.Label(self,
                 text="""More Spesific Survey :""",
                 justify = tk.LEFT,
                 padx = 20).pack()

        for val, option in enumerate(options):
            tk.Radiobutton(self,
                          text=option,
                          padx = 20,
                          variable=v,

                          value=val+1).pack(anchor=tk.W)
        button = tk.Button(self, text="Next",
                           command=lambda: Next(v))
        button.pack()

class PageM5(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        v = tk.IntVar()
        v.set(1)  

        options = [
            "Air",
            "Ground",
        ]




        def Next(a):
            if (a.get() == 1):
                controller.show_frame("PageM51")
            elif (a.get() == 2):
                controller.show_frame("PageM52")

        tk.Label(self,
                 text="""More Spesific Survey :""",
                 justify = tk.LEFT,
                 padx = 20).pack()

        for val, option in enumerate(options):
            tk.Radiobutton(self,
                          text=option,
                          padx = 20,
                          variable=v,

                          value=val+1).pack(anchor=tk.W)
        button = tk.Button(self, text="Next",
                           command=lambda: Next(v))
        button.pack()

class PageM6(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text=
                         """The Proper Method for your Survey is
Gravity, Seismic Reflection, Seismic Refraction, Magnetic """, font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)

class PageM11(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        v = tk.IntVar()
        v.set(1)  

        options = [
            "Geological Framework",
            "Direct Targeting",
        ]




        def Next(a):
            if (a.get() == 1):
                controller.show_frame("PageM111")
            elif (a.get() == 2):
                controller.show_frame("PageM112")

        tk.Label(self,
                 text="""More Spesific Survey :""",
                 justify = tk.LEFT,
                 padx = 20).pack()

        for val, option in enumerate(options):
            tk.Radiobutton(self,
                          text=option,
                          padx = 20,
                          variable=v,

                          value=val+1).pack(anchor=tk.W)
        button = tk.Button(self, text="Next",
                           command=lambda: Next(v))
        button.pack()


class PageM12(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        v = tk.IntVar()
        v.set(1)  

        options = [
            "Geological Framework",
            "Direct Targeting",
        ]




        def Next(a):
            if (a.get() == 1):
                controller.show_frame("PageM121")
            elif (a.get() == 2):
                controller.show_frame("PageM122")

        tk.Label(self,
                 text="""More Spesific Survey :""",
                 justify = tk.LEFT,
                 padx = 20).pack()

        for val, option in enumerate(options):
            tk.Radiobutton(self,
                          text=option,
                          padx = 20,
                          variable=v,

                          value=val+1).pack(anchor=tk.W)
        button = tk.Button(self, text="Next",
                           command=lambda: Next(v))
        button.pack()


class PageM21(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        v = tk.IntVar()
        v.set(1)  

        options = [
            "Geological Framework",
            "Direct Targeting",
        ]




        def Next(a):
            if (a.get() == 1):
                controller.show_frame("PageM211")
            elif (a.get() == 2):
                controller.show_frame("PageM212")

        tk.Label(self,
                 text="""More Spesific Survey :""",
                 justify = tk.LEFT,
                 padx = 20).pack()

        for val, option in enumerate(options):
            tk.Radiobutton(self,
                          text=option,
                          padx = 20,
                          variable=v,

                          value=val+1).pack(anchor=tk.W)
        button = tk.Button(self, text="Next",
                           command=lambda: Next(v))
        button.pack()


class PageM22(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        v = tk.IntVar()
        v.set(1)  

        options = [
            "Geological Framework",
            "Direct Targeting",
        ]




        def Next(a):
            if (a.get() == 1):
                controller.show_frame("PageM221")
            elif (a.get() == 2):
                controller.show_frame("PageM222")

        tk.Label(self,
                 text="""More Spesific Survey :""",
                 justify = tk.LEFT,
                 padx = 20).pack()

        for val, option in enumerate(options):
            tk.Radiobutton(self,
                          text=option,
                          padx = 20,
                          variable=v,

                          value=val+1).pack(anchor=tk.W)
        button = tk.Button(self, text="Next",
                           command=lambda: Next(v))
        button.pack()


class PageM31(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        v = tk.IntVar()
        v.set(1)  

        options = [
            "Geological Framework",
            "Direct Targeting",
        ]




        def Next(a):
            if (a.get() == 1):
                controller.show_frame("PageM311")
            elif (a.get() == 2):
                controller.show_frame("PageM312")

        tk.Label(self,
                 text="""More Spesific Survey :""",
                 justify = tk.LEFT,
                 padx = 20).pack()

        for val, option in enumerate(options):
            tk.Radiobutton(self,
                          text=option,
                          padx = 20,
                          variable=v,

                          value=val+1).pack(anchor=tk.W)
        button = tk.Button(self, text="Next",
                           command=lambda: Next(v))
        button.pack()


class PageM32(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        v = tk.IntVar()
        v.set(1)  

        options = [
            "Geological Framework",
            "Direct Targeting",
        ]




        def Next(a):
            if (a.get() == 1):
                controller.show_frame("PageM321")
            elif (a.get() == 2):
                controller.show_frame("PageM322")

        tk.Label(self,
                 text="""More Spesific Survey :""",
                 justify = tk.LEFT,
                 padx = 20).pack()

        for val, option in enumerate(options):
            tk.Radiobutton(self,
                          text=option,
                          padx = 20,
                          variable=v,

                          value=val+1).pack(anchor=tk.W)
        button = tk.Button(self, text="Next",
                           command=lambda: Next(v))
        button.pack()


class PageM41(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        v = tk.IntVar()
        v.set(1)  

        options = [
            "Geological Framework",
            "Direct Targeting",
        ]




        def Next(a):
            if (a.get() == 1):
                controller.show_frame("PageM411")
            elif (a.get() == 2):
                controller.show_frame("PageM412")

        tk.Label(self,
                 text="""More Spesific Survey :""",
                 justify = tk.LEFT,
                 padx = 20).pack()

        for val, option in enumerate(options):
            tk.Radiobutton(self,
                          text=option,
                          padx = 20,
                          variable=v,

                          value=val+1).pack(anchor=tk.W)
        button = tk.Button(self, text="Next",
                           command=lambda: Next(v))
        button.pack()


class PageM42(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        v = tk.IntVar()
        v.set(1)  

        options = [
            "Geological Framework",
            "Direct Targeting",
        ]




        def Next(a):
            if (a.get() == 1):
                controller.show_frame("PageM421")
            elif (a.get() == 2):
                controller.show_frame("PageM422")

        tk.Label(self,
                 text="""More Spesific Survey :""",
                 justify = tk.LEFT,
                 padx = 20).pack()

        for val, option in enumerate(options):
            tk.Radiobutton(self,
                          text=option,
                          padx = 20,
                          variable=v,

                          value=val+1).pack(anchor=tk.W)
        button = tk.Button(self, text="Next",
                           command=lambda: Next(v))
        button.pack()


class PageM51(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        v = tk.IntVar()
        v.set(1)  

        options = [
            "Geological Framework",
            "Direct Targeting",
        ]




        def Next(a):
            if (a.get() == 1):
                controller.show_frame("PageM511")
            elif (a.get() == 2):
                controller.show_frame("PageM512")

        tk.Label(self,
                 text="""More Spesific Survey :""",
                 justify = tk.LEFT,
                 padx = 20).pack()

        for val, option in enumerate(options):
            tk.Radiobutton(self,
                          text=option,
                          padx = 20,
                          variable=v,

                          value=val+1).pack(anchor=tk.W)
        button = tk.Button(self, text="Next",
                           command=lambda: Next(v))
        button.pack()


class PageM52(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        v = tk.IntVar()
        v.set(1)  

        options = [
            "Geological Framework",
            "Direct Targeting",
        ]




        def Next(a):
            if (a.get() == 1):
                controller.show_frame("PageM521")
            elif (a.get() == 2):
                controller.show_frame("PageM522")

        tk.Label(self,
                 text="""More Spesific Survey :""",
                 justify = tk.LEFT,
                 padx = 20).pack()

        for val, option in enumerate(options):
            tk.Radiobutton(self,
                          text=option,
                          padx = 20,
                          variable=v,

                          value=val+1).pack(anchor=tk.W)
        button = tk.Button(self, text="Next",
                           command=lambda: Next(v))
        button.pack()

class PageM111(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text=
                         """The Proper Method for your Survey is
Magnetic, Radiometric """, font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)


class PageM112(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text=
                         """The Proper Method for your Survey is
Magnetic, EM, Gravity """, font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)


class PageM121(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text=
                         """The Proper Method for your Survey is
Magnetic """, font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)


class PageM122(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text=
                         """The Proper Method for your Survey is
Magnetic, EM, Electrical, Gravity """, font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)


class PageM211(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text=
                         """The Proper Method for your Survey is
Magnetic, EM, Radiometric """, font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)


class PageM212(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text=
                         """The Proper Method for your Survey is
EM, Radiometric """, font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)


class PageM221(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text=
                         """The Proper Method for your Survey is
 Magnetic, EM, Gravity, Radiometric """, font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)


class PageM222(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text=
                         """The Proper Method for your Survey is
EM, Radiometric """, font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)


class PageM311(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text=
                         """The Proper Method for your Survey is
Magnetic, Radiometric """, font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)


class PageM312(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text=
                         """The Proper Method for your Survey is
Magnetic, Radiometric """, font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)


class PageM321(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text=
                         """The Proper Method for your Survey is
Magnetic, Radiometric """, font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)


class PageM322(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text=
                         """The Proper Method for your Survey is
Magnetic, Electrical, Radiometric """, font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)


class PageM411(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text=
                         """The Proper Method for your Survey is
Magnetic """, font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)


class PageM412(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text=
                         """The Proper Method for your Survey is
Magnetic, EM, Gravity """, font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)


class PageM421(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text=
                         """The Proper Method for your Survey is
Magnetic, EM, Gravity """, font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)


class PageM422(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text=
                         """The Proper Method for your Survey is
Magnetic, EM, Gravity """, font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)


class PageM511(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text=
                         """The Proper Method for your Survey is
Magnetic, Radiometric """, font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)


class PageM512(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text=
                         """The Proper Method for your Survey is
EM, Radiometric """, font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)


class PageM521(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text=
                         """The Proper Method for your Survey is
Magnetic, Radiometric """, font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)


class PageM522(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text=
                         """The Proper Method for your Survey is
Magnetic, Electrical, Radiometric """, font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)


class PageGTL(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        v = tk.IntVar()
        v.set(1)  

        options = [
            "Inorganic Contaminant",
            "Man Made Buried Object",
            "Natural Condition",
        ]




        def Next(a):
            if (a.get() == 1):
                controller.show_frame("PageGTL1")
            elif (a.get() == 2):
                controller.show_frame("PageGTL2")
            elif (a.get() == 3):
                controller.show_frame("PageGTL3")

        tk.Label(self,
                 text="""More Choice : """,
                 justify = tk.LEFT,
                 padx = 20).pack()

        for val, option in enumerate(options):
            tk.Radiobutton(self,
                          text=option,
                          padx = 20,
                          variable=v,

                          value=val+1).pack(anchor=tk.W)
        button = tk.Button(self, text="Next",
                           command=lambda: Next(v))
        button.pack()

class PageGTL1(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        v = tk.IntVar()
        v.set(1)  

        options = [
            "Soil Salinity",
            "Salt Water Intrusion",
            "Landfill",
        ]




        def Next(a):
            if (a.get() == 1):
                controller.show_frame("PageGTL11")
            elif (a.get() == 2):
                controller.show_frame("PageGTL12")
            elif (a.get() == 3):
                controller.show_frame("PageGTL13")

        tk.Label(self,
                 text="""More Choice : """,
                 justify = tk.LEFT,
                 padx = 20).pack()

        for val, option in enumerate(options):
            tk.Radiobutton(self,
                          text=option,
                          padx = 20,
                          variable=v,

                          value=val+1).pack(anchor=tk.W)
        button = tk.Button(self, text="Next",
                           command=lambda: Next(v))
        button.pack()


class PageGTL2(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        v = tk.IntVar()
        v.set(1)  

        options = [
            "Utilities (Cabel, Pipe, etc)",
            "Abandoned Wells",
            "Forensic",
            "Archeology",
        ]




        def Next(a):
            if (a.get() == 1):
                controller.show_frame("PageGTL21")
            elif (a.get() == 2):
                controller.show_frame("PageGTL22")
            elif (a.get() == 3):
                controller.show_frame("PageGTL23")
            elif (a.get() == 4):
                controller.show_frame("PageGTL24")

        tk.Label(self,
                 text="""More Choice : """,
                 justify = tk.LEFT,
                 padx = 20).pack()

        for val, option in enumerate(options):
            tk.Radiobutton(self,
                          text=option,
                          padx = 20,
                          variable=v,

                          value=val+1).pack(anchor=tk.W)
        button = tk.Button(self, text="Next",
                           command=lambda: Next(v))
        button.pack()


class PageGTL3(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        v = tk.IntVar()
        v.set(1)  

        options = [
            "Depth to Water Table",
            "Karst",
            "Buried Channel",
            "Sinkhole",
            "Dam/Lagoon Leakage",
            "Buried Fault/Dyke",
            "Statigraphical",
        ]




        def Next(a):
            if (a.get() == 1):
                controller.show_frame("PageGTL31")
            elif (a.get() == 2):
                controller.show_frame("PageGTL32")
            elif (a.get() == 3):
                controller.show_frame("PageGTL33")
            elif (a.get() == 4):
                controller.show_frame("PageGTL34")
            elif (a.get() == 5):
                controller.show_frame("PageGTL35")
            elif (a.get() == 6):
                controller.show_frame("PageGTL36")
            elif (a.get() == 7):
                controller.show_frame("PageGTL37")
        tk.Label(self,
                 text="""More Choice : """,
                 justify = tk.LEFT,
                 padx = 20).pack()

        for val, option in enumerate(options):
            tk.Radiobutton(self,
                          text=option,
                          padx = 20,
                          variable=v,

                          value=val+1).pack(anchor=tk.W)
        button = tk.Button(self, text="Next",
                           command=lambda: Next(v))
        button.pack()

class PageGTL11(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text=
                         """The Proper Method for your Survey is
DC Resistivity, Frequency Domain EM""", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)


class PageGTL12(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text=
                         """The Proper Method for your Survey is
DC Resistivity, Frequency Domain EM, Time Domain EM""", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)


class PageGTL13(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text=
                         """The Proper Method for your Survey is
DC Resistivity, Frequency Domain EM, Time Domain EM""", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)


class PageGTL21(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text=
                         """The Proper Method for your Survey is
GPR""", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)


class PageGTL22(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text=
                         """The Proper Method for your Survey is
Magnetic""", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)


class PageGTL23(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text=
                         """The Proper Method for your Survey is
Frequency Domain EM""", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)


class PageGTL24(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text=
                         """The Proper Method for your Survey is
Frequency Domain EM, GPR, Time Domain EM""", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)


class PageGTL31(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text=
                         """The Proper Method for your Survey is
DC Resistivity, Seismic Refraction, GPR""", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)


class PageGTL32(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text=
                         """The Proper Method for your Survey is
Microgravity, GPR""", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)


class PageGTL33(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text=
                         """The Proper Method for your Survey is
DC Resistivity, Seismic Refraction""", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)


class PageGTL34(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text=
                         """The Proper Method for your Survey is
GPR, Microgravity""", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)


class PageGTL35(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text=
                         """The Proper Method for your Survey is
Self Potential (SP)""", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)


class PageGTL36(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text=
                         """The Proper Method for your Survey is
DC Resistivity, Seismic, Magnetic""", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)


class PageGTL37(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        v = tk.IntVar()
        v.set(1)  

        options = [
            "Sand & Gravel Over Bedrock, Water Table, Low in Sand & Gravel",
            "Sand & Gravel Over Bedrock, Water Table, High in Sand & Gravel",
        ]




        def Next(a):
            if (a.get() == 1):
                controller.show_frame("PageGTL371")
            elif (a.get() == 2):
                controller.show_frame("PageGTL372")

        tk.Label(self,
                 text="""More Spesific Survey :""",
                 justify = tk.LEFT,
                 padx = 20).pack()

        for val, option in enumerate(options):
            tk.Radiobutton(self,
                          text=option,
                          padx = 20,
                          variable=v,

                          value=val+1).pack(anchor=tk.W)
        button = tk.Button(self, text="Next",
                           command=lambda: Next(v))
        button.pack()

class PageGTL371(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        v = tk.IntVar()
        v.set(1)  

        options = [
            "Land",
            "Marine",
        ]




        def Next(a):
            if (a.get() == 1):
                controller.show_frame("PageGTL3711")
            elif (a.get() == 2):
                controller.show_frame("PageGTL3712")

        tk.Label(self,
                 text="""More Spesific Survey :""",
                 justify = tk.LEFT,
                 padx = 20).pack()

        for val, option in enumerate(options):
            tk.Radiobutton(self,
                          text=option,
                          padx = 20,
                          variable=v,

                          value=val+1).pack(anchor=tk.W)
        button = tk.Button(self, text="Next",
                           command=lambda: Next(v))
        button.pack()


class PageGTL372(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        v = tk.IntVar()
        v.set(1)  

        options = [
            "Land",
            "Marine",
        ]




        def Next(a):
            if (a.get() == 1):
                controller.show_frame("PageGTL3721")
            elif (a.get() == 2):
                controller.show_frame("PageGTL3722")

        tk.Label(self,
                 text="""More Spesific Survey :""",
                 justify = tk.LEFT,
                 padx = 20).pack()

        for val, option in enumerate(options):
            tk.Radiobutton(self,
                          text=option,
                          padx = 20,
                          variable=v,

                          value=val+1).pack(anchor=tk.W)
        button = tk.Button(self, text="Next",
                           command=lambda: Next(v))
        button.pack()


class PageGTL3711(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text=
                         """The Proper Method for your Survey is
Seismic Refraction""", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)


class PageGTL3712(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text=
                         """The Proper Method for your Survey is
Continuous Reflection Seismic Profilling (CRSP)""", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)


class PageGTL3721(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text=
                         """The Proper Method for your Survey is
DC Resistivity""", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)


class PageGTL3722(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text=
                         """The Proper Method for your Survey is
Continuous Reflection Seismic Profilling (CRSP)""", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)

class PageG(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        v = tk.IntVar()
        v.set(1)  

        options = [
            "Exploration",
            "Development",
        ]




        def Next(a):
            if (a.get() == 1):
                controller.show_frame("PageG1")
            elif (a.get() == 2):
                controller.show_frame("PageG2")

        tk.Label(self,
                 text="""More Choice : """,
                 justify = tk.LEFT,
                 padx = 20).pack()

        for val, option in enumerate(options):
            tk.Radiobutton(self,
                          text=option,
                          padx = 20,
                          variable=v,

                          value=val+1).pack(anchor=tk.W)
        button = tk.Button(self, text="Next",
                           command=lambda: Next(v))
        button.pack()


class PageG1(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        v = tk.IntVar()
        v.set(1)  

        options = [
            "Clay Cap Distribution",
            "Delineation Reservoir & Basement",
        ]




        def Next(a):
            if (a.get() == 1):
                controller.show_frame("PageG11")
            elif (a.get() == 2):
                controller.show_frame("PageG12")

        tk.Label(self,
                 text="""More Choice : """,
                 justify = tk.LEFT,
                 padx = 20).pack()

        for val, option in enumerate(options):
            tk.Radiobutton(self,
                          text=option,
                          padx = 20,
                          variable=v,

                          value=val+1).pack(anchor=tk.W)
        button = tk.Button(self, text="Next",
                           command=lambda: Next(v))
        button.pack()


class PageG2(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        v = tk.IntVar()
        v.set(1)  

        options = [
            "Well Target Zone",
            "Monitoring (Injection, etc)",
        ]




        def Next(a):
            if (a.get() == 1):
                controller.show_frame("PageG21")
            elif (a.get() == 2):
                controller.show_frame("PageG22")

        tk.Label(self,
                 text="""More Choice : """,
                 justify = tk.LEFT,
                 padx = 20).pack()

        for val, option in enumerate(options):
            tk.Radiobutton(self,
                          text=option,
                          padx = 20,
                          variable=v,

                          value=val+1).pack(anchor=tk.W)
        button = tk.Button(self, text="Next",
                           command=lambda: Next(v))
        button.pack()

class PageG11(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text=
                         """The Proper Method for your Survey is
MT, Gravity, Time Domain EM, """, font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)


class PageG12(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text=
                         """The Proper Method for your Survey is
MT, Gravity, Magnetic, Passive Seismic, Time Domain EM""", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)


class PageG21(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text=
                         """The Proper Method for your Survey is
Passive Seismic, MT, Gravity""", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)


class PageG22(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text=
                         """The Proper Method for your Survey is
Microearthquake, Microgravity""", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)

class PageO(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        v = tk.IntVar()
        v.set(1)  

        options = [
            "Delineation Reservoir Hydrocarbon",
            "Delineation Basement",
            "Structural Mapping"
        ]




        def Next(a):
            if (a.get() == 1):
                controller.show_frame("PageO1")
            elif (a.get() == 2):
                controller.show_frame("PageO2")
            elif (a.get() == 3):
                controller.show_frame("PageO3")

        tk.Label(self,
                 text="""Exploration : """,
                 justify = tk.LEFT,
                 padx = 20).pack()

        for val, option in enumerate(options):
            tk.Radiobutton(self,
                          text=option,
                          padx = 20,
                          variable=v,

                          value=val+1).pack(anchor=tk.W)
        button = tk.Button(self, text="Next",
                           command=lambda: Next(v))
        button.pack()

class PageO1(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text=
                         """The Proper Method for your Survey is
Seismic Reflection""", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)


class PageO2(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text=
                         """The Proper Method for your Survey is
Gravity, Seismic Reflection""", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)


class PageO3(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text=
                         """The Proper Method for your Survey is
Gravity, Seismic Reflection, Magnetic, Seismic Refraction""", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)

class PageU(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        v = tk.IntVar()
        v.set(1)  

        options = [
            "Shale gas & Oil",
            "Hydrate Gas",
        ]




        def Next(a):
            if (a.get() == 1):
                controller.show_frame("PageU1")
            elif (a.get() == 2):
                controller.show_frame("PageU2")

        tk.Label(self,
                 text="""Exploration : """,
                 justify = tk.LEFT,
                 padx = 20).pack()

        for val, option in enumerate(options):
            tk.Radiobutton(self,
                          text=option,
                          padx = 20,
                          variable=v,

                          value=val+1).pack(anchor=tk.W)
        button = tk.Button(self, text="Next",
                           command=lambda: Next(v))
        button.pack()

class PageU1(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text=
                         """The Proper Method for your Survey is
Seismic Reflection, Gravity""", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)


class PageU2(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text=
                         """The Proper Method for your Survey is
Seismic Reflection""", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)


if __name__ == "__main__":
    app = SampleApp()
    app.mainloop()
