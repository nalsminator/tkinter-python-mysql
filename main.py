from tkinter import *
from ventana import *
import sv_ttk

def main():
    root=Tk()
    root.wm_title("Crud Python SqlServer")
    app = Ventana(root)
    app.mainloop()
sv_ttk.set_theme("dark")

if __name__== "__main__":
    main()