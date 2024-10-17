import tkinter as tk

root= tk.Tk()
root.title('ex5')
root.geometry('300x200')

def act():
    pink= pinky.get()
    root.config(bg=pink)

pinky= tk.StringVar()

titulo= tk.Label(root, text="Selecciona a cor da ventá emerxente:")
titulo.pack(pady=5)

vermello= tk.Radiobutton(root, text="Vermello", variable=pinky, value="red", command= act)
vermello.pack(pady=3)
rosa= tk.Radiobutton(root, text="Rosa", variable=pinky, value="lightpink", command= act)
rosa.pack(pady=3)
azul= tk.Radiobutton(root, text="Azul", variable=pinky, value="lightblue", command= act)
azul.pack(pady=3)

tk.mainloop()