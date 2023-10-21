import tkinter as tk 
import random
import string
def genpass(length):
    chartacter= string.ascii_letters + string.digits + string.punctuation
    password=''.join(random.choice(chartacter)for _ in range(length))
    return password
def genpassbuton():
    length=int(length_entry.get())
    password=genpass(length)
    passdisplay.config(text="generated password is:"+password)
app=tk.Tk()
app.title("password generator")
length_label=tk.Label(app,text= "enter the length:")
length_label.pack()
length_entry=tk.Entry(app)
length_entry.pack()
generatebutton=tk.Button(app,text="generate password:",command=genpassbuton)
generatebutton.pack()
passdisplay=tk.Label(app,text='')
passdisplay.pack()
app.mainloop()
    
