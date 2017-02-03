from tkinter import *
class Menu_settings_window:
    optionsmenu = Toplevel()

    Warn_Skiplink = IntVar()##settings[0]
    History_Track = IntVar()##settings[1]
    Session_History = IntVar()##settings[2]
    SETTINGS_filename = 'SETTINGS.CFF'
    
    def __init__(self):
        #self.optionsmenu()

        self.Menu_settings_loadsettings()
        
        
        OCL = LabelFrame(self.optionsmenu,text = 'toggle options')##options_Checkboxes_labelframe
        OBL = LabelFrame(self.optionsmenu,text = 'buttons')##options_buttons_labelframe
        
        SKIPWARN_check = Checkbutton(OCL,text = 'skip openbox on link open',variable = self.Warn_Skiplink,onvalue = 1,offvalue =0)
        KEEPHISTORY_checks = Checkbutton(OCL,text = "DON'T keep history",variable = self.History_Track,onvalue = 1,offvalue =0)
        SESSIONHISTORY_checks = Checkbutton(OCL,text = "dont save session to disk",variable = self.Session_History,onvalue = 1,offvalue =0)
        
        SAVESETTINGS_button = Button(OBL,text = 'Save settings',command = self.Menu_settings_savesettings)##'may be able to put into eventloop a check for the changes
        WIPESETTINGS_button = Button(OBL,text = 'clear settings',command = self.Menu_settings_wipesettings)
        WIPEALLDATA_button = Button(OCL,text = "DEFAULT SETTINGS",command = self.menu_settings_default)
        
        OCL.pack()
        OBL.pack()

        SKIPWARN_check.pack()
        KEEPHISTORY_checks.pack()
        SESSIONHISTORY_checks.pack()

        SAVESETTINGS_button.pack()
        WIPESETTINGS_button.pack()
        WIPEALLDATA_button.pack()
        
        #root.config()
        self.optionsmenu.title('options')
        self.optionsmenu.mainloop()
        
    def Menu_settings_loadsettings(self):
        if 'SETTINGS.CFF' in os.listdir():
            f  = open(self.SETTINGS_filename,'r+')
            data = self.csv2array(f.readline())
            print(data)
            f.close()
            self.Warn_Skiplink.set(data[0])
            self.History_Track.set(data[1])
            self.Session_History.set(data[2])
            #print(data)

        else:
            print('file not found!')
            
        
    def Menu_settings_savesettings(self):##saves settings to SETTINGS.CFF
        #def save_file(name,data,overwrite = False,array = False):#saving funct
        data = self.array2csv(self.Menu_settings_getsettings())

        f = open(self.SETTINGS_filename,'w')
        f.write(data)
        #for x in data:
            #f.write(x+'\n')
        f.close()
        self.Menu_settings_loadsettings()#reload settings to memory to update
        
    def Menu_settings_getsettings(self):##return settings data
        returner = [
        self.Warn_Skiplink.get(),
        self.History_Track.get(),
        self.Session_History.get()
        ]
        print(returner)
        return returner ##returning print(returner) may also work dunno tho
    
    def Menu_settings_wipesettings(self):##Reset config file
    #def save_file(name,data,overwrite = False,array = False):#saving funct
        data = self.array2csv(([0]*len(settings)))

        f = open(self.SETTINGS_filename,'w')
        f.write(data)
        #for x in data:
            #f.write(x+'\n')
        f.close()
        self.Menu_settings_loadsettings()#reload settings to memory
        
    def menu_settings_default(self):##reset to default ALL files
        files = ['SETTINGS.CFF','CUSTOM.CLF','history.dat']
        if messagebox.askokcancel(title = 'confirm WIPE',message = 'are you sure\nthis will reset the historyfile\ncustomfile and settings to default!'):
            f = open('SETTINGS.CFF','w')
            f.write('0,0,0,,')
            f.close()
            f = open('CUSTOM.CLF','w')
            f.write('https://www.youtube.com/watch?v=,10,10,0.1.2.3.4.5.6.7.8.9.A.B.C.D.E.F.G.H.I.J.K.L.M.N.O.P.Q.R.S.T.U.V.W.X.Y.Z.a.b.c.d.e.f.g.h.i.j.k.l.m.n.o.p.q.r.s.t.u.v.w.x.y.z..,1,,')
            f.close()
            f = open('history.dat','w')
            f.write('The History File')
            f.close()##use mega for packing a backup?
        print('wipe complete')
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
