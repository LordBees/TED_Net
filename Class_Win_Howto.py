#help window for how to use singleplayer mode
import tkinter as TK

class Window:
    ##

    ##
    def __init__(self):
        self.Drop_help_facts()

    def Drop_help_facts(self):
        helptext = ['How to use LinkRoulette v1'
                    'Playing the game:',
                    'phase 1, Generating a link:',
                    'select your preferred link to generate by clicking the',
                    'button next to the link type,then press generate link',
                    'when you have found a link you want to submit, you can click',
                    '',
                    'phase 2, Opening the link:',
                    'to open the link in this phase you click one of the buttons',
                    'labelled as open link,',
                    '',
                    'history box - allows you to see a history of links you have viewed',
                    'click on one in the box and press select link to load that link for',
                    'opening by the open link button',
                    '',
                    'open homepage -- opens google.co.uk in your browser',
                    '',
                    'clear history - wipes history file',
                    ''
                    ] ##may want a seperate file for help
        ##helpwin = TK.Tk()##debigging win as seperate entity
        helpwin = TK.Toplevel()
        helpwin.title("useful information")
        helpwin.geometry('320x480')
        helpwin_lblframe = TK.LabelFrame(helpwin, text="User guide for SP")
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