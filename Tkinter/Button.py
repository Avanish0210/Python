from tkinter import *
window = Tk()
window.title("Button")
window.geometry("250x250")
window.config(bg="#0fc8ed")



 
label = Label(window , width=10 , text="First Input" )
label.grid(row=0,column=0)

label2 = Label(window , width=10 )
label2.grid(row=1,column=0)

entry = Entry(window , width=20)
entry.grid(row=0 , column=1)

def first_entry():
    print("Taking your first entry")
    result = entry.get()
    label2.configure(text=result)
    print(result)

button = Button(window , width=10 , text="Click here"  , command=first_entry)
#button.place(x=10,y=10)
button.grid(row=0,column=2 ,padx=10) 
window.mainloop()