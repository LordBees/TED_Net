#help window for how to use and connect to party mode
import tkinter as TK

class Window:
    ##

    ##
    def __init__(self):
        self.Drop_help_facts()

    def Drop_help_facts(self):
        helptext = ['How to use LinkRoulette - Party v1'
                    ] ##may want a seperate file for help
        ##helpwin = TK.Tk()##debigging win as seperate entity
        helpwin = TK.Toplevel()
        helpwin.title("useful information")
        helpwin.geometry('320x480')
        helpwin_lblframe = TK.LabelFrame(helpwin, text="User Guide for MP")
        helpwin_lblframe.pack(fill="both", expand="yes")
     
        helpwin_scroll = TK.Scrollbar(helpwin_lblframe)
        helpwin_scroll.pack( side = TK.RIGHT, fill=TK.Y )

        helpwin_listbox = TK.Listbox(helpwin_lblframe, yscrollcommand = helpwin_scroll.set )
        for line in range(len(helptext)):
            helpwin_listbox.insert(TK.END,helptext[line])
    
        helpwin_listbox.config(width =100)

        helpwin_listbox.pack( side = TK.LEFT, fill = TK.Y)
        helpwin_scroll.config( command = helpwin_listbox.yview )
        ##helpwin.mainloop()##debugging win as seperate entity
#Window()