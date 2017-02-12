##main window for submitting a link to the server/gamestate
from tkinter import *

#help menu wins
import Class_Win_Howto,Class_Win_MP_Howto

#menus
import Class_Win_MP_Customchoose,Class_Win_MP_mpgameinfo

#ted misc
import Ted_Links

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
        #end

        ##widgets
        self.SendLink_LF = LabelFrame(self.This_win,text = 'random link generation')
        tinyurl_radio = Radiobutton(self.SendLink_LF,text = 'tinyurl',variable = self.linktype_Radio,value = 1)
        bitly_radio = Radiobutton(self.SendLink_LF,text = 'Bit.ly',variable = self.linktype_Radio,value = 2)
        googl_radio = Radiobutton(self.SendLink_LF,text = 'goo.gl',variable = self.linktype_Radio,value = 3)
        imgur_radio = Radiobutton(self.SendLink_LF,text = 'imgur',variable = self.linktype_Radio,value = 4)
        self.custom_radio = Radiobutton(self.SendLink_LF,text = 'custom',variable = self.linktype_Radio,value = 5,state = 'disabled')
        random_chkbox = Checkbutton(self.SendLink_LF,text = 'Random!',variable = self.linktype_Random,onvalue = 1,offvalue =0)
        pick_link_BUT = Button(self.SendLink_LF,text = 'PICK!',command = self.linkpicker)
        pick_link_LBL = Label(self.SendLink_LF,text = 'your link:')
        picked_link_LBL = Label(self.SendLink_LF,text = '',textvariable = self.gennedlink)

        sublink_BUT = Button(self.This_win,text = 'submit',command = self.sublink_proc)

        self.votelink_LF = LabelFrame(self.This_win,text = 'vote')
        votelink_LF_LBL = Label(self.votelink_LF,text ='pick a link')
        votelink_refresh_BUT = Button(self.votelink_LF,text =' refresh entries',command = self.regetlinks)

        misc_LF = LabelFrame(self.This_win,text = 'misc')

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

    def event_TED(self):
        ##print(self.gennedlink.get())
        ##print(self.linktype_Radio.get())
        self.This_win.after(700, self.event_TED)

    def do_Setup(self):##preloop stuff
        self.disable_voting()

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
        if self.gennedlink.get() == '':
            #pass
            print('error:!nolink!')
        else:
            self.disable_gen()
            self.enable_voting()

    def regetlinks(Self):
        pass

Win_Main_MP()##testing
