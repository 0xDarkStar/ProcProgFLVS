from tkinter import *
from tkinter import ttk

def main():
    root = Tk()
    frm = ttk.Frame(root, padding=10)
    frm.grid()
    ttk.Label(frm, text="Hello World").grid(column=1, row=1)
    ttk.Button(frm, text="Quit", command=root.destroy).grid(column=2, row=4)
    root.mainloop()

main()