import tkinter as tk
import os

guititle = "Home"

# window
gui = tk.Tk()
gui.title(guititle)
gui.attributes("-fullscreen", True)
gui.config(bg="#000000")

# buttons and their locations
quitbutton = tk.Button(text="Quit", command=gui.destroy)
quitbutton.place(x=1320, y=735)

# homepage widgets
homepagewidgets = tk.Frame(gui, width=1366, height=768, bg="#333333")

#             Functions go here


def on_escape(event):
    quitbutton.invoke()
gui.bind("<Escape>", on_escape)

gui.mainloop()
