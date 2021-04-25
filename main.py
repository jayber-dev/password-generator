# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

# ---------------------------- UI SETUP ------------------------------- #
from tkinter import *

window = Tk()
logo = PhotoImage(file="logo.png")
canvas = Canvas(width=300, height=189)
canvas.create_image(220, 99, image=logo)
canvas.grid()
# ---------------------------------------- Label ---------------------------------------------
web_label = Label(text="website")
web_label.grid(row=1, column=0)
# ---------------------------------------- ENTRY ---------------------------------------------
web_entry = Entry()
web_entry.grid(row=1, column=1)
# ----------------------------------------- email/username LABEL ------------------------------
email_label = Label(text="e-mail/username")
email_label.grid(row=2, column=0)
# ----------------------------------------- email/username ENTRY ------------------------------
email_entry = Entry()
email_entry.grid(row=2, column=1)
# ----------------------------------------- password LABEL ------------------------------------
pass_label = Label(text="password")
pass_label.grid(row=3, column=0)
# ----------------------------------------- password ENRTY ------------------------------------
pass_entry = Entry()
pass_entry.grid(row=3, column=1)

window.mainloop()
