#help window for how to use and connect to party mode
import tkinter as TK

class Window:
    ##

    ##
    def __init__(self):
        self.Drop_help_facts()

    def Drop_help_facts(self):
        helptext = ['How to use LinkRoulette - Party v1',
                    '',
                    '',
                    'step 1:',
                    'Hosting a session:',
                    'to host a session you must click the \'host game\' button ',
                    'in the top left corner of the window, you then should ',
                    'click the button labelled\'set as admin of session\' ',
                    'then close the window.',
                    'your main window should now have an admin pin at the bottom',
                    'instead of NONE.',
                    'note down your game pin to give to other players later',
                    'input a unique name into your username box',
                    'then,click join to start the lobby',
                    ' the other players can now join your session!',
                    '(SEE- joining a session to see how)',
                    '',
                    'Joining a session:',
                    'Enter a Username in the box provided',
                    'enter a game pin for a session',
                    'click join to join the game',
                    '',
                    '',
                    ''
                    ] ##may want a seperate file for help
        ##helpwin = TK.Tk()##debigging win as seperate entity
        helpwin = TK.Toplevel()
        helpwin.title("useful information (MP help)")
        helpwin.geometry('325x480')
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
