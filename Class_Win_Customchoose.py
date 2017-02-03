import os
from tkinter import *
import Ted_Qfile
class Menu_customchoose_window:
    customlinkmenu = Toplevel#()##actualy inits in __init__ atm

    Custom_linkprefix = StringVar()
    Custom_linklen = StringVar()#IntVar()##length of link
    Custom_linkstart = StringVar()#IntVar()##inclusive position start of rng link so linklen = 6 linkstart = 4 so random.rng(4,6)
    Custom_charset = StringVar()##csv input string for custom chars
    Custom_enable = IntVar()
    
    cls = Ted_Qfile.customfile_prog()##customlinkstorage ##data for the custom link
    clf = Ted_Qfile.customlinkfile_prog()##custom link quick load file

    ##defs
    Custom_charset.set('0,1,2,3,4,5,6,7,8,9,A,B,C,D,E,F,G,H,I,J,K,L,M,N,O,P,Q,R,S,T,U,V,W,X,Y,Z,a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u,v,w,x,y,z,,')
    EVENTLOOP_TIC = 700
    ##END
    
    #hacky globals
    #customlinkmenu = ''##menu hacky global tkstuff
    LLF= '' #hacky global ##could assign locally on init within so self llf becomes llfsub/something
    #prefixcustom_entry=''
    #lowerlimitrng_entry = ''
    #upperlimitrng_entry = ''
    #charset_entry = ''
    #END
    
    def __init__(self):
        self.customlinkmenu()
        self.loadcustomlink_settings()
        
        CLF = LabelFrame(self.customlinkmenu,text = 'custom link')##Custom Label Frame
        self.LLF = LabelFrame(self.customlinkmenu,text = 'custom link creation')##Link Label Frame
        CPL = LabelFrame(self.customlinkmenu,text = 'custom link presets')##Custom Preset Link

        EnableCL_button = Checkbutton(CLF,text = 'enable custom link',variable = self.Custom_enable,onvalue = 1,offvalue =0)##EnableCustomLink_button
        savesettings_button = Button(CLF,text = 'save settings',command = self.savecustomlink_settings)

        prefixcustom_entry = Entry(self.LLF,textvariable = self.Custom_linkprefix)
        prefixcustom_entry_label = Label(self.LLF,text = 'link prefix')
        lowerlimiting_entry = Entry(self.LLF,textvariable = self.Custom_linkstart)
        lowerlimiting_entry_label = Label(self.LLF,text = 'lower range rng')
        upperlimiting_entry = Entry(self.LLF,textvariable = self.Custom_linklen)
        upperlimiting_entry_label = Label(self.LLF,text = 'upper range rng')
        charset_entry = Entry(self.LLF,textvariable = self.Custom_charset)
        charset_entry_label = Label(self.LLF,text = 'rng charset(CSV)')##print(array2csv(vchars))
        charset_default_button = Button(self.LLF,text = 'default charset',command = self.Custom_resetcharset)
        #savesettings_button = Button(self.LLF,text = 'save settings',command = savecustomlink_settings)

        #custompresetchooser_listbox
        custompresetchooser_listbox_Scrollbar = Scrollbar(CPL)
        custompresetchooser_listbox = Listbox(CPL,yscrollcommand = custompresetchooser_listbox_Scrollbar.set)
        custompresetchooser_listbox_Scrollbar.config(command = custompresetchooser_listbox.yview)
        custompresetchooser_Load = Button(CPL,command = self.load_presetdata,text = 'load preset')
        custompresetchooser_Save = Button(CPL,command = self.save_presetdata,text = 'save preset as new/update selected')
        custompresetchooser_Delt = Button(CPL,command = self.delt_presetdata,text = 'delete selected preset')


        ##setting up
        #self.Custom_charset.set('0,1,2,3,4,5,6,7,8,9,A,B,C,D,E,F,G,H,I,J,K,L,M,N,O,P,Q,R,S,T,U,V,W,X,Y,Z,a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u,v,w,x,y,z,,')
        ##END
        CLF.pack()
        self.LLF.pack()
        CPL.pack()

        EnableCL_button.pack()
        savesettings_button.pack()
        
        prefixcustom_entry_label.pack()
        prefixcustom_entry.pack()
        lowerlimiting_entry_label.pack()
        lowerlimiting_entry.pack()
        upperlimiting_entry_label.pack()
        upperlimiting_entry.pack()
        charset_entry_label.pack()
        charset_entry.pack()
        charset_default_button.pack()

        custompresetchooser_listbox.pack()
        custompresetchooser_listbox_Scrollbar.pack()
        custompresetchooser_Load.pack()
        custompresetchooser_Save.pack()
        custompresetchooser_Delt.pack()

        
        #root.config()
        self.customlinkmenu.title('custom link creation')
        self.customlinkmenu.after(self.EVENTLOOP_TIC, self.event_TED)

        self.disable_custom()##disable at start
        #self.checkstate_custom()
        self.loadcustomlink_settings()
        self.customlinkmenu.mainloop()
        
    def event_TED(self):##custom event loop
        ##event code here##
        
        #print('test')
        ##hacky stuffWILLFIX LATER

