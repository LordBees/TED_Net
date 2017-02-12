##tk
from tkinter import *

#ted misc
import Ted_Settings as Setting

class Window_Main:
    ##

    ##
    def __init__(self):
        self.This_win = Toplevel()

        self.msb_Gpin_VAR = StringVar()
        self.msb_Apin_VAR = StringVar()
        self.msb_Gnam_VAR = StringVar()
        self.msb_Ppin_VAR = StringVar()
        
        msb_LF = LabelFrame(self.This_win,text = 'your session info')
        msb_gp_LBL = Label(msb_LF,textvariable = self.msb_Gpin_VAR)
        msb_gp_ENT = Entry(msb_LF,textvariable = self.msb_Gpin_VAR,state = DISABLED)
        msb_gp_inf_LBL = Label(msb_LF,text = 'game pin:')

        msb_ap_LBL = Label(msb_LF,textvariable = self.msb_Apin_VAR)
        msb_ap_ENT = Entry(msb_LF,textvariable = self.msb_Apin_VAR,state = DISABLED)
        msb_ap_inf_LBL = Label(msb_LF,text = 'admin pin:')

        msb_pn_LBL = Label(msb_LF,textvariable = self.msb_Gnam_VAR)
        msb_pn_ENT = Entry(msb_LF,textvariable = self.msb_Gnam_VAR,state = DISABLED)
        msb_pn_inf_LBL = Label(msb_LF,text = 'game username:')

        msb_pp_LBL = Label(msb_LF,textvariable = self.msb_Ppin_VAR)
        msb_pp_ENT = Entry(msb_LF,textvariable = self.msb_Ppin_VAR,state = DISABLED)
        msb_pp_inf_LBL = Label(msb_LF,text = 'player pin:')

        msb_LF.pack()

        msb_gp_inf_LBL.pack()
        msb_gp_LBL.pack()
        msb_gp_ENT.pack()

        msb_ap_inf_LBL.pack()
        msb_ap_LBL.pack()
        msb_ap_ENT.pack()

        msb_pn_inf_LBL.pack()
        msb_pn_LBL.pack()
        msb_pn_ENT.pack()

        msb_pp_inf_LBL.pack()
        msb_pp_LBL.pack()
        msb_pp_ENT.pack()

        self.This_win.after(700,self.TED_loop)
        self.This_win.mainloop()

    def TED_loop(self):
        self.msb_Gpin_VAR.set(Setting.gpin)
        self.msb_Apin_VAR.set(Setting.apin)
        self.msb_Gnam_VAR.set(Setting.pname)
        self.msb_Ppin_VAR.set(Setting.ppin)
        self.This_win.after(700,self.TED_loop)
##Window_Main()##testing