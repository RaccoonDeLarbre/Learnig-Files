import tkinter as tk

# window
root = tk.Tk()
root.title("Password Check Window")
root.geometry("500x300")
root.configure(bg="#5A5A5A")

# accounts in the app
user = ""

# trick button function
def b_trick():
    current_text = trickbutton["text"] 

    if current_text == "clickme":
        trickbutton["text"] = "Click Me again!"
    elif current_text == "Click Me again!":
        trickbutton["text"] = "and... again"
    elif current_text == "and... again":
        trickbutton["text"] = "click me once more"
    else:
        trickbutton["text"] = "clickme"

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
        trynb_widget.config(text=str(trynb) + tries)
    elif pssw == "heatfromfire":

        trynb = 3
        user = "Emily"
        tries = " tries left"

        acsinfolabel.config(text="Access Granted", fg="green")
        userwelcome.config(text="Welcome "+ user )
        trynb_widget.config(text=str(trynb) + tries)
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
        acsinfolabel.config(text="Access Denied", fg="red")
        root.after(3000, lambda: acsinfolabel.config(text="Please try again", fg="white"))
        # closes window when trynb hits 0
        if trynb == 0:
            root.after(500, root.destroy)

# binds the enter key to the enter button
def on_enter(event):
    enterbutton.invoke()
root.bind("<Return>", on_enter)

# buttons
trickbutton = tk.Button(root, text="clickme", bg="black", fg="white", command=b_trick)

enterbutton = tk.Button(root, command=psswcheck)

# entry widget
entry_widget = tk.Entry(root, width=15,show="•", bg="black", fg="white", font=("Arial", 11))

# info widget
acsinfolabel = tk.Label(root, width=13, text="Enter a password", bg="black", fg="white", font=("Arial", 11))

userwelcome = tk.Label(root, width=13, text="Welcome", bg="black", fg="white", font=("Arial", 11))

trynb_widget = tk.Label(root, text=str(trynb) + tries, bg="black", fg="white", font=("Arial", 11))

# widget locations/places widgetsS
trickbutton.place(x=50, y=30)
entry_widget.place(x=200, y=75)
acsinfolabel.place(x=200, y=100)
trynb_widget.place(x=125, y=75)
userwelcome.place(x=200, y=50)

root.mainloop()