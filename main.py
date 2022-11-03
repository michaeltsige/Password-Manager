from tkinter import *
from tkinter import messagebox
import random
import json

# window creation and configuration
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)
bgimage = PhotoImage(file="bglock.jpg")
window.config()
#=========== SAVE FUNCTION ==============#


def save():

    website = website_entry.get()
    username = username_entry.get()
    password = password_entry.get()
    new_data = {
        website: {
            "username/email": username,
            "password": password,
        }
    }

    field_not_empty = bool(len(website) and len(username) and len(password))

    if not field_not_empty:
        messagebox.showinfo(
            title="Oops", message="Please make sure you haven't left any empty fields.")
    else:
        try:

            with open("data.json", "r") as data_file:
                data = json.load(data_file)
                data.update(new_data)

        except FileNotFoundError:
            with open("data.json", "w") as data_file:
                json.dump(new_data, data_file, indent=4)
        else:
            with open("data.json", "w") as data_file:
                json.dump(data, data_file, indent=4)
        finally:
            website_entry.delete("0", "end")
            username_entry.delete("0", "end")
            password_entry.delete("0", "end")

#=============Password generator function====================#


def generate_password():

    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y',
               'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    digits = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '*', '+', '?', '@']

    password_letters = [random.choice(letters)
                        for _ in range(random.randint(6, 10))]
    password_digits = [random.choice(digits)
                       for _ in range(random.randint(2, 4))]
    password_symbols = [random.choice(symbols)
                        for _ in range(random.randint(2, 4))]

    password_list = password_letters + password_digits + password_symbols
    random.shuffle(password_list)
    random_password = "".join(password_list)

    password_entry.delete("0", "end")
    password_entry.insert("0", random_password)


#============Password finder function===================#

def find_password():
    website = website_entry.get()
    try:
        with open("data.json") as data_file:
            data = json.load(data_file)

    except FileNotFoundError:
        messagebox.showinfo(title="Oops!", message="No Data File Found!")

    else:
        if website in data:
            username = data[website]["username/email"]
            password = data[website]["password"]
            messagebox.showinfo(
                title="Website", message=f"{username}\n{password}")
        else:
            messagebox.showinfo(
                title="Oops!", message="No Such Website Found!")


# canvas
canvas = Canvas(height=200, width=200)
logo_img = PhotoImage(file="LockLogo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(row=0, column=1)

# Labels

website_label = Label(text="Website: ")
website_label.grid(row=1, column=0)
username_label = Label(text="Email/Username: ")
username_label.grid(row=2, column=0)
password_label = Label(text="Password: ")
password_label.grid(row=3, column=0)


# Entries

website_entry = Entry(width=35)
website_entry.grid(row=1, column=1)
website_entry.focus()
username_entry = Entry(width=55)
username_entry.grid(row=2, column=1, columnspan=2)
password_entry = Entry(width=35)
password_entry.grid(row=3, column=1)


# buttons

search_button = Button(text="Search", width=15, command=find_password)
search_button.grid(row=1, column=2)
generate_password_button = Button(
    text="Generate Password", width=15, command=generate_password)
generate_password_button.grid(row=3, column=2)
add_button = Button(text="Add", width=46, command=save)
add_button.grid(row=4, column=1, columnspan=2)


window.mainloop()
