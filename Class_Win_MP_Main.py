##main window for submitting a link to the server/gamestate
from tkinter import *

#help menu wins
import Class_Win_Howto,Class_Win_MP_Howto

class Win_Main_MP:
    ##

    ##
    def __init__(self):
        self.This_win = Tk()
        self.This_win.title('Link Roulette - Session')#add id to this
        self.This_win.geometry('305x300')

        ##widgets

        ##end
        Menu_main = Menu(self.This_win)
        Menu_help = Menu(Menu_main,tearoff = 0)
        #Menu_settings = Menu(menubar, tearoff=0)
        Menu_help.add_command(label="MP help", command=Class_Win_MP_Howto.Window)##mp at top as more relavent to this window
        Menu_help.add_command(label="SP help", command=Class_Win_Howto.Window)
        Menu_main.add_cascade(label = 'How To',menu = Menu_help)

        self.This_win.config(menu=Menu_main)#title = 'Link Roulette'
        #self.This_win.title('Link Roulette')
        #self.This_win.geometry('305x300')
        self.This_win.after(700, self.event_TED)
        #print('test')
        self.This_win.mainloop()

    def event_TED(self):
        self.This_win.after(700, self.event_TED)
#Win_Main_MP()##testing
