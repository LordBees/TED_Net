##main window for submitting a link to the server/gamestate
##usual
import webbrowser
from tkinter import *
from tkinter import messagebox

#help menu wins
import Class_Win_Howto,Class_Win_MP_Howto

#menus
import Class_Win_MP_Customchoose,Class_Win_MP_mpgameinfo

#wins
import Class_Win_MP_Lobby

#ted misc
import Ted_Links,Ted_Network
import Ted_Settings as Setting

class Win_Main_MP:
    ##

    ##
    def __init__(self):
        self.This_win = Tk()
        self.This_win.title('Link Roulette - Session')#add id to this
        self.This_win.geometry('305x300')

        #varinit
        self.linktype_Radio = IntVar()
        self.linktype_Random = IntVar()
        self.gennedlink = StringVar()
        #voting
        self.linkvote_Radio = IntVar()
        #end

        ##widgets
        self.SendLink_LF = LabelFrame(self.This_win,text = 'random link generation')
        tinyurl_radio = Radiobutton(self.SendLink_LF,text = 'tinyurl',variable = self.linktype_Radio,value = 1)
        bitly_radio = Radiobutton(self.SendLink_LF,text = 'Bit.ly',variable = self.linktype_Radio,value = 2)
        googl_radio = Radiobutton(self.SendLink_LF,text = 'goo.gl',variable = self.linktype_Radio,value = 3)
        imgur_radio = Radiobutton(self.SendLink_LF,text = 'imgur',variable = self.linktype_Radio,value = 4)
        self.custom_radio = Radiobutton(self.SendLink_LF,text = 'custom',variable = self.linktype_Radio,value = 5,state = 'disabled')
        random_chkbox = Checkbutton(self.SendLink_LF,text = 'Random!',variable = self.linktype_Random,onvalue = 1,offvalue =0)
        #genl_link_BUT = Button(self.SendLink_LF,text = 'generate a link',command = self.linkgenner)
        pick_link_BUT = Button(self.SendLink_LF,text = 'PICK!',command = self.linkpicker)
        pick_link_LBL = Label(self.SendLink_LF,text = 'your link:')
        picked_link_LBL = Label(self.SendLink_LF,text = '',textvariable = self.gennedlink)

        sublink_BUT = Button(self.This_win,text = 'submit',command = self.sublink_proc)

        self.votelink_LF = LabelFrame(self.This_win,text = 'vote')
        votelink_LF_LBL = Label(self.votelink_LF,text ='pick a link')
        votelink_refresh_BUT = Button(self.votelink_LF,text =' refresh entries',command = self.regetlinks)

        link1_radio = Radiobutton(self.votelink_LF,text = "player1's link",variable = self.linkvote_Radio,value = 1)
        link2_radio = Radiobutton(self.votelink_LF,text = "player2's link",variable = self.linkvote_Radio,value = 2)
        link3_radio = Radiobutton(self.votelink_LF,text = "player3's link",variable = self.linkvote_Radio,value = 3)
        link4_radio = Radiobutton(self.votelink_LF,text = "player4's link",variable = self.linkvote_Radio,value = 4)
        link5_radio = Radiobutton(self.votelink_LF,text = "player5's link",variable = self.linkvote_Radio,value = 5)
        link6_radio = Radiobutton(self.votelink_LF,text = "player6's link",variable = self.linkvote_Radio,value = 6)

       ## link1_lbl = Label(self.votelink_LF,text = "player1's link",variable = self.linkvote_Radio,value = 1)
       ## link2_lbl = Label(self.votelink_LF,text = "player2's link",variable = self.linkvote_Radio,value = 2)
       ## link3_lbl = Label(self.votelink_LF,text = "player3's link",variable = self.linkvote_Radio,value = 3)
       ## link4_lbl = Label(self.votelink_LF,text = "player4's link",variable = self.linkvote_Radio,value = 4)
       ## link5_lbl = Label(self.votelink_LF,text = "player5's link",variable = self.linkvote_Radio,value = 5)
       ## link6_lbl = Label(self.votelink_LF,text = "player6's link",textvariable = self.linkvote_Radio,value = 6)

        misc_LF = LabelFrame(self.This_win,text = 'misc')
        self.ADMIN_closesession_BUT = Button(misc_LF,text = 'ADMIN Close\nsession',command = self.close_session,state = DISABLED)
        self.Leave_session_BTN = Button(misc_LF,text = 'leavesession\nsession', command = self.leavesession)

        #packing
        self.SendLink_LF.pack()
        tinyurl_radio.pack()
        bitly_radio.pack()
        googl_radio.pack()
        imgur_radio.pack()
        self.custom_radio.pack()
        random_chkbox.pack()
        pick_link_BUT.pack()
        pick_link_LBL.pack()
        picked_link_LBL.pack()

        sublink_BUT.pack()

        self.votelink_LF.pack()
        votelink_LF_LBL.pack()
        votelink_refresh_BUT.pack()
        link1_radio.pack()
        link2_radio.pack()
        link3_radio.pack()
        link4_radio.pack()
        link5_radio.pack()
        link6_radio.pack()

        misc_LF.pack()
        self.ADMIN_closesession_BUT.pack()
        
        ##end
        Menu_main = Menu(self.This_win)
        Menu_help = Menu(Menu_main,tearoff = 0)
        #Menu_settings = Menu(menubar, tearoff=0)
        Menu_help.add_command(label="MP help", command=Class_Win_MP_Howto.Window)##mp at top as more relavent to this window
        Menu_help.add_command(label="SP help", command=Class_Win_Howto.Window)
        Menu_main.add_cascade(label = 'How To',menu = Menu_help)
      
        Menu_settings = Menu(Menu_main,tearoff = 0)
        Menu_settings.add_command(label="custom link", command=Class_Win_MP_Customchoose.Menu_customchoose_window,state = DISABLED)
        Menu_main.add_cascade(label = 'settings',menu = Menu_settings)
        Menu_main.add_command(label = 'game info', command = Class_Win_MP_mpgameinfo.Window_Main)

        self.This_win.config(menu=Menu_main)#title = 'Link Roulette'
        #self.This_win.title('Link Roulette')
        #self.This_win.geometry('305x300')
        ##preloading/preloop
        self.do_Setup()

        self.This_win.after(700, self.event_TED)
        #print('test')
        self.This_win.mainloop()
    def __del__(self):
        if Setting.InGame == True:
            self.leavesession()

    def event_TED(self):
        ##print(self.gennedlink.get())
        ##print(self.linktype_Radio.get())
        gamestate = str(Ted_Network.URL_request_State(Setting.gpin))
        print('state:',gamestate)
        gamestate = str(gamestate[0])
        if gamestate == '0':
            pass
        elif gamestate == '1':
            pass
        elif gamestate == '2':
            pass
        elif gamestate == '3':
            pass
        elif gamestate == '4':
            pass
        else:
            print('gamestate error')
        ##move into gamestate bracket when done
        self.regetlinks()
        ##

        self.This_win.after(700, self.event_TED)

    def do_Setup(self):##preloop stuff
        self.disable_voting()
        if Setting.ADMIN == True:
            self.This_win.title('Link Roulette - Session Admin')#add id to this
            self.ADMIN_closesession_BUT.config(state = 'normal')

    def linkpicker(self):
        #global settings
        button_num = 4
        #global custom_radio
        #if self.linktype_Random.get() == 1:
        #    #if custom_radio ==
        #    print('settings[3] == '+str(Setting.settings[3]))
        #    if Setting.settings[3] == '1':
        #        self.linktype_Radio.set(random.randint(1,(button_num+1)))
        #    else:
        #        self.linktype_Radio.set(random.randint(1,button_num))##randomises the link(change values to allow for all radios(UPDATE)
        #        ##genlink()
        #
        if self.linktype_Radio.get() == 0:
            pass
            ##print('skipped generation')

        else:
            ##if linktype_Radio.get() == -1:
                ##linktype_Radio.set(random.randint(1,3))##randomises the link(change values to allow for all radios(UPDATE)
                ##genlink()
            if self.linktype_Radio.get()   ==  1:
                self.gennedlink.set(Ted_Links.get_tinyurl())##eg http://tinyurl.com/DlJzJ
            elif self.linktype_Radio.get() ==  2:
                self.gennedlink.set(Ted_Links.get_BitLy())
            elif self.linktype_Radio.get() ==  3:
                self.gennedlink.set(Ted_Links.get_googl())
            elif self.linktype_Radio.get() ==  4:
                self.gennedlink.set(Ted_Links.get_imgur())
            elif self.linktype_Radio.get() ==  5:
                self.gennedlink.set(Ted_Links.get_custom())
            #print(self.gennedlink.get())

            #if int(Setting.settings[1]) == 1:##skips saving link to array and disk
            #    print('skipped saving history')
            #else:
            #    self.history.append(self.gennedlink.get())
            #    self.save_history()
            #self.linkbox_Label.config(text = str(self.gennedlink.get()))
            #self.refresh_Hbox()

    def enable_voting(self):##enable voting widgets
        print('enabled!')
        for child in self.votelink_LF.winfo_children():
            child.configure(state='normal')

    def disable_voting(self):##disable voting widgets
        print('disabled!')
        for child in self.votelink_LF.winfo_children():
            child.configure(state='disable')

    def enable_gen(self):##enable genning widgets
        print('enabled!')
        for child in self.SendLink_LF.winfo_children():
            child.configure(state='normal')

    def disable_gen(self):##disable genning widgets
        print('disabled!')
        for child in self.SendLink_LF.winfo_children():
            child.configure(state='disable')

    def sublink_proc(self):
        sub = Ted_Network.URL_sublink(Setting.gpin,Setting.ppin,self.gennedlink.get())
        print('subdat',sub)
        if self.gennedlink.get() == '':
            #pass
            print('error:!nolink!')
        elif sub[0] == 'ERROR':
            print('error with link\nEDAT==========================\n')
            print(sub)
        #else:
        elif sub[0].upper() == 'S':
            self.disable_gen()
            self.enable_voting()
            print('sub sucess!!')
        else:
            print('error occurred')
            print('sub',sub)

    def regetlinks(Self):
        pass

    def openrng(self):##button funct
        #global gennedlink
        #global settings
        print('link = ',self.gennedlink.get())
        #0 = prompt
        print(Setting.mp_prompt)
        #if int(Setting.settings[0]) == 1:##functionise instead?
        if Setting.mp_prompt == False:
            print('no prompt')
            webbrowser.open(self.gennedlink.get())
        
        else:
            if messagebox.askokcancel(title = 'confirm open',message = 'are you sure\nthere is NO guaruntee the link will be safe!'):
                webbrowser.open(self.gennedlink.get())

    def close_session(self):
        Ted_Network.URL_closesession(Setting.gpin,Setting.apin)
        self.This_win.destroy()

    def process_newround(self):
        Class_Win_MP_Lobby.Win_MP_Lobby()##temp logical will replace with rejoin screen
        self.This_win.destroy()
    
    def leavesession(self):
        if Setting.ADMIN == True:
            if messagebox.askokcancel('Are you sure?','CLose session by leaving?'):
                pass
        else:

            if messagebox.askokcancel('Are you sure?','leave session?'):
                leave_DBG = Ted_Network.URL_leavegame(Setting.gpin,Setting.ppin)
                print('left session: data',leave_DBG)
                self.This_win.destroy()





##Win_Main_MP()##testing
