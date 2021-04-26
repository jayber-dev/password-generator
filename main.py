import random
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def pass_generator()
    letters = [a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u,v,w,x,y,z]
    numbers = [0,1,2,3,4,5,6,7,8,9,]
    signs = [~,!,@,'#',$,%,^,&,*,(,),-,+ ]
# ---------------------------- SAVE PASSWORD ------------------------------- #

# ---------------------------- UI SETUP ------------------------------- #
from tkinter import *

window = Tk()
window.config(padx=10,pady=10)
logo = PhotoImage(file="logo.png")
canvas = Canvas(width=250, height=189)
canvas.create_image(150, 99, image=logo)
canvas.grid(row=0,column=1)
# ---------------------------------------- Label ---------------------------------------------
web_label = Label(text="website",width=5)
web_label.grid(row=1, column=0)

web_entry = Entry(width=70)
web_entry.grid(row=1, column=1, columnspan=2)
# ----------------------------------------- email/username LABEL ------------------------------
email_label = Label(text="e-mail/username")
email_label.grid(row=2, column=0)

email_entry = Entry(width=70)
email_entry.grid(row=2, column=1, columnspan=2)
# ----------------------------------------- password LABEL ------------------------------------
pass_label = Label(text="password")
pass_label.grid(row=3, column=0)

pass_entry = Entry(width= 43)
pass_entry.grid(row=3, column=1)

pass_button = Button(text="generate",width=16)
pass_button.grid(row=3, column=2)

add_to_file = Button(text="add details", width=60)
add_to_file.grid(row=4, column=1, columnspan=3)

window.mainloop()
