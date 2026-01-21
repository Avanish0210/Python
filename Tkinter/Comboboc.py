from tkinter import *
from tkinter.ttk import Combobox

#Created window
window = Tk()

#configuring a winfow
window.title("combobox")
window.geometry("250x250")
window.resizable(height=False , width=False)
window.config(bg="#0fc8ed")


def first_data():
    result = combo.get()
    print(result)
    label.configure(text=result)


label = Label(window , text="text")
label.grid(row=1 , column=1)

combo = Combobox(window)
combo['values'] = ("apple" , "banana " , "mango")
combo.current(0)
combo.grid(row=2 , column=2 , padx=10 , pady=10)

button = Button(window , text="Click here" , command=first_data)
button.grid(row=1,column=0)

window.mainloop()