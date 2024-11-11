import tkinter as tk
import GameController
import GameModel

root = tk.Tk()
root.title('sprint4')
root.geometry('300x300')
controller = GameController()

if __name__ == "__main__":
    model = GameModel()
    model.difficulty('neutral')
    model.pname('heineken')

    
    root.mainloop()