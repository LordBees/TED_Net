##tkinter
from tkinter import *
##tedutils
import Ted_Network as net
import Ted_Settings as Setting

class Admin_Win:
    ##

    ##
    def __init__(self):
        self.msb = Toplevel()
        self.msb_Gpin_VAR = StringVar()
        self.msb_Apin_VAR = StringVar()
        self.ERR_VAR = StringVar()

        msb_LF = LabelFrame(self.msb,text = 'your game pin and admin code')
        msb_gp_LBL = Label(msb_LF,textvariable = self.msb_Gpin_VAR)
        msb_gp_ENT = Entry(msb_LF,textvariable = self.msb_Gpin_VAR)
        msb_gp_inf_LBL = Label(msb_LF,text = 'game pin:')

        msb_ap_LBL = Label(msb_LF,textvariable = self.msb_Apin_VAR)
        msb_ap_ENT = Entry(msb_LF,textvariable = self.msb_Apin_VAR)
        msb_ap_inf_LBL = Label(msb_LF,text = 'admin pin:')

        msb_Launch_BUT = Button(self.msb,text = 'launch as admin')##disabled atm
        self.msb_ADMIN_BUT = Button(self.msb,text = 'Set as admin of session',command = self.SET_ADMIN_MODE,state = 'disabled')#
        msb_ERR_LBL = Label(msb_LF,textvariable = self.ERR_VAR)


        msb_gp_inf_LBL.pack()
        msb_gp_LBL.pack()
        msb_gp_ENT.pack()

        msb_ap_inf_LBL.pack()
        msb_ap_LBL.pack()
        msb_ap_ENT.pack()

        self.msb_ADMIN_BUT.pack()
        msb_ERR_LBL.pack()
        msb_LF.pack()

        resp = net.URL_request_Gen()

        if resp[0] == 'ERROR' or (resp[0] == 'F'):
            #pass#do error label code here
            self.ERR_VAR.set('FAILED RESPONSE!')
        elif resp[0].upper() == 'S':
            print('Got AP+GP')
            self.msb_Gpin_VAR.set(resp[1])
            self.msb_Apin_VAR.set(resp[2])
            self.msb_ADMIN_BUT.config(state = 'normal')
            #Setting.apin = 
        else:
            print('mysterious failure!')
        #self.msb.after(700,self.Event_TED)
        self.msb.mainloop()
    #def Event_TED(self):
    #    if 

    def SET_ADMIN_MODE(self):
        Setting.ADMIN = True
        Setting.apin = self.msb_Apin_VAR.get()
        Setting.gpin = self.msb_Gpin_VAR.get()
        self.ERR_VAR.set('ADMIN MODE')
        #self.msb.destroy()