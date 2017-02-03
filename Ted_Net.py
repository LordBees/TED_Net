##main initialisation
##http://bit.do/list-of-url-shorteners.php
##http://www.hongkiat.com/blog/url-shortening-services-the-ultimate-list/
import Class_Win_Main,Class_Win_MP_Main
from tkinter import *
## quick window for mp or sp
root = Tk()
root.title('TED Gamemode selector')

def Play_SP():
    Class_Win_Main.Win_Main()
def Play_MP():
    Class_Win_MP_Main.Win_Main_MP()

SP_Button = Button(root,text = 'Singleplayer',command = Play_SP)#Class_Win_Main.Win_Main)
MP_Button = Button(root,text = 'Multiplayer',command = Play_MP)#Class_Win_MP_Main.Win_Main_MP)
#Class_Win_Main.Win_Main()
#Class_Win_Main.Win_Main_MP()

SP_Button.pack()
MP_Button.pack()
root.mainloop()
