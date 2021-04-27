import random

# ---------------------------- FILE CREATION ----------------------------#
details_file = open("datafile.txt", "w")
details_file.write("website, user/email, password \n")
details_file.close()


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def pass_generator():
    password = ""
    capital_letters = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
    letters = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
    numbers = ["0","1","2","3","4","5","6","7","8","9",]
    signs = ["~","!","@",'#',"$","%","^","&","*","(",")","-","+" ]
    pass_entry.delete(0,END)

    for i in range(0,3):
        letters_value = random.choice(letters)
        capital_letters_value = random.choice(capital_letters)
        numbers_value = random.choice(numbers)
        signs_value = random.choice(signs)

        password = str(password + letters_value + capital_letters_value + numbers_value + signs_value)
        
    pass_entry.insert(0, password)
    

# ---------------------------- SAVE DETAILS------------------------------ #

def save_to_file():
    website = web_entry.get()
    email = email_entry.get()
    password_data = pass_entry.get()


    details_file = open("datafile.txt", "a")
    details_file.write(f"{website}, {email}, {password_data}  \n")
    details_file.close()


# ---------------------------- UI SETUP ------------------------------- #
from tkinter import *

window = Tk()
window.config(padx=10,pady=10)
logo = PhotoImage(file="logo.png")
canvas = Canvas(width=250, height=189)
canvas.create_image(150, 99, image=logo)
canvas.grid(row=0,column=1)
# ---------------------------------------- Label ----------------------------------------- #
web_label = Label(text="website",width=5)
web_label.grid(row=1, column=0)

web_entry = Entry(width=70)
web_entry.grid(row=1, column=1, columnspan=2)
# ----------------------------------------- email/username LABEL ---------------------- #
email_label = Label(text="e-mail/username")
email_label.grid(row=2, column=0)

email_entry = Entry(width=70)
email_entry.grid(row=2, column=1, columnspan=2)
# ----------------------------------------- password LABEL --------------------------------- # 
pass_label = Label(text="password")
pass_label.grid(row=3, column=0)

pass_entry = Entry(window, width= 43)
pass_entry.insert(0,"insert or generate a password")
pass_entry.grid(row=3, column=1)

pass_button = Button(text="generate",width=16, command=pass_generator)
pass_button.grid(row=3, column=2)

add_to_file = Button(text="save password to file", width=59, command=save_to_file)
add_to_file.grid(row=4, column=1, columnspan=3)

window.mainloop()
