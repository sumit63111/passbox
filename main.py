from tkinter import *
from tkinter import messagebox
import random
import pyperclip

#**********password Generator************

def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')','+']

    nr_letter=random.randint(4, 6)
    nr_symbols=random.randint(3, 4)
    nr_number=random.randint(2, 4)

    password_letter=[random.choice(letters) for _ in range(nr_letter)]
    password_number=[random.choice(numbers) for _ in range(nr_number)]
    password_symbols=[random.choice(symbols) for _ in range(nr_symbols)]
    
    password_list=password_letter+password_number+password_symbols
    random.shuffle(password_list)
    password="".join(password_list)
    pwd_entry.insert(0, password)

    pyperclip.copy(password)

#*********save password******************

def save():
    website=website_entry.get()
    email=email_entry.get()
    password=pwd_entry.get()

    if len(website)==0 or len(password) == 0:
        messagebox.showinfo(title=website, message="Please Make Sure that each and every field is filled up!")
     
    is_ok=messagebox.askokcancel(title=website, message=f"These are the details entered : \nEmail: {email} \nPassword: {password} \nAre you sure you want to save this? ")

    if is_ok:
        with open ("da.txt","a") as data_file:
            data_file.write(f"{website} | {email} | {password}\n")
            website_entry.delete(0,END)
            pwd_entry.delete(0,END)


#*******UI Setup************
window=Tk()
window.title("Password  Manager")
window.config(padx=50, pady=50)

canvas= Canvas(height=200, width=200)
img=PhotoImage(file="logo.gif")
canvas.create_image(125,100,image=img)
canvas.grid(row=0, column=1)

#labels
website_label=Label(text="Website :")
website_label.grid(row=1,column=0)
email_label=Label(text="Email :")
email_label.grid(row=2,column=0)
pwd=Label(text="Password :")
pwd.grid(row=3,column=0)

#Entries
website_entry=Entry(width=53)
website_entry.grid(row=1,column=1,columnspan=2)
email_entry=Entry(width=53)
email_entry.grid(row=2,column=1,columnspan=2)
email_entry.insert(0, "example@gmail.com")
pwd_entry=Entry(width=35)
pwd_entry.grid(row=3,column=1)

#buttons
generate_password=Button(text="Generate Password",width=14, command=generate_password) 
generate_password.grid(row=3,column=2)
add_button=Button(text="Add",width=36,command=save)
add_button.grid(row=4,column=1,columnspan=2)



window.mainloop()