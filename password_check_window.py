import tkinter as tk
import os

# window
root = tk.Tk()
root.title("Password Check Window")
root.attributes("-fullscreen", True)
root.configure(bg="#5A5A5A")


# 'accounts' in the app
user = "blank"

# password check and countdown
trynb = 3
# tries variable is only for grammar
tries = " tries left"
def psswcheck():
    global trynb, tries, user
    pssw = entry_widget.get()
    entry_widget.delete(0, tk.END)
    # checks password for 2 possible users
    if pssw == "spearfish":

        trynb = 3
        user = "admin"
        tries = " tries left"

        acsinfolabel.config(text="Access Granted", fg="green")
        userwelcome.config(text="Welcome "+ user )
        trynb_widget.place_forget()
        openuserfile.place(x=600, y=125)

    elif pssw == "heatfromfire":

        trynb = 3
        user = "Emily"
        tries = " tries left"

        acsinfolabel.config(text="Access Granted", fg="green")
        userwelcome.config(text="Welcome "+ user )
        trynb_widget.place_forget()
        openuserfile.place(x=600, y=125)
    else:
        # makes sure trynb doesn't go below 0
        if trynb > 0:
            trynb -= 1
        # correct grammar is important
        if trynb == 1:
            tries = " try left"
        else:
            tries = " tries left"
        # updates trynb widget & info widget
        userwelcome.config(text="Welcome")
        openuserfile.place_forget()
        trynb_widget.config(text=str(trynb) + tries)
        trynb_widget.place(x=125, y=75)
        acsinfolabel.config(text="Access Denied", fg="red")
        root.after(3000, lambda: acsinfolabel.config(text="Please try again", fg="white"))
        # closes window when trynb hits 0
        if trynb == 0:
            acsinfolabel.config(text="closing session...", fg="red")
            root.after(500, root.destroy)

# opens user file
def openfile():
    global user
    file_path = ""
    if user == "admin":
        file_path = "C:\\Users\\anato\\Desktop\\password_check_user_files\\admin"
        os.startfile(file_path)
    elif user == "Emily":
        file_path = "C:\\Users\\anato\\Desktop\\password_check_user_files\\emily"
        os.startfile(file_path)

# binds the enter key to the enter button
def on_enter(event):
    enterbutton.invoke()
root.bind("<Return>", on_enter)

def on_escape(event):
    quitbutton.invoke()
root.bind("<Escape>", on_escape)

# buttons
enterbutton = tk.Button(root, command=psswcheck)

openuserfile = tk.Button(root, width=16, text="Open your file", bg="black", fg="white", command=openfile)

quitbutton = tk.Button(root, text="Quit", bg="black", fg="white", command=root.destroy)

# entry widget
entry_widget = tk.Entry(root, width=15,show="•", bg="black", fg="white", font=("Arial", 11))

# info widget
acsinfolabel = tk.Label(root, width=13, text="Enter a password", bg="black", fg="white", font=("Arial", 11))

userwelcome = tk.Label(root, width=13, text="Welcome", bg="black", fg="white", font=("Arial", 11))

trynb_widget = tk.Label(root, text=str(trynb) + tries, bg="black", fg="white", font=("Arial", 11))

# widget locations/places widgetsS
entry_widget.place(x=600, y=300)
acsinfolabel.place(x=600, y=323)
trynb_widget.place(x=125, y=75)
userwelcome.place(x=600, y=275)
quitbutton.place(x=1320, y=735)

root.mainloop()