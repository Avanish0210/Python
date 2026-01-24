from tkinter import *
window = Tk()
window.title("Demo")
window.config(bg="#0fc8ed")

label = Label(window , text="hello i am motuu label")
label.grid(row = 0,column=1)
entry = Entry(window , width=10)
entry.grid(row=0,column=2)

def function():
    print("Hello motuuuuuuu")
button = Button(window , text="click me" , command=function)
button.grid(row=0,column=0)
window.mainloop()