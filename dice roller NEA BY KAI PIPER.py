from tkinter import *
from tkinter import ttk
from PIL import ImageTk,Image
import os
import random
window = Tk()
window.title("Dice Roller")

#GUI -- Labels
ttk.Label(window, text='''Type of Dice/
Number of sides''',font=('helvetica', 10)).pack()
ttk.Label(window, text='''Number of Dice''',font=('helvetica', 10)).pack()
#GUI -- Comboboxs
cmb = ttk.Combobox(window, width="10", values=("D4","D6","D8","D10"))
cmb.current(0)
cmb.pack()


spin = ttk.Spinbox(window, from_=1, to=100, width=5)
spin.set(1)
spin.pack()

               

def Start():
    Dicenum = int(spin.get())
    if cmb.get() == "D4":
        
        for i in range (Dicenum):


            D4= random.randint(1, 6)
            print(D4)
            canvas = Canvas(window, width = 60, height = 60)      
            canvas.pack(side=LEFT)
            img = ImageTk.PhotoImage(file="die" + str(D4) + ".png")
            canvas.create_image(20, 20, image=img)
            canvas.image = img
            canvas.pack()


    if cmb.get() == "D6":
        for i in range(Dicenum):
            D4=[random.randint(1, 12)]
            print(D4)
    if cmb.get() == "D8":
        for i in range(Dicenum):
            D4=[random.randint(1, 24)]
            print(D4)
    if cmb.get() == "D10":
        for i in range(Dicenum):
            D4=[random.randint(1, 48)]
            print(D4)

    
    
Start_button = ttk.Button(window, text='Start', command=Start).pack()
window.resizable(False, False)
window.mainloop()
