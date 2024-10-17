import tkinter as tk
import sys

root = tk.Tk()
root.title('ex1')
root.geometry("300x150")

def etiqueta():
    e = tk.Label(root, text="fin")
    e.grid(row= 3, column= 3)

b_etiqueta= tk.Button(root, text="Ver texto", command= etiqueta)
b_etiqueta.grid(row= 2, column= 2, padx= 5, pady= 5)

b_fin= tk.Button(root,text="Pechar", command= lambda: sys.exit())
b_fin.grid(row= 13, column= 4, padx= 5, pady=5)

tk.mainloop()