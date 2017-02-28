##tkinter
from tkinter import *
from tkinter import messagebox
##tedutils
import Ted_Network as net
import Ted_Settings as Setting

##wins
import Class_Win_MP_Main

## pregame lobby window
class Win_Main:
    ##

    ##
    def __init__(self):
        self.This_win = Tk()#Toplevel()
        self.This_win.title('Link Roulette - ADMIN/prelobby')
        self.This_win.geometry('305x300')
    
        self.player1_label_LBL_VAR = StringVar()
        self.player2_label_LBL_VAR = StringVar()
        self.player3_label_LBL_VAR = StringVar()
        self.player4_label_LBL_VAR = StringVar()
        self.player5_label_LBL_VAR = StringVar()
        self.player6_label_LBL_VAR = StringVar()
        ##self.playerx_label_LBL_VAR
        ##  widgets
        players_loaded_LF = LabelFrame(self.This_win,text = 'players in session:')
        player1_label_LBL = Label(players_loaded_LF,textvariable = self.player1_label_LBL_VAR)
        player2_label_LBL = Label(players_loaded_LF,textvariable = self.player2_label_LBL_VAR)
        player3_label_LBL = Label(players_loaded_LF,textvariable = self.player3_label_LBL_VAR)
        player4_label_LBL = Label(players_loaded_LF,textvariable = self.player4_label_LBL_VAR)
        player5_label_LBL = Label(players_loaded_LF,textvariable = self.player5_label_LBL_VAR)
        player6_label_LBL = Label(players_loaded_LF,textvariable = self.player6_label_LBL_VAR)

        player1_LBL = Label(players_loaded_LF,text = '|player1:')
        player2_LBL = Label(players_loaded_LF,text = '|player2:')
        player3_LBL = Label(players_loaded_LF,text = '|player3:')
        player4_LBL = Label(players_loaded_LF,text = '|player4:')
        player5_LBL = Label(players_loaded_LF,text = '|player5:')
        player6_LBL = Label(players_loaded_LF,text = '|player6:')##may be able to use only one 


        ##playerx_label_LBL = Label(self.This_win,textvariable = self.playerx_label_LBL_VAR)

        admin_funct_LF = LabelFrame(self.This_win,text = 'admin options')
        admin_closesession_BTN = Button(admin_funct_LF,text = 'close session',command = self.session_close_BUT)
        admin_startgame_BTN = Button(admin_funct_LF,text = 'start game',command = self.session_start)

        #pack

        players_loaded_LF.pack()
        player1_label_LBL.grid(row = 0,column = 1)
        player2_label_LBL.grid(row = 1,column = 1)
        player3_label_LBL.grid(row = 2,column = 1)
        player4_label_LBL.grid(row = 0,column = 3)
        player5_label_LBL.grid(row = 1,column = 3)
        player6_label_LBL.grid(row = 2,column = 3)
        player1_LBL.grid(row = 0,column = 0)
        player2_LBL.grid(row = 1,column = 0)
        player3_LBL.grid(row = 2,column = 0)
        player4_LBL.grid(row = 0,column = 2)
        player5_LBL.grid(row = 1,column = 2)
        player6_LBL.grid(row = 2,column = 2)


        admin_funct_LF.pack()
        admin_closesession_BTN.grid(row = 0,column = 0)
        admin_startgame_BTN.grid(row = 0,column = 1)


        ##
        self.This_win.after(700,self.TED_Event)

    def __del__(self):
        self.session_close()

    def TED_Event(self):
        ##
        self.update_players()
        ##
        self.This_win.after(700,self.TED_Event)

    def update_players(self):
        Playername_data = net.URL_getplayers(Setting.gpin)#,Setting.apin)
        print(Playername_data)
        self.player1_label_LBL_VAR.set(Playername_data[0])
        self.player2_label_LBL_VAR.set(Playername_data[1])
        self.player3_label_LBL_VAR.set(Playername_data[2])
        self.player4_label_LBL_VAR.set(Playername_data[3])
        self.player5_label_LBL_VAR.set(Playername_data[4])
        self.player6_label_LBL_VAR.set(Playername_data[5])

    def session_close(self):
        dat = net.URL_closesession(Setting.gpin,Setting.apin)
        print('session closed:',dat)
        self.This_win.destroy()#destroy the setup win

    def session_close_BUT(self):
        if messagebox.askokcancel('close session?','are you sure?'):
            self.session_close()

    def session_start(self):
        print('starting session')
        start = net.URL_startsession(Setting.gpin,Setting.apin)
        print('start:\n',start,'\n====')
        self.This_win.destroy()#destroy the setup win
        Class_Win_MP_Main.Win_Main_MP()##start up window
##Win_Main()
