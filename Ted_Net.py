##main initialisation
##http://bit.do/list-of-url-shorteners.php
##http://www.hongkiat.com/blog/url-shortening-services-the-ultimate-list/
import Class_Win_Main,Class_Win_MP_Main
from tkinter import *
## quick window for mp or sp
root = Tk()
root.title('TED Gamemode selector')
#root.geometry('300x100')
root.geometry('150x100')

def Play_SP():
    Class_Win_Main.Win_Main()
    root.destroy()
def Play_MP():
    Class_Win_MP_Main.Win_Main_MP()
    root.destroy()

SP_Button = Button(root,text = 'Singleplayer',command = Play_SP)#Class_Win_Main.Win_Main)
MP_Button = Button(root,text = 'Multiplayer',command = Play_MP)#Class_Win_MP_Main.Win_Main_MP)
D_label = Label(root,text = 'TED Gamemode selector')
#Class_Win_Main.Win_Main()
#Class_Win_Main.Win_Main_MP()

D_label.pack()#description label
SP_Button.pack()#sp button
MP_Button.pack()#mp button
root.mainloop()
