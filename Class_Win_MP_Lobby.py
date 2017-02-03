#lobby menu for connection managing
import os
from tkinter import *

#help menu wins
import Class_Win_Howto,Class_Win_MP_Howto

##menus
import Class_Win_MP_Main,Class_Win_MP_hostsetup

##tedutils
import Ted_Network as net
import Ted_Settings as Setting

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
        self.G_pname_ent_var = StringVar()
        self.G_Aname_lbl_VAR = StringVar()
        ##end

        ##widgets
        #G_host_but = Button(self.This_win,text = 'Host a game!')

        G_join_but = Button(self.This_win,text = 'Join!',command = self.prepgamejoin)
        G_join_ent = Entry(self.This_win,textvariable = self.G_join_ent_var)
        G_join_lbl = Label(self.This_win,text = 'enter pin to join a multiplayer game')

        G_pname_ent = Entry(self.This_win,textvariable = self.G_pname_ent_var)
        G_pname_lbl = Label(self.This_win,text = 'enter name for game')

        G_Aname_lbl = Label(self.This_win,textvariable = self.G_Aname_lbl_VAR)#,text = 'enter name for game')

        G_join_lbl.pack()
        G_join_ent.pack()
       

        G_pname_lbl.pack()
        G_pname_ent.pack()

        G_Aname_lbl.pack()
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
        self.This_win.after(700,self.Event_TED)
        self.This_win.config(menu=Menu_main)#title = 'Link Roulette'
        self.This_win.mainloop()

    def Event_TED(self):
        if Setting.ADMIN == True:
            self.G_Aname_lbl_VAR.set('ADMIN PIN:'+str(Setting.apin))
            self.G_join_ent_var.set(Setting.gpin)
        else:
            self.G_Aname_lbl_VAR.set('ADMIN PIN: NONE')
        self.This_win.after(700,self.Event_TED)

    def dn(self):
        pass

    def gethostinfo(self):
        Class_Win_MP_hostsetup.Admin_Win()

    def prepgamejoin(self):
        name = self.G_pname_ent_var.get()
        gpin = self.G_join_ent_var.get()

        resp = net.URL_join_session(gpin,name)

        if resp[0] == 'ERROR' or (resp[0] == 'F'):
            pass#do error label code here
        elif resp[0].upper() == 'S':
            print('Joining game:'+gpin+'as'+str(name))
            Setting.gpin = gpin
            Setting.ppin = str(resp[1])
            Setting.pname = name
            ##self.This_win.after_cancel()
            self.This_win.destroy()#destroy the setup win
            Class_Win_MP_Main.Win_Main_MP()##start up window
        else:
            print('mysterious failure!')

    def prepgamejoin_admin(self):##unfinished
        if Setting.ADMIN == True:
            if resp[0] == 'ERROR' or (resp[0] == 'F'):
                pass#do error label code here
            elif resp[0].upper() == 'S':
                print('Joining game:'+gpin+'as'+str(name)+' (admin)')
                Setting.gpin = gpin
                Setting.ppin = str(resp[1])
                Setting.pname = name
                self.This_win.destroy()#destroy the setup win
                Class_Win_MP_Main.Win_Main_MP()##start up window
            else:
                print('mysterious failure!')

   