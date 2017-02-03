##main window for submitting a link to the server/gamestate
from tkinter import *

class Win_Main_MP:
    ##

    ##
    def __init__(self):
        self.This_win = Toplevel()
        self.This_win.title('Link Roulette - Session')#add id to this
        self.This_win.geometry('305x300')

        ##widgets

        ##end
        #self.root.config(menu=Menu_main)#title = 'Link Roulette'
        #self.This_win.title('Link Roulette')
        #self.This_win.geometry('305x300')
        self.This_win.after(2000, self.event_TED)
        self.This_win.mainloop()

    def event_TED(self):
        root.after(2000, self.event_TED)

