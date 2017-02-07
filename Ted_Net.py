##main initialisation
##http://bit.do/list-of-url-shorteners.php
##http://www.hongkiat.com/blog/url-shortening-services-the-ultimate-list/
import Class_Win_Main,Class_Win_MP_Lobby#,Class_Win_MP_Main
from tkinter import *
import os
## quick window for mp or sp
root = Tk()
root.title('TED Gamemode selector')
#root.geometry('300x100')
root.geometry('150x100')

def fs_check():
    #def menu_settings_default(self):##reset to default ALL files
    files = ['SETTINGS.CFF','CUSTOM.CLF','history.dat']
    #if messagebox.askokcancel(title = 'confirm WIPE',message = 'are you sure\nthis will reset the historyfile\ncustomfile and settings to default!'):
    print('file(s) generated: ',end = '')
    if  not os.path.isfile('SETTINGS.CFF'):
        print(',SETTINGS.CFF',end = '')
        f = open('SETTINGS.CFF','w')
        f.write('0,0,0,,')
        f.close()
    if  not os.path.isfile('CUSTOM.CLF'):
        print(',CUSTOM.CLF',end = '')
        f = open('CUSTOM.CLF','w')
        f.write('https://www.youtube.com/watch?v=,10,10,0.1.2.3.4.5.6.7.8.9.A.B.C.D.E.F.G.H.I.J.K.L.M.N.O.P.Q.R.S.T.U.V.W.X.Y.Z.a.b.c.d.e.f.g.h.i.j.k.l.m.n.o.p.q.r.s.t.u.v.w.x.y.z..,1,,')
        f.close()
    if  not os.path.isfile('history.dat'):
        print(',history.dat',end = '')
        f = open('history.dat','w')
        f.write('The History File')
        f.close()##use mega for packing a backup?
    print(' ...file ops complete')##gen
    
def Play_SP():
    root.destroy()
    Class_Win_Main.Win_Main()
    
def Play_MP():
    root.destroy()
    Class_Win_MP_Lobby.Win_MP_Lobby()
    #Class_Win_MP_Main.Win_Main_MP()
    

SP_Button = Button(root,text = 'Singleplayer',command = Play_SP)#Class_Win_Main.Win_Main)
MP_Button = Button(root,text = 'Multiplayer',command = Play_MP)#Class_Win_MP_Main.Win_Main_MP)
D_label = Label(root,text = 'TED Gamemode selector')
#Class_Win_Main.Win_Main()
#Class_Win_Main.Win_Main_MP()

D_label.pack()#description label
SP_Button.pack()#sp button
MP_Button.pack()#mp button
fs_check()
root.mainloop()


###check settings in sub windows now as settings is just in the main window(will set as arg for instanciation atm)
