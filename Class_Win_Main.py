import random,webbrowser,os
from tkinter import *
from tkinter import messagebox

##windows
#options menu wins
import Class_Win_Options, Class_Win_Customchoose
#help menu wins
import Class_Win_Howto
#
##end

#ted misc
import Ted_Qfile

class Win_Main:
    FILE_HISTORY = 'history.dat'
    vchars = [ '0', '1', '2', '3', '4', '5', '6', '7', '8', '9','A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L','M','N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    history = []
    #settings in order Warn_Skiplink , History_Track , Session_History , custom button enabled?
    settings = []
    ##settings do double check when adding new settings that every setting is added in all the procs properly
    #Menu_settings_window_DATA = []##global datastore for settings window maynot need as objectified
    root = Tk()
    linktype_Radio = IntVar()
    linktype_Random = IntVar()
    gennedlink = StringVar()

    def __init__(self):
        ol_LF = LabelFrame(self.root,text = 'open link')##openlink
        s_ol_LF  = LabelFrame(self.root,text = 'link')##openlink subframe forlink buttons
        lr_LF = LabelFrame(self.root,text = 'pick a link type')##linkradio
        hb_LF = LabelFrame(self.root,text = 'link history')##historybox
        ms_LF = LabelFrame(self.root,text = 'misc functions')##misc
        historyscroller_Scrollbar = Scrollbar(hb_LF)
        self.history_Listbox = Listbox(hb_LF,yscrollcommand = historyscroller_Scrollbar.set)
        historyscroller_Scrollbar.config(command = self.history_Listbox.yview)

        tinyurl_radio = Radiobutton(lr_LF,text = 'tinyurl',variable = self.linktype_Radio,value = 1)
        bitly_radio = Radiobutton(lr_LF,text = 'Bit.ly',variable = self.linktype_Radio,value = 2)
        googl_radio = Radiobutton(lr_LF,text = 'goo.gl',variable = self.linktype_Radio,value = 3)
        imgur_radio = Radiobutton(lr_LF,text = 'imgur',variable = self.linktype_Radio,value = 4)
        custom_radio = Radiobutton(lr_LF,text = 'custom',variable = self.linktype_Radio,value = 5,state= 'disabled')
        random_chkbox = Checkbutton(lr_LF,text = 'Random!',variable = self.linktype_Random,onvalue = 1,offvalue =0)
        genlnk_Button = Button(ol_LF,command = self.genlink,text = 'generate\nlink')
        openlnk_Button = Button(ol_LF,command = self.openrng,text = 'open\nlink')
        opengoogle_Button = Button(ms_LF,command = self.googlehome,text = 'google homepage')
        selectlink_Button = Button(hb_LF,command = self.setlink,text = 'select link')
        clearhistory_Button  = Button(ms_LF,command = self.clearhistory,text = 'clear history')
        linkbox_Label = Label(s_ol_LF)


        buff = [5,5]##pixel edge buffer/offset
        lr_LF.place(x = buff[0]+ 0,y = buff[1]+ 0)#.pack()              ###PACK CHANGED TO PLACE UNCONFIGGED!!!
        ol_LF.place(x = buff[0]+ 75,y = buff[1]+ 250)#.pack()
        hb_LF.place(x = buff[0]+ 150,y = buff[1]+ 0)#.pack()
        ms_LF.place(x = buff[0]+ 0,y = buff[1]+ 175)#.pack()
        s_ol_LF.place(x = buff[0]+ 115,y = buff[1]+ 315)


        tinyurl_radio.pack()
        bitly_radio.pack()
        googl_radio.pack()
        imgur_radio.pack()
        custom_radio.pack()
        random_chkbox.pack()
        genlnk_Button.pack(side = LEFT)
        openlnk_Button.pack(side = LEFT)
        opengoogle_Button.pack()
        selectlink_Button.pack()
        clearhistory_Button.pack()
        linkbox_Label.pack(side = BOTTOM)
        self.history_Listbox.pack(side = LEFT)
        historyscroller_Scrollbar.pack(side = RIGHT,fill = Y)

        Menu_main = Menu(self.root)
        Menu_settings = Menu(Menu_main,tearoff = 0)
        #Menu_settings = Menu(menubar, tearoff=0)
        Menu_settings.add_command(label="options", command=Class_Win_Options.Menu_settings_window)
        Menu_settings.add_command(label="custom link", command=Class_Win_Customchoose.Menu_customchoose_window)
        Menu_main.add_cascade(label = 'options',menu = Menu_settings)
        #Menu_main.add_command(label="preview", command=Menu_preview_window)
        self.on_run()
        self.root.config(menu=Menu_main)#title = 'Link Roulette'
        self.root.title('Link Roulette')
        self.root.geometry('305x300')
        self.root.after(2000, self.event_TED)
        self.root.mainloop()
        on_close()

    def openrng(self):##button funct
        #global gennedlink
        #global settings
        print('link = ',self.gennedlink.get())
        #0 = prompt
        print(self.settings[0])
        if int(self.settings[0]) == 1:##functionise instead?
            print('no prompt')
            webbrowser.open(self.gennedlink.get())
        
        else:
            if messagebox.askokcancel(title = 'confirm open',message = 'are you sure\nthere is NO guaruntee the link will be safe!'):
                webbrowser.open(self.gennedlink.get())
        
    
    def googlehome():##button funct
        webbrowser.open('google.co.uk')


    def save_file(self,name,data,overwrite = False,array = False):#saving funct
        if overwrite:
            f = open(name,'r+')
        else:
            f = open(name,'w')
        if array:
            for x in data:
                f.write(x+'\n')
        else:
            for x in data:
                f.write(x)
        f.close()


    def loadfile(self,name):##loading funct
        contents = []
        f = open(name,'r')
        for x in f.readlines():
            contents.append(x.strip('\n'))
        f.close()
        return contents

    def array2csv(self,array):##from beelib
            temp = ''
            for fl in array:
                print(fl)
                temp += str(fl)+','
            temp+=','
            return temp
    
    def csv2array(self,csvstr):##may need os.isfile() or whatever it is to check file is in dir before declaring eofsame for array2csv      ##from beelib
        arrayreturn = []
        temp = ''
        flag = False
        for x in csvstr:#range(len(csvnames)):
            if flag and (x==','):## ,, delimiter
                break
            if x ==',':
                arrayreturn.append(temp)
                temp = ''
                flag = True
            else:
                temp+=x
                flag = False
        return arrayreturn

    def load_history_ext(self):##unused
        #global history
        if askokcancel():
            self.history = self.loadfile(self.FILE_HISTORY)
        
    ##temp here till beelib sorted out should'nt be here
    def csv2dot(self,strng):##replaces , with . char for  sub 'csvising them'
        temp = ''
        for x in range(len(strng)):
            if strng[x] == ',':
                temp += '.'
            else:
                temp += strng[x]
        return temp

    def dot2csv(self,strng):##replaces . with , char for  sub 'uncsvising them'
        temp = ''
        for x in range(len(strng)):
            if strng[x] == '.':
                temp += ','
            else:
                temp += strng[x]
        return temp
    ##END

    def load_history(self):
        #global history
        if self.FILE_HISTORY in os.listdir():
            history = self.loadfile(self.FILE_HISTORY)
        else:
            save_file(FILE_HISTORY,['the history file'])

    
    def save_history(self):
        #global history
        #global settings
        print(self.settings[2])
        if int(self.settings[2]) == 1:
            print('not saving to disk')
        else:
            save_file(self.FILE_HISTORY,self.history,array = True)

    def refresh_Hbox(self):##refreshes listbox to update it
        self.history_Listbox.delete(0,self.history_Listbox.size())
        for x in self.history:
            self.history_Listbox.insert(END,x)

        
    def clearhistory(self):##temp clears urlbox
        if messagebox.askokcancel(title = 'confirm clear',message = 'delete your history?'):
            save_file(self.FILE_HISTORY,['the history file'],overwrite = False)
            self.history_Listbox.delete(0,self.history_Listbox.size())
            self.refresh_Hbox()
            print('cleared')
        else:
            print('no')
    
    def loadsettings(self):##the custom button is only checked on load time currently whether it should be added to the random pool and nowhere else
        #global settings
        #global custom_radio
        print('loading settings...')
        if 'SETTINGS.CFF' in os.listdir():##my add as a function instead(exists checker)
            f = open('SETTINGS.CFF','r+')
            data = self.csv2array(f.readline())
            f.close()
            #print(data)
            self.settings = data
            print ('loaded: ',data)
        if 'CUSTOM.CLF' in os.listdir():
            f = open('CUSTOM.CLF','r')
            dat = f.readline()
            f.close()
            #print(dat)
            data = self.csv2array(dat)##to solve type prob
            print(data)
            print('enabled custom: '+data[4])
            if str(data[4]) == '1':
                self.custom_radio.configure(state = 'normal')
                print('dat[4] = normal')
            else:
                self.custom_radio.configure(state = 'disabled')
        
            print(self.settings)
            self.settings.append(str(data[4]))
            print(self.settings)
            
        

    def genlink(self):##button funct
        #global settings
        button_num = 4
        #global custom_radio
        if self.linktype_Random.get() == 1:
            #if custom_radio ==
            print('settings[3] == '+str(self.settings[3]))
            if self.settings[3] == '1':
                self.linktype_Radio.set(random.randint(1,(button_num+1)))
            else:
                self.linktype_Radio.set(random.randint(1,button_num))##randomises the link(change values to allow for all radios(UPDATE)
                ##genlink()
        
        if self.linktype_Radio.get() == 0:
            pass

        else:
            ##if linktype_Radio.get() == -1:
                ##linktype_Radio.set(random.randint(1,3))##randomises the link(change values to allow for all radios(UPDATE)
                ##genlink()
            if self.linktype_Radio.get()   ==  1:
                self.gennedlink.set(self.get_tinyurl())##eg http://tinyurl.com/DlJzJ
            elif self.linktype_Radio.get() ==  2:
                self.gennedlink.set(self.get_BitLy())
            elif self.linktype_Radio.get() ==  3:
                self.gennedlink.set(self.get_googl())
            elif self.linktype_Radio.get() ==  4:
                self.gennedlink.set(self.get_imgur())
            elif self.linktype_Radio.get() ==  5:
                self.gennedlink.set(self.get_custom())
            
            if int(self.settings[1]) == 1:##skips saving link to array and disk
                print('skipped saving history')
            else:
                self.history.append(self.gennedlink.get())
                self.save_history()
            self.linkbox_Label.config(text = str(self.gennedlink.get()))
            self.refresh_Hbox()

        
    def setlink(self):
        #global history_listbox
        if self.history_Listbox.curselection() == None:##checks if valid
            pass
        else:
            self.gennedlink.set(self.history_Listbox.get(self.history_Listbox.curselection()))
            self.linkbox_Label.config(text = str(self.gennedlink.get()))


    def get_tinyurl(self):   
        link = ''
        leng = random.randint(4,6)#4-6 chars
        for x in range(0,leng):
            link+=vchars[random.randint(0,len(vchars))]
        return 'http://tinyurl.com/'+link


    def get_BitLy(self):
        link = ''
        leng = random.randint(4,6)#4-6 chars
        for x in range(0,leng):##can be longer as https://bit.ly/zzzzzzzzzzzzzzzzz is valid
            link+=vchars[random.randint(0,len(vchars))]
        return 'http://bit.ly/'+link


    def get_googl(self):
        link = ''
        leng = 7##7 imgur has fixed 7charsrandom.randint(4,6)#4-6 chars
        for x in range(0,leng):
            link+=vchars[random.randint(0,len(vchars))]
        return 'http://goo.gl/'+link

    ##image sites
    def get_imgur(self):
        link = ''
        leng = random.randint(4,7)#4-6 chars
        for x in range(0,leng):##can be longer as https://bit.ly/zzzzzzzzzzzzzzzzz is valid
            link+=vchars[random.randint(0,len(vchars))]
        return 'http://i.imgur.com/'+link##+'.jpg'##check format may need detecting from file

    ##custom
    def get_custom(self):##youtube thing bndPy1MHm8E
        f = open('CUSTOM.CLF','r')
        dat = f.readline()
        f.close()
        data = self.csv2array(dat)##to solve type prob
        print('//##//\n',data,'\n\\##\\')
        #data = csv2array(dat)
        print(data[3])
        print(self.dot2csv(data[3]))
        data[3] = self.csv2array(self.dot2csv(data[3]))
        print('\n\n//##//\n',data,'\n\\##\\')
        enabled = data[4]
        if enabled  == 1 or '1':
            link = ''
            leng = random.randint(int(data[2]),int(data[1]))#chars
            for x in range(0,leng):##can be longer as https://bit.ly/zzzzzzzzzzzzzzzzz is valid
                link+=data[3][random.randint(0,len(vchars))]
            return data[0]+link##+'.jpg'##check format may need detecting from file
    
    def on_run(self):##bootup setup
        self.load_history()
        self.refresh_Hbox()
        self.loadsettings()

    
    def on_close(self):##cleanup on close
        #save_history()##better to save direct
        print('cleanup')
    
    
    def asciidump_ext(self):
        chrs = []
        for x in range(0,255):
            chrs.append(str(chr(x)))
        return chrs


    #def genrandom():#save_file(name,data,overwrite = False,array = False)
    #    pass ##implemented in class

    ##def Menu_settings_window():
    ##    global self.root
    ##    #global Menu_settings_window_DATA
    ##    Warn_Skiplink = IntVar()
    ##    
    ##    optionsmenu = Toplevel()
    ##    OCL = LabelFrame(optionsmenu,text = 'toggle options')##options_Checkboxes_labelframe
    ##    OBL = LabelFrame(optionsmenu,text = 'buttons')##options_buttons_labelframe
    ##    
    ##    SKIPWARN_check = Checkbutton(OCL,text = 'skip openbox on link open',variable = Warn_Skiplink,onvalue = 1,offvalue =0)
    ##    KEEPHISTORY_checks = Checkbutton(OCL,text = 'keep history',variable = Warn_Skiplink,onvalue = 1,offvalue =0)
    ##
    ##    OCL.pack()
    ##    OBL.pack()
    ##
    ##    SKIPWARN_check.pack()
    ##    KEEPHISTORY_checks.pack()
    ##
    ##    #self.root.config()
    ##    optionsmenu.title('options')
    ##    optionsmenu.mainloop()
    ##
    ##def Menu_settings_savesettings():
    ##    #global Menu_settings_window_DATA

    
    
    


    def event_TED(self):##custom event loop
        ##event code here##
    
        ##END EVENT CODE##
        self.root.after(700, self.event_TED)


    

