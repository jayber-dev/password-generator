import random
from tkinter import *
from tkinter import messagebox
import json


# ---------------------------- SEARCH MECHANISM --------------------------------#


def search():
    with open("data.json", "r") as data_file:
        file = json.load(data_file)
        web_entry_to_search = web_entry.get()
        if web_entry_to_search in file:
            website_found = file
            email_address = file[web_entry_to_search]['email']
            password_found = file[web_entry_to_search]['password']
            messagebox.showinfo(web_entry_to_search, f"username: {email_address} \n"
                                               f"password: {password_found}")
        else:
            messagebox.showinfo("ooops", F'there is no "{web_entry_to_search}" in the database')
            web_entry.delete(0, END)


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def pass_generator():
    password = ""
    capital_letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S",
                       "T", "U", "V", "W", "X", "Y", "Z"]
    letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u",
               "v", "w", "x", "y", "z"]
    numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", ]
    signs = ["~", "!", "@", '#', "$", "%", "^", "&", "*", "(", ")", "-", "+"]
    pass_entry.delete(0, END)

    for i in range(0, 3):
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
    new_data = {
        website: {
            "email": email,
            "password": password_data}
    }

    if website == "" or email == "" or password_data == "":
        messagebox.showwarning("warning", "there is an empty field")
    else:
        try:
            with open("data.json", "r") as data_file:
                data = json.load(data_file)
                data.update(new_data)

            with open("data.json", "w") as data_file:
                json.dump(data, data_file, indent=4)
        except FileNotFoundError:
            with open("data.json", "w") as data_file:
                json.dump(new_data, data_file, indent=4)

        pass_entry.delete(0, END)
        pass_entry.insert(0, "insert or generate a password")
        email_entry.delete(0, END)
        web_entry.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.config(padx=5, pady=5)
logo = PhotoImage(file="logo.png")
canvas = Canvas(width=250, height=189)
canvas.create_image(150, 99, image=logo)
canvas.grid(row=0, column=1)
# ---------------------------------------- WEBSITE Label ----------------------------------------- #
web_label = Label(text="website", width=5)
web_label.grid(row=1, column=0)

web_entry = Entry(width=50)
web_entry.grid(row=1, column=1)

# --------------------------------- SEARCH BUTTON -----------------------------------#

search_button = Button(text="search", width=16, command=search)
search_button.grid(row=1, column=2)
# ----------------------------------------- email/username LABEL ---------------------- #
email_label = Label(text="e-mail/username")
email_label.grid(row=2, column=0)

email_entry = Entry(width=70)
email_entry.grid(row=2, column=1, columnspan=2)
# ----------------------------------------- password LABEL --------------------------------- #
pass_label = Label(text="password")
pass_label.grid(row=3, column=0)

pass_entry = Entry(window, width=43)
pass_entry.insert(0, "insert or generate a password")
pass_entry.grid(row=3, column=1)

pass_button = Button(text="generate", width=16, command=pass_generator)
pass_button.grid(row=3, column=2)

add_to_file = Button(text="save password to file", width=59, command=save_to_file)
add_to_file.grid(row=4, column=1, columnspan=3)
# ----------------------------- messege box --------------------------------------#


window.mainloop()
