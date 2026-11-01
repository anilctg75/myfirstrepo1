import tkinter as tk
from time import strftime

root = tk.Tk()
clock = tk.Label(root, font=("Arial", 60))
clock.pack()

def update():
    clock.config(text=strftime("%H:%M:%S"))
    root.after(1000, update)

update()
root.mainloop()