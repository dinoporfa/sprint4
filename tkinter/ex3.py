import tkinter as tk

root= tk.Tk()
root.title('ex3')
root.geometry('300x150')

e_1= tk.Label(root, text="Ola ")
e_1.grid(pady=5)

nome= tk.Entry(root, width= 20)
nome.grid(pady=10)

def saudo():
    nom= nome.get()
    e_1.config(text="Ola "+nom)

b_confirm= tk.Button(root, text="Aceptar", command=saudo)
b_confirm.grid(pady=10)

tk.mainloop()