##        print(self.prefixcustom_entry.get(),
##        self.lowerlimitrng_entry.get(),
##        self.upperlimitrng_entry.get(),
##        self.charset_entry.get())
##        
##        self.Custom_linkprefix.set(self.prefixcustom_entry.get())
##        self.Custom_linklen.set(self.lowerlimitrng_entry.get())##length of link
##        self.Custom_linkstart.set(self.upperlimitrng_entry.get())##inclusive position start of rng link so linklen = 6 linkstart = 4 so random.rng(4,6)
##        self.Custom_charset.set(self.charset_entry.get())##csv input string for custom chars
        print(self.Custom_enable.get())
        if self.Custom_enable.get() == 1:
            self.enable_custom()
        else:
            self.disable_custom()
        ##END EVENT CODE##
        self.customlinkmenu.after(self.EVENTLOOP_TIC, self.event_TED)
        
    def enable_custom(self):
        print('enabled!')
        for child in self.LLF.winfo_children():
            child.configure(state='normal')
    def disable_custom(self):
        print('disabled!')
        for child in self.LLF.winfo_children():
            child.configure(state='disable')
            
    def checkstate_custom(self):##checks in settings for if enabled
        ###NOTNEEDED IGNORE here  for refrence
        dat = self.csv2array(cls.get_data())
        prefix = dat[0]
        rngrangelen = dat[1]

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

    def savecustomlink_settings(self):
        global custom_radio
        global settings
        dat2sav = self.getsettings()
        print('~~~~####~~~~####~~~~')
        print(dat2sav)##check array handlingstuff
        print(self.csv2dot('0,1,2,3,4,5,6,7,8,9,A,B,C,D,E,F,G,H,I,J,K,L,M,N,O,P,Q,R,S,T,U,V,W,X,Y,Z,a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u,v,w,x,y,z,,'))
        print('~~~~####~~~~####~~~~')
        dat2sav[3] = self.csv2dot(dat2sav[3])
        self.cls.save_customdata(dat2sav)##data is csvised internally in fileclass so no csving needed here
        print('custom state = '+str(dat2sav[4]))
        if str(dat2sav[4]) == '1':
            custom_radio.configure(state = 'normal')
            csttg = '1'##customtoggle
        else:
            print('cstmst = disabled')
            custom_radio.configure(state = 'disabled')
            csttg = '0'
            
        try:
            settings[3] = csttg## if fail then append may be good idea to use 'variable type data in arrays E.G. ['Button_on = 1',"Test = '1'"] etc may help with id problems
        except:
            settings.append(csttg)
        
    def getsettings(self):
        returner = [
        self.Custom_linkprefix.get(),
        self.Custom_linklen.get(),
        self.Custom_linkstart.get(),
        self.Custom_charset.get(),
        self.Custom_enable.get()
        ]
        return returner
            
    def loadcustomlink_settings(self):
        #data = self.csv2array(self.cls.get_data())
        #print(data)

        ##manual load till fix
        if os.path.isfile('CUSTOM.CLF'):
            f = open('CUSTOM.CLF','r')
            data = f.readline()
            f.close()
            data = csv2array(data)
            print(data)
        ##END
        
            data[3] = self.dot2csv(data[3])
        
            self.Custom_linkprefix.set(data[0])
            self.Custom_linklen.set(data[1])
            self.Custom_linkstart.set(data[2])
            self.Custom_charset.set(data[3])
            self.Custom_enable.set(data[4])
        else:
            print('file: CUSTOM.CLF not found!')
    def Custom_resetcharset(self):
        if messagebox.askokcancel(title = 'confirm reset',message = 'are you sure\nthis will reset the the charset box to the default value!'):
            self.Custom_charset.set('0,1,2,3,4,5,6,7,8,9,A,B,C,D,E,F,G,H,I,J,K,L,M,N,O,P,Q,R,S,T,U,V,W,X,Y,Z,a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u,v,w,x,y,z,,')
            print('RESET!')

    #######custom link files##
            ##preset.cbf is all preset configs
            ##preset.dat is quick load of a single setting file with 1 preset
            
    def Custom_loadpreset(self):##loads apreset file via tk.loadbox
        pass
    
    def Custom_load_presetfile(self):##loader and saver functons
        print('loading from preset.CPF')
        f = open('preset.CPF','r')
        dat = f.readlines().strip('\n')
        print(dat)
        f.close()
        print('loading DONE!')
    def Custom_save_presetfile(self):
        print('saving from preset.CPF')
        f = open('preset.CPF','w')
        for x in data:
            f.write(x+str('\n'))
        f.close()
        print('saving DONE!')
    def presetlist_update(self,dat):##refreshes listbox containing presets with dat  supplied in array form
        input('fgbjgujg')
        self.custompresetchooser_listbox.delete(0,self.custompresetchooser_listbox.size())
        for x in dat:
            self.custompresetchooser_listbox.insert(END,x)
            
    def load_presetdata(self):##load individual preset file
        print('loading from preset.dat')
        if os.path.isfile('PRESET.dat'):
            f = open('PRESET.dat','r')
            data = f.readline()
            f.close()
            data = csv2array(data)
            print(data)
        ##END
        
            data[3] = self.dot2csv(data[3])
        
            self.Custom_linkprefix.set(data[0])
            self.Custom_linklen.set(data[1])
            self.Custom_linkstart.set(data[2])
            self.Custom_charset.set(data[3])
            self.Custom_enable.set(data[4])

            self.savecustomlink_settings()##'saves' the preset
            
    def save_presetdata(self):##C+p of savesettings atm nned to change ##sae individual preset file
        print('saving to preset.dat...')
        global custom_radio
        global settings
        dat2sav = self.getsettings()
        if os.path.isfile('PRESET.dat'):
            if messagebox.askokcancel(title = 'confirm save',message = 'are you sure?\n this will overwrite your existing quickpreset file!'):
                dat2sav[3] = self.csv2dot(dat2sav[3])
                self.clf.save_customdata(dat2sav)##data is csvised internally in fileclass so no csving needed here
                print('custom state = '+str(dat2sav[4]))
                if str(dat2sav[4]) == '1':
                    custom_radio.configure(state = 'normal')
                    csttg = '1'##customtoggle
                else:
                    print('cstmst = disabled')
                    custom_radio.configure(state = 'disabled')
                    csttg = '0'
                    
                try:
                    settings[3] = csttg## if fail then append may be good idea to use 'variable type data in arrays E.G. ['Button_on = 1',"Test = '1'"] etc may help with id problems
                except:
                    settings.append(csttg)
        else:##same again as only ask to replace
            dat2sav[3] = self.csv2dot(dat2sav[3])
            self.clf.save_customdata(dat2sav)##data is csvised internally in fileclass so no csving needed here
            print('custom state = '+str(dat2sav[4]))
            if str(dat2sav[4]) == '1':
                custom_radio.configure(state = 'normal')
                csttg = '1'##customtoggle
            else:
                print('cstmst = disabled')
                custom_radio.configure(state = 'disabled')
                csttg = '0'
                
            try:
                settings[3] = csttg## if fail then append may be good idea to use 'variable type data in arrays E.G. ['Button_on = 1',"Test = '1'"] etc may help with id problems
            except:
                settings.append(csttg)
        print('DONE!')
                    
    def delt_presetdata(self):##delete preset file
        if os.path.isfile('PRESET.dat'):
            pass
        self.Custom_load_presetfile()
    ##end customfile
    ###these really shouldnt be here..
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
    ###