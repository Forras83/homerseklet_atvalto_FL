import tkinter as tk
from fl_gui import FLApp

def main():
    root = tk.Tk()
    root.title("Grafikus Hőmérséklet Átváltó.app")
    root.geometry("400x300")
    app = FLApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()