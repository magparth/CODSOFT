import tkinter as tk
def evaluate_expression():
    try:
        result.set(eval(entry.get()))
    except:
        result.set("Error")
def button_click(event):
    current_text = entry.get()
    text = event.widget.cget("text")
    
    if text == "=":
        evaluate_expression()
    elif text == "C":
        entry.delete(0, tk.END)
    else:
        entry.insert(tk.END, text)
root = tk.Tk()
root.title("Calculator")
entry = tk.Entry(root, font=('Arial', 20))
entry.grid(row=0, column=0, columnspan=4)
button_texts = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    '0', 'C', '=', '+'
]
row, col = 1, 0
for text in button_texts:
    button = tk.Button(root, text=text, font=('Arial', 20),fg="red" ,bg="black")
    button.grid(row=row, column=col)
    button.bind("<Button-1>", button_click)
    col += 1
    if col > 3:
        col = 0
        row += 1
result = tk.StringVar()
result.set("")
result_label = tk.Label(root,text="answer is" ,textvariable=result, font=('Arial', 20))
result_label.grid(row=6, column=0, columnspan=4)
root.mainloop()
