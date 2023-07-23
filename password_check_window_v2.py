import tkinter as tk
import os

#           Main variables go here
guititle = "Authentication"
trynb = 3
tries = " tries left"

# Window
gui = tk.Tk()
gui.title(guititle)
gui.attributes("-fullscreen", True)
gui.config(bg="blue")

# Widget frames
mainframe = tk.Frame(gui, width=1366, height=768, bg="#333333")
topbanner = tk.Frame(mainframe, width=1366, height=100, bg="#FFFFFF")
userwidgets = tk.Frame(mainframe, width=1366, height=768, bg="#333333")
authwidgets = tk.Frame(gui, width=1366, height=768, bg="#000000")

#           Main functions go here

def psswcheck():
    global trynb, tries, user
    pssw = entry_widget.get()
    print(pssw)
    entry_widget.delete(0, tk.END)
    # checks password for possible users
    if pssw == "XXadminXX":
        user = "admin"
        access_true()
    elif pssw == "spearfish":
        user = "Raccoon De Larbre"
        access_true()
    elif pssw == "heatfromfire":
        user = "Emily"
        access_true()

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
        trynb_widget.config(text=str(trynb) + tries)
        trynb_widget.place(x=520, y=299)
        acsinfolabel.config(text="Access Denied", fg="red")
        gui.after(3000, lambda: acsinfolabel.config(text="Please try again", fg="white"))
        # closes window when trynb hits 0
        if trynb == 0:
            acsinfolabel.config(text="Closing session...", fg="red")
            gui.after(500, gui.destroy)

def on_enter(event):
    enterbutton.invoke()
gui.bind("<Return>", on_enter)

def on_escape(event):
    quitbutton.invoke()
gui.bind("<Escape>", on_escape)

# Widgets (and their locations)
quitbutton = tk.Button(text="Quit", command=gui.destroy)
quitbutton.place(x=1320, y=735)

enterbutton = tk.Button(gui, command=psswcheck)

userinfobutton = tk.Button(topbanner, text="User", bg="black", fg="white", font=("Arial", 11))
userinfobutton.place(x=600, y=323)

entry_widget = tk.Entry(authwidgets, width=15,show="•", bg="black", fg="white", font=("Arial", 11))
entry_widget.place(x=600, y=300)

acsinfolabel = tk.Label(authwidgets, width=13, text="Enter a password", bg="black", fg="white", font=("Arial", 11))
acsinfolabel.place(x=600, y=323)

userwelcome = tk.Label(authwidgets, width=30, text="Welcome", bg="black", fg="white", font=("Arial", 11))
userwelcome.place(x=520, y=275)

trynb_widget = tk.Label(authwidgets, text=str(trynb) + tries, bg="black", fg="white", font=("Arial", 11))
trynb_widget.place(x=520, y=299)

#           Other

def access_true():
    global guititle, tries, trynb
    
    acsinfolabel.config(text="Access Granted", fg="green")
    userwelcome.config(text="Welcome "+ user )
    authwidgets.forget()
    trynb = 3
    guititle = "Home"

def framechoice():
    topbanner.place(x=0, y=0)

    if guititle == "User":
        userwidgets.place(x=0, y=0)
    elif guititle == "Authentication":
        authwidgets.place(x=0, y=0)

entry_widget.focus()

framechoice()

gui.mainloop()