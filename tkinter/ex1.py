import tkinter as tk

def cambiar_etiqueta(e):
   e.config(text='clicaches o botón')

root = tk.Tk()
root.title('ex1')
root.geometry("300x150")

e_benvida = tk.Label(root, text='ola')
e_benvida.pack()

e_nome = tk.Label(root, text='lois,')
e_nome.pack()

e_fin = tk.Label(root, text='clica o botón')
e_fin.pack()

boton = tk.Button(root, text='aquí', command= lambda: cambiar_etiqueta(e_fin), bg='blue', fg='white')
boton.pack()

root.mainloop()