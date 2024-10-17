import tkinter as tk

root= tk.Tk()
root.title('ex4')
root.geometry('300x200')

def afis():
    lers= ler_c.get()
    pasears= pasear_c.get()
    xogars= xogar_c.get()
    afi2.config(text="  ler  ") if lers else afi2.config(text="")
    afi3.config(text="  pasear  ") if pasears else afi3.config(text="")
    afi4.config(text="  xogar videoxogos  ") if xogars else afi4.config(text="")

ler_c= tk.IntVar()
pasear_c= tk.IntVar()
xogar_c= tk.IntVar()

ler= tk.Checkbutton(root, text= "Lectura", variable= ler_c, command= afis)
ler.grid(pady=1)
pasear= tk.Checkbutton(root, text= "Paseos", variable= pasear_c, command= afis)
pasear.grid(pady=1)
xogar= tk.Checkbutton(root, text= "Videoxogos", variable= xogar_c, command= afis)
xogar.grid(pady=1)

afi1= tk.Label(root, text="Gústame...")
afi1.grid(pady=2)
afi2= tk.Label(root, text="")
afi2.grid(pady=1)
afi3= tk.Label(root, text="")
afi3.grid(pady=1)
afi4= tk.Label(root, text="")
afi4.grid(pady=1)

tk.mainloop()