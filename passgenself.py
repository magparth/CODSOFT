import tkinter as tk 
import random
import string
app=tk.Tk()
app.title("password generator")
length_label=tk.Label(app,text= "enter the length:")
length_label.pack()
length_entry=tk.Entry(app)
length_entry.pack()
generatebutton=tk.Button(app,text="generate password:")
generatebutton.pack()
passdisplay=tk.Label(app,text='')
passdisplay.pack()
app.mainloop()
    
