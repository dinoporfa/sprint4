import tkinter as tk

root= tk.Tk()
root.title('ex7')
root.geometry('400x600')

eci= tk.Label(root, text="CÍRCULO")
eci.pack(pady=1)

eci1= tk.Label(root, text="radio")
eci1.pack(pady=1)
enr= tk.Entry(root, width=3)
enr.pack(pady=1)
r=enr.get()

eci2= tk.Label(root, text="x")
eci2.pack(pady=1)
encx= tk.Entry(root, width=4)
encx.pack(pady=1)
cx= encx.get()

eci3= tk.Label(root, text="y")
eci3.pack(pady=1)
ency= tk.Entry(root, width=4)
ency.pack(pady=1)
cy= ency.get()


ere= tk.Label(root, text="RECTÁCGULO")
ere.pack(pady=1)

ere1= tk.Label(root, text="lado menor")
ere1.pack(pady=1)
enlme= tk.Entry(root, width=2)
enlme.pack(pady=1)
lme=enlme.get()

ere2= tk.Label(root, text="lado maior")
ere2.pack(pady=1)
enlma= tk.Entry(root, width=3)
enlma.pack(pady=1)
lma=enlma.get()

ere3= tk.Label(root, text="x")
ere3.pack(pady=1)
enrex= tk.Entry(root, width=4)
enrex.pack(pady=1)
rex= enrex.get()

ere4= tk.Label(root, text="y")
ere4.pack(pady=1)
enrey= tk.Entry(root, width=4)
enrey.pack(pady=1)
rey= enrey.get()

canvas= tk.Canvas(root, width=350, height= 250, bg="white")
canvas.pack(pady=1)

canvas.create_rectangle(rex, rex, rey, rey, )

root.mainloop()