try:
    from tkinter import *
except ImportError:
    from Tkinter import *
from db import display
import time
import os
def show():
	showg = Toplevel()
	showg.title('Save Password')
	showg.geometry('600x500')


	Top = Frame(showg, width=600)
	Top.pack(side=TOP)
	Form = Frame(showg, width=600)
	Form.pack(side=TOP)
	Bot = Frame(showg, width=600)
	Bot.pack(side=BOTTOM)
	

	data=display()
	lbl_title = Label(Top, width=600, font=('sans serif', 20, 'bold'), text="Saved Passwords ", bd=1, relief=SOLID, background="black",foreground="white")
	lbl_title.pack(fill=X)
	lbl_instructions = Label(Bot, width=width, font=('sans serif', 12, 'bold'), text="Don't share your passwords with anyone..", bd=1, relief=SOLID, background="black",foreground="white")
	lbl_instructions.pack(fill=X)
	
	Label(Form, text="Account", font=('sans serif', 12 ,'bold'), background="black",foreground="white",padx=20).grid(row=0, column=0,pady=20,padx=20)
	Label(Form, text="Username", font=('sans serif', 12,'bold'), background="black",foreground="white",padx=20).grid(row=0, column=1,pady=20,padx=20)
	Label(Form, text="Password", font=('sans serif', 12,'bold'), background="black",foreground="white",padx=20).grid(row=0, column=2,pady=20,padx=20)
	
	for index, dat in enumerate(data):
	    Label(Form, text=dat[0], font=('sans serif', 12), bd=1).grid(row=index+1, column=0)
	    Label(Form, text=dat[1], font=('sans serif', 12), bd=1).grid(row=index+1, column=1)
	    Label(Form, text=dat[2], font=('sans serif', 12), bd=1).grid(row=index+1, column=2)

	btn_exit = Button(Form,font=('sans serif', 12, 'bold'), text="Exit", width=20, background="black",foreground="white",command=lambda:showg.destroy())
	btn_exit.grid(row=100, column=2,pady=50,padx=50, columnspan=2)


gui = Tk()
gui.title("Main Menu")
width = 350
height = 350

gui.geometry("%dx%d+%d+%d" % (width, height, 10, 10))

Top = Frame(gui, width=width)
Top.pack(side=TOP)
Form = Frame(gui, width=width)
Form.pack(side=TOP)
Bot = Frame(gui, width=width)
Bot.pack(side=BOTTOM)


lbl_title = Label(Top, width=width, font=('verdana', 25, 'bold'), text=" Welcome!! ",pady=20,background="black", foreground="white")
lbl_title.pack(fill=X)
lbl_instructions = Label(Bot, width=width, font=('sans serif', 12, 'bold'), text="Save/write your passwords before exiting!!", bd=1, relief=SOLID ,background="black", foreground="white")
lbl_instructions.pack(fill=X)


btn_gen = Button(Form,font=('sans serif', 15, 'bold'), text="Generate Password", width=20, command=lambda:(os.system("python gen.py")))
btn_gen.grid(row=2, column=1,pady=10, columnspan=2)
btn_show = Button(Form,font=('sans serif', 15, 'bold'), text="Show Passwords", width=20, command=lambda:show())
btn_show.grid(row=3, column=1,pady=10, columnspan=2)
btn_show = Button(Form,font=('sans serif', 15, 'bold'), text="Exit", width=20, command=lambda:gui.destroy())
btn_show.grid(row=4, column=1,pady=10, columnspan=2)


gui.mainloop()