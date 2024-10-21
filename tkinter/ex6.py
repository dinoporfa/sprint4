import tkinter as tk

def ver_frutas():
    selec=lista.curselection()
    element=[lista.get(i) for i in selec]
    eti.config(text=f"Selección: {', '.join(element)}")

root= tk.Tk()
root.title('ex6')
root.geometry('300x300')

fruits=['fresa', 'pexego', 'mango', 'cereixa', 'plátano', 'sandía']

lista= tk.Listbox(root, selectmode=tk.MULTIPLE)
for fruit in fruits:
    lista.insert(tk.END, fruit)
lista.pack(pady=10)

boton= tk.Button(root, text="Ver selección", command= ver_frutas)
boton.pack(pady=5)

eti= tk.Label(root, text="Selección: ningún")
eti.pack(pady=10)

root.mainloop()