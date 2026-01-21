from tkinter import *

#Created window
window = Tk()

#configuring a winfow
window.title("Demo")
window.geometry("250x250")
window.resizable(height=False , width=False)
window.config(bg="#0fc8ed")

#label
label1 = Label(window , width=10 , text="Avanish" , font= ("Arial bold",15) , anchor="nw")
label1.grid(row=0,column=0)
label2 = Label(window , width=10 , text="Singh" , font= ("Arial bold",15) , anchor="nw")
#label2.place(x=10,y=60)
#label2.pack(side=BOTTOM)
label2.grid(row=1,column=0)
window.mainloop()
