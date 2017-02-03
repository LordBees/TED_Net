#lobby menu for connection managing
import os
from tkinter import *

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

        G_join_lbl.pack()
        G_join_ent.pack()
        G_join_but.pack()

        Menu_main = Menu(self.This_win)
        Menu_settings = Menu(Menu_main,tearoff = 0)
        #Menu_settings = Menu(menubar, tearoff=0)
        #Menu_settings.add_command(label="Host game", command=self.dn)
        #Menu_settings.add_command(label="custom link", command=Menu_customchoose_window)
        #Menu_main.add_cascade(label = 'options',menu = Menu_settings)
        #Menu_main.add_command(label="preview", command=Menu_preview_window)
        Menu_main.add_command(label="Host game", command=self.dn)
        #on_run()
        self.This_win.config(menu=Menu_main)#title = 'Link Roulette'
        self.This_win.mainloop()
    def dn(self):
        pass