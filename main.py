# How to bind the Enter key to a function in Tkinter

from tkinter import Tk, ttk

root = Tk()

root.geometry('400x400')

frm = ttk.Frame(root, padding=10)

frm.grid()

label = ttk.Label(frm, text="Press Enter to update text",
                  font=('Helvetica', 22))
label.grid(column=0, row=0)


def example_func(event):
    print(event)
    print('User pressed Enter')
    label.config(text="bobbyahdz.com")


root.bind('<Return>', example_func)

root.mainloop()