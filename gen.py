try:
    from tkinter import *
except ImportError:
    from Tkinter import *
import tkinter.messagebox
import time
import os
from db import entry
from pwgenfunc import RandPass
#=====================================METHODS===================================
def pwGenerator(size = 8):
    data = RandPass(size)
    new_password = data[0]
    pw_strength = data[1]
    pw_color = data[2]
    PASSWORD.set(new_password);
    lbl_strength.configure(foreground="white", background=pw_color, text=pw_strength, font=('sans serif', 10, 'bold'), bd=10, height=1, width=10)
    gui.clipboard_clear()
    gui.clipboard_append(new_password)
    gui.update()
    time.sleep(.02)
    gui.update()
    gui.mainloop()


def save():
    saveg = Toplevel()
    saveg.title('Save Password')
    saveg.geometry('400x350')

    acc_lbl=Label(saveg, font=('sans serif', 12), text="Account", bd=10)
    acc_lbl.grid(row=1,column=1,padx=10,pady=15)
    un_lbl=Label(saveg, font=('sans serif', 12), text="Username", bd=10)
    un_lbl.grid(row=2,column=1,padx=10,pady=15) 
    pw_lbl=Label(saveg, font=('sans serif', 12), text="Password", bd=10)
    pw_lbl.grid(row=3,column=1,padx=10,pady=15)


    Account = Entry(saveg,font=(18), width=24)
    Account.grid(row=1, column=2, columnspan=2)
    username = Entry(saveg, font=(18), width=24)
    username.grid(row=2, column=2, columnspan=2)
    pas = Entry(saveg, textvariable=PASSWORD, font=(18), width=24)
    pas.grid(row=3, column=2, columnspan=2)


    save_btn=Button(saveg,font=('sans serif', 12,'bold'), text="OK", width=15, command=lambda:save_exit())
    save_btn.grid(row=4,column=2,columnspan=2,pady=10)

    def save_exit():
        acc=Account.get()
        un=username.get()
        pw=pas.get()
        entry(acc,un,pw)
        saveg.destroy()
        tkinter.messagebox.showinfo('Succesful','Password saved successfully!')

#=====================================WINDOW===================================
gui = Tk()
gui.title("Password Generator")
width = 600
height = 350
screen_width = gui.winfo_screenwidth()
screen_height = gui.winfo_screenheight()
x = (screen_width/2) - (width/2)
y = (screen_height/2) - (height/2)
gui.geometry("%dx%d+%d+%d" % (width, height, x, y))


#====================================VARIABLES==================================
PASSWORD = StringVar()
PW_SIZE = IntVar()
e1 = Entry(gui, text=PW_SIZE)
PW_SIZE.set(8)

#====================================FRAME======================================
Top = Frame(gui, width=width)
Top.pack(side=TOP)
Form = Frame(gui, width=width)
Form.pack(side=TOP)
Bot = Frame(gui, width=width)
Bot.pack(side=BOTTOM)
#====================================LABEL WIDGET===============================
lbl_title = Label(Top, width=width, font=('sans serif', 12, 'bold'), text="Select: Size >> Click: Generate Now", bd=1, relief=SOLID, background="black",foreground="white")
lbl_title.pack(fill=X)
lbl_password = Label(Form, font=('sans serif', 18), text="Password", bd=10)
lbl_password.grid(row=0, pady=10)
lbl_strength = Label(Form, font=('sans serif', 10, 'bold'), foreground="white", background="#6d0001", text="Weak", bd=10, height=1, width=10)
lbl_strength.grid(row=0, column=3, pady=10, padx=10)
lbl_pw_size = Label(Form, font=('sans serif', 18), text="Size", bd=10)
lbl_pw_size.grid(row=1, pady=10)
lbl_instructions = Label(Bot, width=width, font=('sans serif', 12, 'bold'), text="Result will be on clipboard.", bd=1, relief=SOLID, background="black",foreground="white")
lbl_instructions.pack(fill=X)
#====================================ENTRY WIDGET===============================
password = Entry(Form, textvariable=PASSWORD, font=(18), width=24)
password.grid(row=0, column=1, columnspan=2)
pw_size = Scale(Form, from_=8, to=24, length=230,width=24,sliderlength=14, orient=HORIZONTAL, variable=PW_SIZE, font=(18))
pw_size.grid(row=1, column=1, columnspan=2)


#====================================BUTTON WIDGET==============================
btn_generate = Button(Form,font=('sans serif', 12, 'bold'), text="Generate Now", width=20, command=lambda: pwGenerator(PW_SIZE))
btn_generate.grid(row=2, column=1,pady=10, columnspan=2)
btn_generate1 = Button(Form,font=('sans serif', 12, 'bold'), text="Save", width=20, command=lambda: save())
btn_generate1.grid(row=3, column=1, pady=10, columnspan=2)
#=======================================INITIATOR=================================

gui.mainloop()
