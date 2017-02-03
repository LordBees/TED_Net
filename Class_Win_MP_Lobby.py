#lobby menu for connection managing
import os
from tkinter import *

#help menu wins
import Class_Win_Howto,Class_Win_MP_Howto

class Win_MP_Lobby:
    ##
    
    ##
    def __init__(self):
        self.This_win = Tk()#Toplevel()
        self.This_win.title('Link Roulette - Lobby')
        self.This_win.geometry('305x300')
        
        ##tkvars
        #g

        self.G_join_ent_var = StringVar()
        ##end

        ##widgets
        #G_host_but = Button(self.This_win,text = 'Host a game!')

        G_join_but = Button(self.This_win,text = 'Join!')
        G_join_ent = Entry(self.This_win,textvariable = self.G_join_ent_var)
        G_join_lbl = Label(self.This_win,text = 'enter pin to join a multiplayer game')

        G_pname_ent = Entry(self.This_win,textvariable = self.G_join_ent_var)
        G_pname_lbl = Label(self.This_win,text = 'enter name for game')

        G_join_lbl.pack()
        G_join_ent.pack()
       

        G_pname_lbl.pack()
        G_pname_ent.pack()

        G_join_but.pack()

        Menu_main = Menu(self.This_win)
        Menu_help = Menu(Menu_main,tearoff = 0)
        #Menu_settings = Menu(menubar, tearoff=0)
        Menu_help.add_command(label="MP help", command=Class_Win_MP_Howto.Window)##mp at top as more relavent to this window
        Menu_help.add_command(label="SP help", command=Class_Win_Howto.Window)
      
        #Menu_settings.add_command(label="custom link", command=Menu_customchoose_window)
        #Menu_main.add_command(label="preview", command=Menu_preview_window)
        Menu_main.add_command(label="Host game", command=self.gethostinfo)#=self.dn)
        Menu_main.add_cascade(label = 'How To',menu = Menu_help)
        #Menu_main
        #on_run()
        self.This_win.config(menu=Menu_main)#title = 'Link Roulette'
        self.This_win.mainloop()
    def dn(self):
        pass
    def gethostinfo(self):
        pass